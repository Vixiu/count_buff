import copy
from copy import deepcopy

from Config import *

def count_buff(buff_amount: int, intellect: int,xs: int,xyz,arm=1.08):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    """
    :param xyz:
    :param buff_amount: 增益量
    :param intellect: 四维
    :param xs: 系数

    :param arm:
    :return: 函数
    """
    x, y, z = xyz
    def count(fixed, bfb: list, basic:int,cp_arms: bool) -> int:
        """
        :param cp_arms: cp武器
        :param fixed: 固定加成
        :param bfb: 百分比加成
        :param basic: 基础数值
        :return:
        """
        old_buff = ((basic + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        buff_ = (old_buff + new_buff) * (arm if cp_arms else 1)
        return round(buff_)
    return count

def compare_and_update(base_dict, target_dict):
    diff = {}
    for key, value in base_dict.items():
        if isinstance(value, dict) and isinstance(target_dict.get(key), dict):
            nested_diff = compare_and_update(value, target_dict[key])
            if nested_diff:
                diff[key] = nested_diff
        elif target_dict.get(key) != value:
            diff[key] = value
    return diff


class Buff:
    def __init__(self):
        self._base_result=[]
        self._backup_data = deepcopy(DEFAULT_INPUT_DATA)
        self._offset=0
        self._data = {}
        self._job=''
    @property
    def _buff_amount_in_map(self):
        """
        进图增益量
        :return:
        """
        return    (
            (self._data['buff_amount']['in_map'] + self._data['buff_amount']['out_map']) *
            (1 + self._data['buff_amount']['enh'] / 100 + self._data['bxy']['enh'] / 100)
        )
    @property
    def _buff_amount_out_map(self):
        """
        图外增益量
        :return:
        """
        return (
            self._data['buff_amount']['out_map'] * (1 + self._data['buff_amount']['enh'] / 100)
        )
    @property
    def data(self)->dict:
        return self._data
    @property
    def job(self)->str:
        return  self._job

    def _count_buff(self,intellect,buff_amount,lv)->dict:
        count = count_buff(
            buff_amount,
            intellect,
            CLASS[ self._job]['buff']['xs'],
            CLASS[ self._job]['buff']['xyz'],
            1.008 if  self._job == 'ba' else 1.08
        )
        return {
        'attack': count(
            self._data['bxy']['fixed_attack'],
            self._data['bxy']['percentage_attack'],
            CLASS[ self._job]['buff']['attack'][lv - 1],
            self._data['cp_arms'],
        ),
        'intellect': count(
            self._data['bxy']['fixed_intellect'],
            self._data['bxy']['percentage_intellect'],
            CLASS[ self._job]['buff']['intellect'][lv - 1],
            False
        )}

    def _count_ty(self,intellect)->list:
        """
        计算太阳
        :param intellect: 四维
        :return:
        """
        data=CLASS[self._job]
        count = count_buff(
            self._buff_amount_in_map,
            intellect,
            data['ty1']['xs'],
            data['ty1']['xyz'],
        )
        ty1=count(self._data['bxy']['fixed_ty'],
                  self._data['bxy']['percentage_ty'],
                  data['ty1']['intellect'][self._data['ty']['ty1_lv']- 1],
                  False
                  )
        ty3=round(ty1 * (
            ( data['ty3']['bind1'] if self._data['ty']["is_ty1"] else data['ty3']['bind2+1'])
                        + self._data['ty']['ty3_lv'] * data['ty3']['growth'])
                        )
        return [
            {'attack': '-','intellect': ty1},
            {'attack': '-', 'intellect': ty3},
        ]
    def _count_multiplier(self, attack, intellect, damage_increase)->float:
        """
        倍率计算
        :param attack: 三攻
        :param intellect: 力智
        :param damage_increase: 增伤
        :return:
        """
        return round(
            (1 + attack / self._data['c_attack']) *
            (1 + intellect / (self._data['c_intellect'] + 250)) * damage_increase
            , 2)
    def _set_multiplier(self,res:list):
        for item in res:
            attack,intellect=item['attack'],item['intellect']
            if attack =='-':
                item['multiplier']='-'
            else:
                item['multiplier']=self._count_multiplier(attack,intellect,CLASS[self._job]['damage_increase'])
        return res

    def _get_job_buff(self):
        # 计算地图内外四维偏移
        intellect_in,intellect_out=self._offset,self._offset
        passive_skill = CLASS[self._job]['passive_skill']
        for i,lv1 in self._data['skill'].items():
            it = passive_skill[i]['data'][lv1 - 1] - passive_skill[i]['data'][self._backup_data['skill'].get(i,1)-1]
            intellect_in+=it
            if passive_skill[i]['out_map']:
                intellect_out+=it

        data=CLASS[self._job]
        # 计算基础buff
        result = [self._count_buff(
            intellect_out + self._data['buff']['intellect_out'],
            self._buff_amount_out_map,
            self._data['buff']['lv_out'])]
        in_map=self._count_buff(
            intellect_in + self._data['buff']['intellect_in'],
            self._buff_amount_in_map,
            self._data['buff']['lv_in']
        )
        result.append(in_map)
        for item in data['skill_form']:
            result.append({
                'attack': round(in_map['attack'] * item['multiplier']),
                'intellect': round(in_map['intellect'] * item['multiplier']),
            })
        result+=self._count_ty(intellect_in + self._data['ty']['intellect'])
        # 添加total_buff总数据
        for item in data['total_buff']:
            result.append({
                key: sum(
                    0 if isinstance(result[i][key], str) else result[i][key]
                    for i in item['value']
                )
                for key in ['attack', 'intellect']
            })

        # 计算倍率
        result=self._set_multiplier(result)
        result[0]['multiplier']='-' # 站街倍率设置为空

        return result

    def _diff(self, ls:list):
        result =[]
        for item1,item2 in zip(ls,self._base_result):
            _={}
            for k,v in item1.items():
                if v =='-' or item2[k]=='-':
                    _[k]='-'
                elif k=='multiplier':
                    _[k] = round(v-item2[k],2)
                else:
                    _[k]=v-item2[k]
            result.append(_)
        return result

    def _check_lv(self):
        job= CLASS[self._job]
        self._data['buff']['lv_out']=max(1, min(self._data['buff']['lv_out'],job['buff']['max_lv']))
        self._data['buff']['lv_in'] = max(1, min(self._data['buff']['lv_in'], job['buff']['max_lv']))
        self._data['ty']['ty1_lv']=max(1, min(self._data['ty']['ty1_lv'], job['ty1']['max_lv']))
        self._data['ty']['ty3_lv']=max(1, min(self._data['ty']['ty3_lv'], job['ty3']['max_lv']))
        for i in self._data['skill']:
            self._data['skill'][i]=max(1,min(self._data['skill'][i],job['passive_skill'][i]['max_lv']))


    #------------------
    def add_lv(self,min_lv,max_lv,count):
        """
        :param min_lv:
        :param max_lv:
        :param count:
        :return:
        """

        result=[]
        job= CLASS[self._job]
        data=deepcopy(self._data)
        if min_lv <=job['buff']['lv'] <=max_lv:
            lv=job['buff']['lv']
            result.append(
                {   'lv':lv,
                    'name': f"{job['buff']['name']}(图外)",
                    'old_lv':self._data['buff']['lv_out'],
                    'new_lv': lambda :self._data['buff']['lv_out'],
                    'increase': ''
                }
            )
            result.append(
                {   'lv':lv,
                    'name': f"{job['buff']['name']}(图内)",
                    'old_lv': self._data['buff']['lv_in'],
                    'new_lv': lambda :self._data['buff']['lv_in'],
                    'increase': ''
                }
            )
            self._data['buff']['lv_out'] += count
            self._data['buff']['lv_in'] += count
        if min_lv <= job['ty1']['lv'] <= max_lv:
            result.append(
                {'lv': job['ty1']['lv'],
                 'name': job['ty1']['name'],
                 'old_lv': self._data['ty']['ty1_lv'],
                 'new_lv': lambda :self._data['ty']['ty1_lv'],
                 'increase': ''
                 }
            )
            self._data['ty']['ty1_lv'] += count
        if min_lv <=job['ty3']['lv'] <= max_lv:
            result.append(
                {'lv': job['ty3']['lv'],
                 'name': job['ty3']['name'],
                 'old_lv': self._data['ty']['ty3_lv'],
                 'new_lv': lambda :self._data['ty']['ty1_lv'],
                 'increase': ''
                 }
            )
            self._data['ty']['ty3_lv'] += count
        job=job['passive_skill']
        for i in self._data['skill']:
            if min_lv<=job[i]['lv']<=max_lv:
                lv=self._data['skill'][i]
                new_lv=max(1, min(lv+count,len(job[i]['data'])))
                result.append(
                    {'lv':job[i]['lv'] ,
                     'name': job[i]['name'],
                     'old_lv': lv,
                     'new_lv': lambda y=i: self._data['skill'][y],
                     'increase': job[i]['data'][new_lv-1]-job[i]['data'][lv-1]
                     }
                )
                self._data['skill'][i]+=count
        self._check_lv()
        for item in result:
            print(item['new_lv']())
            item['new_lv']=item['new_lv']()

        return {'result':result,'data':compare_and_update(self._data,data)}

    def get_value(self,*keys):
        data = self._data
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return None
        return data


    def set_base(self):
        self._data['buff']['intellect_out']+=self._offset
        self._data['buff']['intellect_in'] += self._offset
        self._data['ty']['intellect'] += self._offset
        self._offset=0
        self._data['skill'] =self._backup_data ['skill']
        self._backup_data = deepcopy(self._data)

        self._base_result=self._get_job_buff()

    def set_base_skill(self):
        self._backup_data['skill']=deepcopy(self._data['skill'])
        #self._base_result = self._get_job_buff()

    def set_data(self,data):
        for i, _ in enumerate(CLASS[self._job]['passive_skill']):
            if i not in data['skill']:
                data['skill'][i]=1
        self._data=deepcopy(data)
        self._offset = 0

    def set_value(self, value,*keys):
        # 遍历到待修改的目标位置
        cur = self._data
        for key in keys[:-1]:
            cur = cur[key]
        last_key = keys[-1]

        # 如果value不是字符串，直接赋值
        if not isinstance(value, str):
            cur[last_key] = value
        # 如果value为空字符串, 恢复之前备份的值
        elif value == '':
            cur2 = self._backup_data
            for key in keys[:-1]:
                cur2 = cur2[key]
            cur[last_key]=cur2[last_key]

        # 如果以 '+' 或 '-' 开头，进行加减操作
        elif (value[0] == '+' or value[0] == '-') and value[1:].isdigit():
            cur2 = self._backup_data
            for key in keys[:-1]:
                cur2 = cur2[key]
            cur[last_key] = cur2[last_key] + int(value)
        # 如果是数字字符串，则直接赋值
        elif value.isdigit():
            cur[last_key] = int(value)
        else:
            print(keys,value)
        self._check_lv()


    def set_offset(self,value):
        self._offset=value
    def set_job(self,job):
        self._job=job


    def __call__(self)->dict[str:list]:
        """
        列表构成
        第一项固定为图外Buff,
        第二项固定为图内buff,
        skill_form里的项目,
        固定为一觉,
        固定为二觉,
        固定为总和,
        固定为总和,
        :return: [
            {
            'attack': 99999,# 三攻 '-'为不存在
            'intellect': 99999,# 力智 '-'为不存在
            'multiplier':99.99 # 对应倍率
                    },
            ...
        ]

        """
        res=self._get_job_buff()
        return {'result':res,'diff':self._diff(res)}








