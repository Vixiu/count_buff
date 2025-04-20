from dataclasses import dataclass
from typing import Callable, Union, Optional


@dataclass
class Skill:
    name: str
    lv: int
    icon: str # ":/png/ico.png"
    def __lt__(self, other):
        return self.lv < other.lv
@dataclass
class TY1(Skill):
    intellect:tuple[int, ...]
    xs:int
    xyz:tuple[int,int,float]

    @property
    def max_lv(self)->int:
        return len(self.intellect)
@dataclass
class TY3(Skill):
    bind1: float
    bind2: float
    growth: float

@dataclass
class Buff(TY1):
    attack:tuple[int, ...]
    @property
    def max_lv(self)->int:
        return min(len(self.attack),len(self.intellect))
@dataclass
class SkillFrom(Skill):
    multiplier: float
    show: tuple[bool, bool, bool]  # 是否显示(三攻,力智,倍率)


@dataclass
class PassiveSkill(Skill):
    data:tuple[int, ...]
    out_map:bool
    @property
    def max_lv(self) -> int:
        return len(self.data)

@dataclass
class PassiveSkillInf(Skill):
    out_map:bool
    max_lv:int
    _fnc: Callable[[int], int]
    @property
    def data(self):
        return self

    def __getitem__(self, index:int)->int:
        return self._fnc(index)

@dataclass
class TotalBuff:
    icon: str
    name: str
    skill_from:int #skill_from对应索引
    is_ty:bool #  True计算一觉,False计算三觉

@dataclass
class Job:
    id:str
    name:str
    buff:Buff
    ty1:TY1
    ty3:TY3
    increase:float
    attribute:str
    skill_form:tuple[SkillFrom, ...]
    passive_skill:tuple[Union[PassiveSkill, PassiveSkillInf], ...]
    total_buff:tuple[TotalBuff, ...]

    def get_passive_skill(self,lv)-> Optional[tuple[int, Union[PassiveSkill, PassiveSkillInf]]]:
        for i,item in enumerate(self.passive_skill):
            if item.lv==lv:
                return i,item
        return None