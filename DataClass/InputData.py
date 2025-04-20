from dataclasses import dataclass,field
@dataclass
class InputData:
    is_cp: bool = False
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
    skill_0: int = 1
    skill_1: int = 1
    skill_2: int = 1
    skill_3: int = 1
    skill_4: int = 1
    skill_5: int = 1
    skill_6: int = 1
    @property
    def in_map_buff_amount(self) -> float:
        return (
                (self.buff_amount_in_map + self.buff_amount_out_map) *
                (1 + self.buff_amount_amp / 100 + self.bxy_amp / 100)
        )
    @property
    def out_map_buff_amount(self) -> float:
        return self.buff_amount_out_map * (1 + self.buff_amount_amp / 100)

    def passive_skill(self, index)->int:
        return self.__dict__[f'skill_{index}']
    def set_passive_skill(self,index,value):
        setattr(self,f'skill_{index}',value)

    def set_backup(self,is_skill=False):...
    def update(self,data:"InputData"):
            self.__dict__.update(data.__dict__)

    def get_data(self):
        return self
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
