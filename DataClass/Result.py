from dataclasses import dataclass
from typing import Generator
@dataclass
class Lv:
    lv: int
    name: str
    old_lv: int
    new_lv: int
    info:str
    attribute: int
    def __lt__(self, other):
        return self.lv< other.lv

class LvResult:
    def __init__(self):
        self.__list=[]
    def append(self,lv,name,old_lv,new_lv,info,attribute):
        self.__list.append(
            Lv(lv, name, old_lv, new_lv, info,attribute)
        )
    def sort(self):
        self.__list.sort()

    def __iter__(self)->Generator[Lv,None,None]:
        yield from self.__list
@dataclass
class Item:
    attack: int
    intellect: int
    multiplier: float
    def __sub__(self, other:"Item")->"Item":
        return Item(
            self.attack - other.attack,
            self.intellect-other.intellect,
            round(self.multiplier-other.multiplier,2)
        )
@dataclass
class Result:
    buff_in_map:Item
    buff_out_map:Item
    skill_from:list[Item]
    ty1:Item
    ty3:Item
    total:list[Item]
    def __iter__(self)->Generator[Item, None, None]:
        """
        固定顺序
        :return:
        """
        yield self.buff_out_map
        yield self.buff_in_map
        yield from self.skill_from
        yield self.ty1
        yield self.ty3
        yield from self.total

    def __sub__(self, other:"Result")->"Result":
       return Result(
            buff_in_map=self.buff_in_map - other.buff_in_map,
            buff_out_map=self.buff_out_map - other.buff_out_map,
            skill_from=[a - b for a, b in zip(self.skill_from, other.skill_from)],
            ty1=self.ty1 - other.ty1,
            ty3=self.ty3 - other.ty3,
            total=[a - b for a, b in zip(self.total, other.total)],
        )