from DataClass.InputData import InputData
from DataClass.Job import Job, PassiveSkill
from DataClass.Result import Result, Item, LvResult
# 核心计算函数
def count_buff(buff_amount, intellect:int,xs: int,xyz:tuple[int,int,float]):  # 这个arm参数仅用于临时修正奶爸的站街武器BUG
    """
    :param xyz:
    :param buff_amount: 增益量
    :param intellect: 四维
    :param xs: 系数
    :return: callable
    """
    x, y, z = xyz
    def count(fixed:int, bfb: tuple[float,...], basic:int) -> int:
        """
        :param fixed: 固定加成
        :param bfb: 百分比加成
        :param basic: 基础数值
        :return:
        """
        old_buff = ((basic + fixed) * ((intellect / xs) + 1))
        for n in bfb:
            old_buff *= (1 + n / 100)
        new_buff = basic * ((intellect + x) / xs + 1) * (buff_amount + y) * z if buff_amount != 0 else 0
        return round(old_buff + new_buff)
    return count


class Buff:
    def __init__(self,job:Job):
        self.__data:InputData=InputData()
        self.__job:Job=job
        self.__offset_intellect:int=0
        self.__base_result=Result(
            buff_in_map=Item(0,0,0),
            buff_out_map=Item(0,0,0),
            skill_from=[Item(0,0,0)],
            ty1=Item(0,0,0),
            ty3=Item(0,0,0),
            total=[Item(0,0,0)]
        )
        self.__base_passive_skill=self.__data.passive_skill

    def __count_multiplier(self, attack: int, intellect: int) -> Item:
        """
        倍率计算
        :param attack: 三攻
        :param intellect: 力智
        :return:
        """
        multiplier = round(
            (1 + attack / self.__data.c_attack) * (
                        1 + intellect / (self.__data.c_intellect + 250)) * self.__job.increase
            , 2)
        return Item(attack=attack, intellect=intellect, multiplier=multiplier)

    def __count_buff(self, intellect, buff_amount, lv: int) -> Item:
        count = count_buff(
            buff_amount,
            intellect,
            self.__job.buff.xs,
            self.__job.buff.xyz,
        )
        return self.__count_multiplier(
            attack=count(
                self.__data.bxy_fixed_attack,
                self.__data.bxy_percentage_attack,
                self.__job.buff.get_attack(lv)

            ),
            intellect=count(
                self.__data.bxy_fixed_intellect,
                self.__data.bxy_percentage_intellect,
                self.__job.buff.get_intellect(lv)
            )

        )

    def __count_ty(self, intellect: int) -> tuple[Item, Item]:
        """
        计算太阳
        :param intellect: 四维
        :return:
        """
        count = count_buff(
            self.__data.in_map_buff_amount,
            intellect,
            self.__job.ty1.xs,
            self.__job.ty1.xyz,
        )
        ty1 = count(
            self.__data.bxy_fixed_ty,
            self.__data.bxy_percentage_ty,
            self.__job.ty1[self.__data.ty_ty1_lv]
        )
        ty3 = round(ty1 * (
                (self.__job.ty3.bind1 if self.__data.ty_is_ty1 else self.__job.ty3.bind2)
                + self.__data.ty_ty3_lv * self.__job.ty3.growth)
                    )
        return self.__count_multiplier(0, ty1), self.__count_multiplier(0, ty3),


    @property
    def data(self)->InputData:
        return self.__data

    def set_offset_intellect(self,value:int):
        self.__offset_intellect=value

    def init_data(self,data:InputData):
        self.__data=data
        self.__offset_intellect=0

    def init_job(self,job:Job,data:InputData):
        self.__job=job
        self.init_data(data)
        self.set_base_skill()
        self.set_baseline()

    def set_baseline(self):
        self.__data.buff_intellect_out_map += self.__offset_intellect
        self.__data.buff_intellect_in_map += self.__offset_intellect
        self.__data.ty_intellect += self.__offset_intellect
        self.__offset_intellect = 0
        self.__base_result = self.calculate()


    def set_base_skill(self):
        self.__base_passive_skill=self.__data.passive_skill
        self.__base_result=self.calculate()

    def add_lv(self, min_lv: int, max_lv: int, count: int) -> LvResult:
        result = LvResult()
        if min_lv <= self.__job.buff.lv <= max_lv:
            lv_max = self.__job.buff.max_lv
            new_lv = max(1, min(lv_max, self.__data.buff_lv_out_map + count))
            result.append(
                self.__job.buff.lv,
                f"{self.__job.buff.name}(图外)",
                self.__data.buff_lv_out_map,
                new_lv,
                '-',
                0
            )
            self.__data.buff_lv_out_map = new_lv
            # -
            new_lv = max(1, min(lv_max, self.__data.buff_lv_in_map + count))
            result.append(
                self.__job.buff.lv,
                f"{self.__job.buff.name}(图内)",
                self.__data.buff_lv_in_map,
                new_lv,
                '-',
                0
            )
            self.__data.buff_lv_in_map = new_lv
        if min_lv <= self.__job.ty1.lv <= max_lv:
            new_lv = max(1, min(self.__job.ty1.max_lv, self.__data.ty_ty1_lv + count))
            result.append(
                self.__job.ty1.lv,
                self.__job.ty1.name,
                self.__data.ty_ty1_lv,
                new_lv,
                '-',
                0
            )
            self.__data.ty_ty1_lv = new_lv
        if min_lv <= self.__job.ty3.lv <= max_lv:
            new_lv = max(1, min(99999, self.__data.ty_ty3_lv + count))
            result.append(
                self.__job.ty3.lv,
                self.__job.ty3.name,
                self.__data.ty_ty3_lv,
                new_lv,
                '-',
                0
            )
            self.__data.ty_ty3_lv = new_lv
        passive_skill=self.__data.passive_skill
        for i, skill in enumerate(self.__job.passive_skill):
            if min_lv <= skill.lv <= max_lv:
                old_lv = max(1, min(skill.max_lv,passive_skill[i]))
                new_lv = max(1, min(skill.max_lv, old_lv + count))
                it = skill.data[new_lv - 1] - skill.data[old_lv - 1]
                result.append(
                    skill.lv,
                    skill.name,
                    old_lv,
                    new_lv,
                    str(it),
                    it
                )
                self.__data.set_passive_skill_lv(i, new_lv)
        result.sort()
        return result

    def passive_skill(self,lv)->tuple[PassiveSkill,int]:
        index,skill=self.__job.get_passive_skill(lv)
        return skill,skill[self.__data.passive_skill[index]]

    def calculate(self):
        intellect_in, intellect_out = self.__offset_intellect, self.__offset_intellect
        passive_skill=self.__data.passive_skill
        for i, skill in enumerate(self.__job.passive_skill):
            it = skill[passive_skill[i]]-skill[self.__base_passive_skill[i]]
            intellect_in += it
            if skill.out_map:
                intellect_out += it

        # 图外buff
        buff_out_map = self.__count_buff(
            intellect_out + self.__data.buff_intellect_out_map,
            self.__data.out_map_buff_amount,
            self.__data.buff_lv_out_map
        )
        # 图内buff
        buff_in_map = self.__count_buff(
            intellect_in + self.__data.buff_intellect_in_map,
            self.__data.in_map_buff_amount,
            self.__data.buff_lv_in_map
        )
        # 圣歌等
        skill_from = [
            self.__count_multiplier(
                attack=round(buff_in_map.attack * item.multiplier),
                intellect=round(buff_in_map.intellect * item.multiplier)
            )
            for item in self.__job.skill_form
        ]
        # 觉醒
        ty1, ty3 = self.__count_ty(intellect_in + self.__data.ty_intellect)

        # 总数据
        total_buff = []
        for item in self.__job.total_buff:
            attack, intellect = skill_from[item.skill_from].attack, skill_from[item.skill_from].intellect
            intellect += ty1.intellect if item.is_ty else ty3.intellect
            total_buff.append(self.__count_multiplier(attack, intellect))
        return Result(
            buff_in_map=buff_in_map,
            buff_out_map=buff_out_map,
            skill_from=skill_from,
            ty1=ty1,
            ty3=ty3,
            total=total_buff
        )

    def __call__(self)->tuple[Result,Result]:
        res=self.calculate()
        return res,res-self.__base_result

    def __setitem__(self, key:str, value):
        self.__data[key]=value





