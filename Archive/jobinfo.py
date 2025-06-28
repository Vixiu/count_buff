from requests import get
#https://www.dfoneople.com/developers xxxx
#https://developers.neople.co.kr/main

skid='68062215e75d92575958873ac8ede31a'
tr=True
class GetSkillData:
    def __init__(self):
        self.apikey='6l6enit0JbyDGQ4GXSEh8GA2zALPEwJh'
        self.job={
            '奶萝': {
                'jobId': '3909d0b188e9c95311399f776e331da5',
                'jobGrowId': '92da05ec93fb43406e193ffb9a2a629b',
                'skill': {
                    '8d8981a94b8bdd4e3ffad5bc05042080': 'lv15人偶操纵者',
                    '0dbdeaf846356f8b9380f8fbb8e97377': 'lv50少女的爱',
                    'de20372767d014d62dc7361ac686834e': 'lv75冥月绽放',
                    '2575e479271da5c46990ab0bb88dd677': 'lv95不祥的微笑',
                }
            },
            '奶妈': {
                'jobId': '0c1b401bb09241570d364420b3ba3fd7',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
                'skill': {
                    '1': '勇气祝福',
                    '78bd107acd474518b606be1e4fd38239': 'lv15启示:颂歌',
                    '1dad88963abdc96b091fcab185a8820d': 'lv50虔诚信念',
                    'dbf8b30c7057032af0d68fcfa289fdae': 'lv75圣天使之光',
                    '5cac3411ccef1af333953e0ded5e942d': 'lv95大天使庇护',
                }
            },
            '奶枪': {
                'jobId': '944b9aab492c15a8474f96947ceeb9e4',
                'jobGrowId': '92da05ec93fb43406e193ffb9a2a629b',
                'skill': {
                    'e73e980e87591bc98940afb1ac0fe522': '军械强化',
                    '6235960237fdb1b77f2c82b33614dcf4': 'lv15战场信息',
                    '7ccc03c65d676c4d8a7e6a1821409ad0': 'lv25装甲强化',
                    'a8574a8efa365e8e46e805a6e1d7bfef': 'lv50作战应对',
                    'a354f4930334e70b0275f5d92668ce3d': 'lv75限制解除',
                    '5fed75723a5d5d373c9f54fba1c7dc06': 'lv95临战编程',
                },
            },
            '奶爸': {
                'jobId': 'f6a4ad30555b99b499c07835f87ce522',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
                   'skill': {
                    '2c9d9a36c8401bddff6cdb80fab8dc24': 'lv15守护恩赐',
                    '3d8f3d438405d79f8d3ed68072674d1e': 'lv25守护徽章',
                    '4f2e001e9a19eb7bae50ad1840dfb329': 'lv50信念光环',
                    'c4a5b868f1e8e60cd1867a2cfab4a242': 'lv75神圣之光',
                    '': 'lv95神之代行者',
                },
            },
            '奶弓': {
                'jobId': 'b9cb48777665de22c006fabaf9a560b3',
                'jobGrowId': '37495b941da3b1661bc900e68ef3b2c6',
                'skill': {
                    '0ed3148658fe37b3336ccb718dc0fdb0': 'lv15多彩感性',
                    'e49e57b2e8fbeceb0a2c56a0c63fe6c5': 'lv25主角登场',
                    'de3fea2d65c597f4d55c70a02b97fc79': 'lv50明星气场',
                    'faf9cd66281078b51be2ee0b0f6c5530': 'lv75崭新曲风',
                    '68062215e75d92575958873ac8ede31a': 'lv95和茉霓之歌',
                },
            },

}
        self.__translate={
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '불길한 눈웃음': '不祥的微笑',
            '어둠에 피는 장미': '冥月绽放',
            '소악마': '少女的爱',
            '퍼페티어': '人偶操纵者',
            '하드코딩': '临战编程',
            "대상": "目标",
            "크리티컬": "暴击",
            "확률": "概率",
            "피해": "伤害",
            "감소": "减少",
            "강화": "强化",
            "보호막": "护盾",
            '대응체계': '作战应对',
            "패러메딕": "医疗兵",
            "활용시": "使用时",
            "방어": "防御",
            '장갑강화': '装甲强化',
            "적중률": "命中率",
            "파티원": "小队成员",
            "전용": "专用",
            "효과": "效果",
            '마법': '魔法',
            '물리':'物理',
            '량':'量',
            '무기강화':'军械强化',
            'passive':'被动',
            'active':'主动',
            '계시':'启示',
            '아리아': '颂歌',
            '신실한 열정':'虔诚信念',
            '라파엘의 축복':'圣天使之光',
            '루클렌티스 엔젤':'大天使庇护',
            'apius::': '系统·',
            '전장정보()':'战场信息',
            '지능':'智力',
            '힘': '力量',
            '증가': '增加',
            "체력": "体力",
            "정신력": "精神",
            "속도": "速度",
            "공격": "攻击",
            "이동": "移动",
            "버프": "增益效果",
            "지속": "持续",
            "시간": "时间",
            "기본": "普通",
            "스킬": "技能",
            "범위": "范围",
            "정보": "信息",
            "오라": "光环",
            "력": "力",
            "율": "率",
            "초": "秒",
            "및 ": "和",

            "누적": "累计",
            "최대량": "最大量",
            "스택": "层数",

            "증가량": "增加量",
            "속성": "属性",
            "피해량": "伤害量",
            "증가율": "增加率",

            "지속시간": "持续时间",
            "최대": "最大",
            "중첩": "重叠",
            "수": "次数",
            "회": "次",
            "독립": "独立",
            "공격력": "攻击力",
            "쿨타임": "冷却时间",
            "감소량": "减少量",
            "소모시": "消耗时",
            "레이저": "激光",
            "사용시": "使用时",
            "추가": "额外",
            "폭격": "轰炸",
            "횟수": "次数",
            "전직":'转职',
            "계열": '系列',
            # 代码/技能名可直接照搬，按需自行补充：
            "apius::무기강화": "Apius：武器强化",
            "override()": "覆盖()",
            "squad::보호모듈(완충)": "Squad：保护模块（缓冲）",
            "squad::보호모듈(정화)": "Squad：保护模块（净化）",
            "squad::기동강화": "Squad：机动强化",
            "squad::무기강화()": "Squad：武器强化()",
            "squad::보호모듈(제세동)": "Squad：保护模块（除颤）"
          
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
    def get_skills(cls,name:str,skill_id:list[str]=None)->list:
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

    @classmethod
    def get_skill(cls,name,skill_id,translate=True):
        instance = cls()
        if name not in instance.job:
            raise ValueError(f'名称错误:{name},({instance.job.keys()})')

        res=get(f"https://api.neople.co.kr/df/skills/{instance.job[name]['jobId']}/{skill_id}?apikey={instance.apikey}"
                ,proxies={"http": None, "https": None})
        try:
            res=res.json()
            levelInfo=res['levelInfo']
            dt = {}
            for item in levelInfo['rows']:
                for k, v in item['optionValue'].items():
                    if k in dt:
                        dt[k].append(v)
                    else:
                        dt[k] = [v]
            name=res['name']
            if translate:
                for old, new in instance.__translate.items():
                    name = name.replace(old, new)
            print(f"名字:{name}")

            print(f"类型:{instance.__translate.get(res['type'],res['type'])}")
            print(f"描述:{instance.__translate.get(res['desc'],res['desc'])}".replace('\n',''))
            print('-------------------------------')
            optionDesc=levelInfo['optionDesc']
            if translate:
                for old, new in instance.__translate.items():
                    optionDesc = optionDesc.replace(old, new)
            print(optionDesc)
            print('-------------------------------')
            for k, v in dt.items():
                print(k, '=', tuple(v))
            print('-------------------------------')

        except:
            print(res)

        return 'end'
print(GetSkillData.get_skill('奶弓',skid,translate=tr))
#print(GetSkillData.get_skill_list('奶弓'))
