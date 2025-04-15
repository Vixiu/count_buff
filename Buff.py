import copy
from copy import deepcopy
from DataClass.InputData import InputData
from DataClass.Job import Job
from DataClass.Result import Result, Item, LvResult
from PyQt5.QtWidgets import QLineEdit


# 核心计算函数
def count_buff(buff_amount, intellect:int,xs: int,xyz:tuple[int,int,float],arm=1.08):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    """
    :param xyz:
    :param buff_amount: 增益量
    :param intellect: 四维
    :param xs: 系数
    :param arm: 奶爸cp站街Bug,后续修复会移除
    :return: callable
    """
    x, y, z = xyz
    def count(fixed:int, bfb: tuple[float,...], basic:int,cp_arms: bool) -> int:
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
        buff = (old_buff + new_buff) * (arm if cp_arms else 1)
        return round(buff)
    return count

def get_lv_value(tp: tuple, index: int):
    try:
        return tp[index - 1]
    except IndexError:
        return tp[0 if index < 1 else -1]


class UIData(InputData):
    def __init__(self,*args,**kwargs):
        self.__input_map: dict[str, QLineEdit] = {}
        super().__init__(*args, **kwargs)
        self.__backup = {k: v for k, v in vars(self).items() if k in self.__annotations__}
        self.__skill_map:set[str]={key for key in self.__backup.keys() if key.startswith('skill_')}
        self.__backup_map:set[str]={*self.__backup}-self.__skill_map

    def set_backup(self,is_skill=False):
        if is_skill:
           for key in self.__skill_map:
               self.__backup[key]=self.__dict__[key]
               self.__input_map[key].setText('')
               self.__input_map[key].setPlaceholderText(str(self.__dict__[key]))
        else:
            for key in self.__backup_map:
                self.__backup[key] = self.__dict__[key]
                self.__input_map[key].setText('')
                self.__input_map[key].setPlaceholderText(str(self.__dict__[key]))

    def bing_input(self,name:str,linedit,call_back):
        if not hasattr(self,name):
            raise AttributeError(f"变量{name} 不在类 {self} 中")
        def set_value(value):
            # setattr(self,name,value) 会调用__setattr__
            # 如果value不是字符串，直接赋值
            if not isinstance(value, str):
                self.__dict__[name]=value
            # 如果value为空字符串, 恢复之前备份的值
            elif value == '':
                self.__dict__[name]=self.__backup[name]
            # 如果以 '+' 或 '-' 开头，进行加减操作
            elif value[0] == '+' or value[0] == '-':
                if value[1:].isdigit():
                    self.__dict__[name] = self.__backup[name] + int(value)
                else:
                    try:
                        self.__dict__[name] = self.__backup[name] + float(value)
                    except ValueError:
                        pass
            # 如果是数字字符串，则直接赋值
            elif value.isdigit():
                self.__dict__[name] = int(value)
            else:
                try:
                    self.__dict__[name] = float(value)
                except ValueError:
                    pass
            print(name,'实际值:',value,"赋值:",self.__dict__[name])

            call_back()
        self.__input_map[name]=linedit
        linedit.textEdited.connect(set_value)

    def update(self,data:InputData):
        for k,v in data.__dict__.items():
            self.__dict__[k]=v
            if k in self.__input_map:
                self.__input_map[k].setText(str(v))
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in  self.__input_map:
            self.__input_map[key].setText(str(value))


