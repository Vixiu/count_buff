from requests import get

class GetSkillData:
    def __init__(self):
        self.apikey='6l6enit0JbyDGQ4GXSEh8GA2zALPEwJh'
        self.job={
            '奶枪':{
                'jobId':'944b9aab492c15a8474f96947ceeb9e4',
                'jobGrowId':'92da05ec93fb43406e193ffb9a2a629b',
                'skill':{
                    '7ccc03c65d676c4d8a7e6a1821409ad0':''

                },
            },
            '奶爸': {
                'jobId': 'f6a4ad30555b99b499c07835f87ce522',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
                'skill':{

                }
            },
            '奶妈': {
                'jobId': '0c1b401bb09241570d364420b3ba3fd7',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
                'skill': {
                    '1': '勇气祝福',
                    '2': '启示:颂歌',
                    '3': '虔诚信念',
                    '4': '圣天使之光',
                    '5': '大天使庇护',
                }
            },
            '奶弓': {
                'jobId': 'b9cb48777665de22c006fabaf9a560b3',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
            },
}
        self.__translate={
            'type':'类型',
            'passive':'被动',
            'active':'主动',
        }
    def __get_skills_list(self,job_id, job_grow_id):
        return get(f'https://api.neople.co.kr/df/skills/{job_id}?jobGrowId={job_grow_id}&apikey={self.apikey}').json()['skills']


    def __get(self,job_id, job_grow_id):
        skills=self.__get_skills_list(job_id, job_grow_id)
        skill_ids = [item['skillId'] for item in skills]
        multi_skill = []
        for i in range(0, len(skill_ids), 10):
            _ = get(
                f"https://api.neople.co.kr/df/multi/skills/{job_id}?skillIds={','.join(skill_ids[i:i + 10])}&apikey={self.apikey}").json()
            multi_skill += _['rows']
        return multi_skill

    @classmethod
    def get_skill(cls,name:str,skill_id:list[str]=None)->list:
        instance = cls()
        if name not in instance.job:
            raise ValueError(f'名称错误:{name},({instance.job.keys()})')
        if skill_id is None:
            return instance.__get(instance.job[name]['jobId'],instance.job[name]['jobGrowId'])
        else:
            pass

    @classmethod
    def get_skill_list(cls,name:str):
        instance = cls()
        if name not in instance.job:
            raise ValueError(f'名称错误:{name},({instance.job.keys()})')
        return instance.__get_skills_list(instance.job[name]['jobId'],instance.job[name]['jobGrowId'])
print(GetSkillData.get_skill_list('奶枪'))
