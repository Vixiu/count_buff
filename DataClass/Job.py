from dataclasses import dataclass, field
from typing import Callable, Union, Optional
from PyQt5.QtGui import QIcon, QPixmap


@dataclass
class Skill:
    name: str
    lv: int
    img: QPixmap = field(init=False, repr=True, compare=False)
    def __lt__(self, other):
        return self.lv < other.lv

@dataclass
class TY1(Skill):
    intellect:tuple[int, ...]=(43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567,608, 651, 696, 741, 789, 838, 888, 939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668)
    xs:int=750
    xyz:tuple[int,int,float]=(5250, 5000, 0.000025)
    lv: int = 50
    @property
    def max_lv(self)->int:
        return len(self.intellect)

    def __getitem__(self, item:int)->int:
        return self.intellect[max(0, min(item-1, len(self.intellect)-1))]

@dataclass
class TY3(Skill):
    lv :int=100
    bind1: float=1.08
    bind2: float=1.23
    growth: float=0.01


@dataclass
class Buff:
    name: str
    intellect: tuple[int, ...]
    attack: tuple[int, ...]
    lv:int=35
    xs:int=665
    xyz:tuple[int,int,float]=(4350, 3500, 3.78880649805069e-05)
    img: QPixmap = field(init=False, repr=True, compare=False)
    @property
    def max_lv(self)->int:
        return min(len(self.attack),len(self.intellect))

    def get_attack(self,index:int):
        return self.attack[max(0, min(index-1, len(self.attack)-1))]

    def get_intellect(self,index:int):
        return self.intellect[max(0, min(index-1, len(self.intellect)-1))]

    def __lt__(self, other):
        return self.lv < other.lv

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
    def __getitem__(self, item:int)->int:
        return self.data[max(0, min(item-1, len(self.data)-1))]

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
class TotalBuff(Skill):
    skill_from:int  #skill_from对应索引
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
    img: QPixmap = field(init=False, repr=True, compare=False)

    def __post_init__(self):
        self.img = QPixmap(f":/{self.id}/av.png")
        self.buff.img=QPixmap(f":/{self.id}/buff.png")
        self.ty1.img=QPixmap(f":/{self.id}/ty1.png")
        self.ty3.img=QPixmap(f":/{self.id}/ty3.png")
        skid=1
        for item in self.skill_form:
            item.img = QPixmap(f":/{self.id}/sk{skid}.png")
            skid+=1

        for item in self.total_buff:
            item.img = QPixmap(f":/{self.id}/sk_{skid}.png")
            skid+=1

        for item in self.passive_skill:
            item.img = QPixmap(f":/{self.id}/pk{item.lv}.png")

    def get_passive_skill(self,lv)-> Optional[tuple[int, Union[PassiveSkill, PassiveSkillInf]]]:
        for i,item in enumerate(self.passive_skill):
            if item.lv==lv:
                return i,item
        return None