class Buff:
    def __init__(self):
        self.__offset=0
        self.__data:InputData=None
        self.__job_data:Job=None
        self.__base_skill:list=[]
        self.__base_result:Result=None

    @property
    def data(self)->InputData:
        return self.__data


    def __count_multiplier(self, attack: int, intellect: int) -> Item:
        """
        倍率计算
        :param attack: 三攻
        :param intellect: 力智
        :return:
        """
        multiplier = round(
            (1 + attack / self.__data.c_attack) * (1 + intellect / (self.__data.c_intellect + 250)) * self.__job_data.increase
            , 2)
        return Item(attack=attack, intellect=intellect, multiplier=multiplier)

    def __count_buff(self, intellect, buff_amount, lv:int) -> Item:
        count = count_buff(
            buff_amount,
            intellect,
            self.__job_data.buff.xs,
            self.__job_data.buff.xyz,
            1.008 if self.__job_data.id == 'ba' else 1.08
        )
        return self.__count_multiplier(
            attack=count(
                self.__data.bxy_fixed_attack,
                self.__data.bxy_percentage_attack,
                get_lv_value(self.__job_data.buff.attack, lv),
                self.__data.is_cp
            ),
            intellect=count(
                self.__data.bxy_fixed_intellect,
                self.__data.bxy_percentage_intellect,
                get_lv_value(self.__job_data.buff.intellect, lv),
                False
            )

        )

    def __count_ty(self,intellect:int)->tuple[Item,Item]:
        """
        计算太阳
        :param intellect: 四维
        :return:
        """
        count = count_buff(
            self.__data.in_map_buff_amount,
            intellect,
            self.__job_data.ty1.xs,
            self.__job_data.ty1.xyz,
        )
        ty1=count(
            self.__data.bxy_fixed_ty,
            self.__data.bxy_percentage_ty,
            get_lv_value(self.__job_data.ty1.intellect, self.__data.ty_ty1_lv),
            False
                  )
        ty3=round(ty1 * (
                (self.__job_data.ty3.bind1 if self.__data.ty_is_ty1 else self.__job_data.ty3.bind2)
                + self.__data.ty_ty3_lv * self.__job_data.ty3.growth)
                        )
        return self.__count_multiplier(0,ty1),self.__count_multiplier(0,ty3),


    def init(self,data:InputData):
        self.__data=data

    def add_lv(self, min_lv:int, max_lv:int, count:int)->LvResult:
        result=LvResult()
        if min_lv <= self.__job_data.buff.lv <= max_lv:
            lv_max=self.__job_data.buff.max_lv
            new_lv=max(1, min(lv_max, self.__data.buff_lv_out_map + count))
            result.append(
                self.__job_data.buff.lv,
                f"{self.__job_data.buff.name}(图外)",
                self.__data.buff_lv_out_map,
                new_lv,
                '-',
                0
            )
            self.__data.buff_lv_out_map = new_lv
            # -
            new_lv = max(1, min(lv_max, self.__data.buff_lv_in_map + count))
            result.append(
                self.__job_data.buff.lv,
                f"{self.__job_data.buff.name}(图内)",
                self.__data.buff_lv_in_map,
                new_lv,
                '-',
                0
            )
            self.__data.buff_lv_in_map=new_lv
        if min_lv <= self.__job_data.ty1.lv <= max_lv:
            new_lv=max(1, min(self.__job_data.ty1.max_lv, self.__data.ty_ty1_lv + count))
            result.append(
                self.__job_data.ty1.lv,
                self.__job_data.ty1.name,
                self.__data.ty_ty1_lv,
                new_lv,
                 '-',
                0
            )
            self.__data.ty_ty1_lv = new_lv
        if min_lv <= self.__job_data.ty3.lv <= max_lv:
            new_lv = max(1, min(99999, self.__data.ty_ty3_lv + count))
            result.append(
                 self.__job_data.ty3.lv,
                 self.__job_data.ty3.name,
                 self.__data.ty_ty3_lv,
                 new_lv,
                  '-',
                0
            )
            self.__data.ty_ty3_lv = new_lv

        for i,skill in enumerate(self.__job_data.passive_skill):
            if min_lv <= skill.lv <= max_lv:
                old_lv=max(1, min(skill.max_lv, self.__data.passive_skill(i)))
                new_lv=max(1,min(skill.max_lv,old_lv+count))
                it=skill.data[new_lv-1]-skill.data[old_lv-1]
                result.append(
                     skill.lv,
                     skill.name,
                     old_lv,
                     new_lv,
                     str(it),
                     it
                )
                self.__data.set_passive_skill(i, new_lv)
        result.sort()
        return result
    def get_buff(self):
        # 计算地图内外四维偏移
        intellect_in, intellect_out = self.__offset, self.__offset
        for i,skill in enumerate(self.__job_data.passive_skill):
            it= get_lv_value(skill.data, self.__data.passive_skill(i)) - get_lv_value(skill.data, self.__base_skill[i])
            intellect_in +=it
            if skill.out_map:
                intellect_out+=it
        # 图外buff
        buff_out_map=self.__count_buff(
            intellect_out+self.__data.buff_intellect_out_map,
            self.__data.out_map_buff_amount,
            self.__data.buff_lv_out_map
        )
        # 图内buff
        buff_in_map=self.__count_buff(
            intellect_in+self.__data.buff_intellect_in_map,
            self.__data.in_map_buff_amount,
            self.__data.buff_lv_in_map
        )
        # 圣歌等
        skill_from=[
          self.__count_multiplier(
              attack=round(buff_in_map.attack*item.multiplier),
              intellect=round(buff_in_map.intellect*item.multiplier)
          )
            for item in self.__job_data.skill_form
        ]
        # 觉醒
        ty1,ty3=self.__count_ty(intellect_in + self.__data.ty_intellect)

        # 总数据
        total_buff=[]
        for item in self.__job_data.total_buff:
            attack,intellect=skill_from[item.skill_from].attack,skill_from[item.skill_from].intellect
            intellect +=  ty1.intellect if item.is_ty else ty3.intellect
            total_buff.append(self.__count_multiplier(attack, intellect))
        return Result(
            buff_in_map=buff_in_map,
            buff_out_map=buff_out_map,
            skill_from=skill_from,
            ty1=ty1,
            ty3=ty3,
            total=total_buff
        )

    def set_base(self):
        # - 将快捷计算里的四维加到data里
        self.__data.buff_intellect_out_map+=self.__offset
        self.__data.buff_intellect_in_map += self.__offset
        self.__data.ty_intellect += self.__offset
        self.__offset = 0
        # skill里的数据不会备份
        self.__data.set_backup()
        self.__base_result=self.get_buff()

    def set_skill_base(self):
        self.__base_skill=[self.__data.passive_skill(i) for i,_ in enumerate(self.__job_data.passive_skill)]
        self.__data.set_backup(True)
        self.__base_result=self.get_buff()

    def update(self,data:InputData):
        self.__data.update(data)
        self.__offset=0

    def set_offset(self,value:int):
        self.__offset=value

    def set_job_data(self,job:Job):
        self.__job_data=job

    def __call__(self)->tuple[Result,Result]:
        res= self.get_buff()
        return res,res-self.__base_result








