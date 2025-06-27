from dataclasses import dataclass,field
from typing import Generator, Any, Iterator


@dataclass
class InputData:
    c_attack: int = 3350
    c_intellect: int = 24500
    # buff属性
    buff_intellect_in_map: int = 0
    buff_lv_in_map: int = 37
    buff_intellect_out_map: int = 0
    buff_lv_out_map: int = 37
    # 增益量
    buff_amount_in_map: int = 0
    buff_amount_out_map: int = 0
    buff_amount_amp: float = 0.0
    # 避邪玉
    bxy_amp: float = 0.0
    bxy_fixed_attack: int = 0
    bxy_fixed_intellect: int = 0
    bxy_fixed_ty: int = 0
    bxy_percentage_attack: tuple[float, ...] = field(default_factory=lambda: (0.0,))
    bxy_percentage_intellect: tuple[float, ...] = field(default_factory=lambda: (0.0,))
    bxy_percentage_ty: tuple[float, ...] = field(default_factory=lambda: (0.0, 0.0))
    # 觉醒
    ty_ty1_lv: int = 41
    ty_intellect: int = 0
    ty_ty3_lv: int = 7
    ty_is_ty1: bool = True
    # 技能
    passive_skill_0: int = 1
    passive_skill_1: int = 1
    passive_skill_2: int = 1
    passive_skill_3: int = 1
    passive_skill_4: int = 1
    passive_skill_5: int = 1
    passive_skill_6: int = 1
    @property
    def in_map_buff_amount(self) -> float:
        return (
                (self.buff_amount_in_map + self.buff_amount_out_map) *
                (1 + self.buff_amount_amp / 100 + self.bxy_amp / 100)
        )
    @property
    def out_map_buff_amount(self) -> float:
        return self.buff_amount_out_map * (1 + self.buff_amount_amp / 100)

    @property
    def passive_skill(self):
        return [self.__dict__[key] for key in self.__dict__ if key.startswith('passive_skill_')]
    def set_passive_skill_lv(self,index,lv):
        self.__dict__[f'passive_skill_{index}']=lv

    def __setitem__(self, key, value):
        if key not in self.__dict__:  # 只允许特定键
            raise KeyError(f"键 '{key}' 不在InputData中!")
        self.__dict__[key]=value

    def __iter__(self)-> Iterator[tuple[str, Any]]:
        return iter(self.__dict__.items())



'''
@dataclass
class BuffAmount:
    in_map:int=0
    out_map:int=0
    amp:float=0.0

@dataclass
class BXY:
    amp: float=0.0
    fixed_attack: int=0
    fixed_intellect: int=0
    fixed_ty: int=0
    percentage_attack: list[float, ...]=field(default_factory=lambda :[0.0])
    percentage_intellect: list[float, ...]=field(default_factory=lambda :[0.0,0.0])
    percentage_ty: list[float, ...]=field(default_factory=lambda :[0.0,0.0,0.0])

@dataclass
class Buff:


@dataclass
class  TY:
    ty1_lv: int=1
    intellect:int=0
    ty3_lv: int=1
    is_ty1:bool=True

@dataclass
class Skill:
    k1:int=1
    k2:int=1
    k3:int=1
    ...

    def __getitem__(self, item: int):
        return self.__dict__[f'k{item + 1}']
'''


