from copy import deepcopy
from dataclasses import dataclass,asdict
import json
from os import path, makedirs
from DataClass.InputData import InputData
from Config import JobID, FilePath


@dataclass
class Data:
    name:str
    data:InputData

class SaveData:
    def __init__(self):
        self.__record:dict[str,int]={job:0 for job in JobID}
        self.__last_job='ma'
        self.__first_launch=False
        self.__config:dict[str,list[Data]]={n:[] for n in JobID}
        self.__property_map:dict[str,int]={k:len(v) for k,v in self.__config.items()}
        self.__load_config()
    @property
    def last_record(self):
        return self.__record[self.__last_job]
    @property
    def last_job(self):
        return self.__last_job
    @property
    def is_first_launch(self)->bool:
        return self.__first_launch
    def set_job(self,name):
        self.__last_job=name

    def __load_config(self):
        try:
            with open(FilePath,'r') as f:
                data=json.load(f)
            for k, v in data['data'].items():
                for item in v:
                    self.__config[k].append(
                        Data(item['name'],InputData(**item['data']))
                    )
            self.__record=data['record']
            self.__last_job=data['last_job']
        except :
            self.__first_launch=True

    def __save_config(self):
        if not path.exists(path.dirname(FilePath)):
            makedirs(path.dirname(FilePath))
        with open(FilePath, 'w+') as f:

            json.dump({
                'data':{k:[asdict(data) for data in v[self.__property_map[k]:]] for k,v in self.__config.items()},
                'record':self.__record,
                'last_job':self.__last_job,
            }, f,indent=4)


    def set_config(self, data:InputData, job:str=None, index:int=None)->tuple[bool,str]:
        if job is None:
            job= self.__last_job
        if index is None:
            index=self.__record[job]

        if  index >=self.__property_map[job]:
            self.__config[job][index].data = deepcopy(data)
            self.__save_config()
            return True, f'{self.__config[job][index].name} 已保存'
        else:
            return False, '默认配置不可修改,请另存为!'

    def add_config(self,name,data:InputData):
        self.__config[self.__last_job].append(Data(name,deepcopy(data)))
        self.__record[self.__last_job]=len(self.__config[self.__last_job])-1
        self.__save_config()

    def add_default_config(self,job_name:str,data:Data):
        if job_name not in JobID:
            raise ValueError(f'{job_name}不在config中:{JobID}')
        self.__config[job_name].insert(self.__property_map[job_name],data)
        self.__property_map[job_name] += 1

    def del_item(self, job:str=None, index:int=None):
        if job is None:
            job = self.__last_job
        if index is None:
            index = self.__record[job]
        if index >= self.__property_map[job]:
            self.__config[job].pop(index)
            self.__record[job] = max(0, self.__record[job] - 1)
            self.__save_config()
            return True, ''
        else:
            return False, '默认配置不可删除'

    def rename(self,name:str,job_name:str=None,index:int=None):
        pass
    def get_data(self, job=None, index=None)->InputData:
        if job is None:
            job = self.__last_job
        if index is None:
            index = self.__record[job]
        else:
            self.__record[job]=index
        return self.__config[job][index].data

    def get_names(self,job_name:str="")->list[str]:
        job_name = job_name or self.__last_job
        return  [item.name for item in self.__config[job_name]]
    def __call__(self):
        self.__save_config()


save=SaveData()