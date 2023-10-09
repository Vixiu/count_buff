import csv
import json
import requests

import asyncio

import json

import aiohttp
from tqdm import tqdm

WORD_DICT = {
    "全部": [
        {
            "name": "全服",
            "worldId": 255
        }
    ],
    "跨1区": [
        {
            "name": "跨1区",
            "worldId": "k1"
        },
        {
            "name": "广东1区",
            "worldId": 1
        },
        {
            "name": "广东2区",
            "worldId": 15
        },
        {
            "name": "广东3区",
            "worldId": 22
        },
        {
            "name": "广东4区",
            "worldId": 45
        },
        {
            "name": "广东5区",
            "worldId": 52
        },
        {
            "name": "广东6区",
            "worldId": 65
        },
        {
            "name": "广东7区",
            "worldId": 71
        },
        {
            "name": "广东8区",
            "worldId": 81
        },
        {
            "name": "广东9区",
            "worldId": 89
        },
        {
            "name": "广东10区",
            "worldId": 98
        },
        {
            "name": "广东11区",
            "worldId": 105
        },
        {
            "name": "广东12区",
            "worldId": 126
        },
        {
            "name": "广东13区",
            "worldId": 134
        },
        {
            "name": "广西1区",
            "worldId": 28
        },
        {
            "name": "广西2区",
            "worldId": 64
        },
        {
            "name": "广西3区",
            "worldId": 88
        },
        {
            "name": "广西5区",
            "worldId": 133
        },
        {
            "name": "广州1区",
            "worldId": 34
        }
    ],
    "跨2区": [
        {
            "name": "跨2区",
            "worldId": "k2"
        },
        {
            "name": "湖南1区",
            "worldId": 5
        },
        {
            "name": "湖南2区",
            "worldId": 25
        },
        {
            "name": "湖南3区",
            "worldId": 50
        },
        {
            "name": "湖南4区",
            "worldId": 66
        },
        {
            "name": "湖南5区",
            "worldId": 74
        },
        {
            "name": "湖南6区",
            "worldId": 85
        },
        {
            "name": "湖南7区",
            "worldId": 117
        },
        {
            "name": "湖北1区",
            "worldId": 9
        },
        {
            "name": "湖北2区",
            "worldId": 24
        },
        {
            "name": "湖北3区",
            "worldId": 48
        },
        {
            "name": "湖北4区",
            "worldId": 68
        },
        {
            "name": "湖北5区",
            "worldId": 76
        },
        {
            "name": "湖北6区",
            "worldId": 94
        },
        {
            "name": "湖北7区",
            "worldId": 115
        },
        {
            "name": "湖北8区",
            "worldId": 127
        }
    ],
    "跨3A区": [
        {
            "name": "跨3A区",
            "worldId": "k3A"
        },
        {
            "name": "四川1区",
            "worldId": 4
        },
        {
            "name": "四川2区",
            "worldId": 26
        },
        {
            "name": "四川3区",
            "worldId": 56
        },
        {
            "name": "四川4区",
            "worldId": 70
        },
        {
            "name": "四川5区",
            "worldId": 82
        },
        {
            "name": "四川6区",
            "worldId": 107
        },
        {
            "name": "西北1区",
            "worldId": 12
        },
        {
            "name": "西北2区",
            "worldId": 46
        },
        {
            "name": "新疆1区",
            "worldId": 123
        }
    ],
    "跨3B区": [
        {
            "name": "跨3B区",
            "worldId": "k3B"
        },
        {
            "name": "重庆1区",
            "worldId": 39
        },
        {
            "name": "重庆2区",
            "worldId": 73
        },
        {
            "name": "贵州1区",
            "worldId": 122
        },
        {
            "name": "陕西1区",
            "worldId": 33
        },
        {
            "name": "陕西2/3区",
            "worldId": 63
        },
        {
            "name": "西南1区",
            "worldId": 17
        },
        {
            "name": "西南2区",
            "worldId": 49
        },
        {
            "name": "西南3区",
            "worldId": 92
        },
        {
            "name": "云贵1区",
            "worldId": 124
        },
        {
            "name": "云南1区",
            "worldId": 120
        }
    ],
    "跨4区": [
        {
            "name": "跨4区",
            "worldId": "k4"
        },
        {
            "name": "安徽3区",
            "worldId": 104
        },
        {
            "name": "福建3/4区",
            "worldId": 80
        },
        {
            "name": "江苏5区",
            "worldId": 79
        },
        {
            "name": "江苏6区",
            "worldId": 90
        },
        {
            "name": "江苏8区",
            "worldId": 109
        },
        {
            "name": "江西3区",
            "worldId": 96
        },
        {
            "name": "上海4区",
            "worldId": 93
        },
        {
            "name": "浙江4区",
            "worldId": 84
        },
        {
            "name": "浙江6区",
            "worldId": 116
        },
        {
            "name": "浙江7区",
            "worldId": 129
        }
    ],
    "跨5区": [
        {
            "name": "跨5区",
            "worldId": "k5"
        },
        {
            "name": "安徽1区",
            "worldId": 30
        },
        {
            "name": "安徽2区",
            "worldId": 58
        },
        {
            "name": "福建1区",
            "worldId": 14
        },
        {
            "name": "福建2区",
            "worldId": 44
        },
        {
            "name": "江苏1区",
            "worldId": 7
        },
        {
            "name": "江苏2区",
            "worldId": 20
        },
        {
            "name": "江苏3区",
            "worldId": 41
        },
        {
            "name": "江苏4区",
            "worldId": 53
        },
        {
            "name": "江西1区",
            "worldId": 29
        },
        {
            "name": "江西2区",
            "worldId": 62
        },
        {
            "name": "上海1区",
            "worldId": 3
        },
        {
            "name": "上海2区",
            "worldId": 16
        },
        {
            "name": "上海3区",
            "worldId": 36
        },
        {
            "name": "浙江1区",
            "worldId": 11
        },
        {
            "name": "浙江2区",
            "worldId": 21
        },
        {
            "name": "浙江3区",
            "worldId": 55
        }
    ],
    "跨6区": [
        {
            "name": "跨6区",
            "worldId": "k6"
        },
        {
            "name": "北京1区",
            "worldId": 2
        },
        {
            "name": "北京2区",
            "worldId": 35
        },
        {
            "name": "东北1区",
            "worldId": 13
        },
        {
            "name": "东北2区",
            "worldId": 18
        },
        {
            "name": "东北3/7区",
            "worldId": 23
        },
        {
            "name": "华北1区",
            "worldId": 10
        },
        {
            "name": "华北2区",
            "worldId": 19
        },
        {
            "name": "华北3区",
            "worldId": 54
        },
        {
            "name": "河北1区",
            "worldId": 38
        },
        {
            "name": "河南1区",
            "worldId": 27
        },
        {
            "name": "河南2区",
            "worldId": 43
        },
        {
            "name": "黑龙江1区",
            "worldId": 40
        },
        {
            "name": "吉林1/2区",
            "worldId": 42
        },
        {
            "name": "辽宁1区",
            "worldId": 31
        },
        {
            "name": "山东1区",
            "worldId": 6
        },
        {
            "name": "山东2区",
            "worldId": 37
        },
        {
            "name": "山西1区",
            "worldId": 32
        }
    ],
    "跨7区": [
        {
            "name": "跨7区",
            "worldId": "k7"
        },
        {
            "name": "东北4区",
            "worldId": 83
        },
        {
            "name": "河北2区",
            "worldId": 67
        },
        {
            "name": "河北4区",
            "worldId": 118
        },
        {
            "name": "河北5区",
            "worldId": 132
        },
        {
            "name": "河南3区",
            "worldId": 57
        },
        {
            "name": "河南4区",
            "worldId": 69
        },
        {
            "name": "河南5区",
            "worldId": 77
        },
        {
            "name": "河南6区",
            "worldId": 103
        },
        {
            "name": "河南7区",
            "worldId": 135
        },
        {
            "name": "辽宁2区",
            "worldId": 47
        },
        {
            "name": "辽宁3区",
            "worldId": 61
        }
    ],
    "跨8区": [
        {
            "name": "跨8区",
            "worldId": "k8"
        },
        {
            "name": "北京3区",
            "worldId": 72
        },
        {
            "name": "华北4区",
            "worldId": 87
        },
        {
            "name": "黑龙江2区",
            "worldId": 51
        },
        {
            "name": "内蒙古1区",
            "worldId": 125
        },
        {
            "name": "山东3区",
            "worldId": 59
        },
        {
            "name": "山东4区",
            "worldId": 75
        },
        {
            "name": "山东5区",
            "worldId": 78
        },
        {
            "name": "山东6区",
            "worldId": 106
        },
        {
            "name": "山西2区",
            "worldId": 95
        },
        {
            "name": "天津1区",
            "worldId": 121
        }
    ]
}
HERO_LIST = [{'jobId': '16', 'transferId': '49', 'hero_name': '聆风·缪斯'},
             {'jobId': '16', 'transferId': '50', 'hero_name': '聆风·旅人'},
             {'jobId': '0', 'transferId': '49', 'hero_name': '极诣·剑魂'},
             {'jobId': '0', 'transferId': '50', 'hero_name': '极诣·鬼泣'},
             {'jobId': '0', 'transferId': '51', 'hero_name': '极诣·狂战士'},
             {'jobId': '0', 'transferId': '52', 'hero_name': '极诣·阿修罗'},
             {'jobId': '0', 'transferId': '53', 'hero_name': '极诣·剑影'},
             {'jobId': '11', 'transferId': '49', 'hero_name': '极诣·驭剑士'},
             {'jobId': '11', 'transferId': '50', 'hero_name': '极诣·暗殿骑士'},
             {'jobId': '11', 'transferId': '51', 'hero_name': '极诣·契魔者'},
             {'jobId': '11', 'transferId': '52', 'hero_name': '极诣·流浪武士'},
             {'jobId': '11', 'transferId': '53', 'hero_name': '极诣·刃影'},
             {'jobId': '7', 'transferId': '9', 'hero_name': '归元·气功师(男)'},
             {'jobId': '7', 'transferId': '0', 'hero_name': '归元·散打(男)'},
             {'jobId': '7', 'transferId': '1', 'hero_name': '归元·街霸(男)'},
             {'jobId': '7', 'transferId': '2', 'hero_name': '归元·柔道家(男)'},
             {'jobId': '1', 'transferId': '9', 'hero_name': '归元·气功师(女)'},
             {'jobId': '1', 'transferId': '0', 'hero_name': '归元·散打(女)'},
             {'jobId': '1', 'transferId': '2', 'hero_name': '归元·柔道家(女)'},
             {'jobId': '1', 'transferId': '1', 'hero_name': '归元·街霸(女)'},
             {'jobId': '2', 'transferId': '9', 'hero_name': '重霄·漫游枪手(男)'},
             {'jobId': '2', 'transferId': '0', 'hero_name': '重霄·枪炮师(男)'},
             {'jobId': '2', 'transferId': '1', 'hero_name': '重霄·机械师(男)'},
             {'jobId': '2', 'transferId': '2', 'hero_name': '重霄·弹药专家(男)'},
             {'jobId': '2', 'transferId': '3', 'hero_name': '重霄·合金战士'},
             {'jobId': '5', 'transferId': '9', 'hero_name': '重霄·漫游枪手(女)'},
             {'jobId': '5', 'transferId': '0', 'hero_name': '重霄·枪炮师(女)'},
             {'jobId': '5', 'transferId': '1', 'hero_name': '重霄·机械师(女)'},
             {'jobId': '5', 'transferId': '2', 'hero_name': '重霄·弹药专家(女)'},
             {'jobId': '8', 'transferId': '9', 'hero_name': '知源·元素爆破师'},
             {'jobId': '8', 'transferId': '0', 'hero_name': '知源·冰结师'},
             {'jobId': '8', 'transferId': '1', 'hero_name': '知源·猩红法师'},
             {'jobId': '8', 'transferId': '2', 'hero_name': '知源·逐风者'},
             {'jobId': '8', 'transferId': '3', 'hero_name': '知源·次元行者'},
             {'jobId': '3', 'transferId': '9', 'hero_name': '知源·元素师'},
             {'jobId': '3', 'transferId': '0', 'hero_name': '知源·召唤师'},
             {'jobId': '3', 'transferId': '1', 'hero_name': '知源·战斗法师'},
             {'jobId': '3', 'transferId': '2', 'hero_name': '知源·魔道学者'},
             {'jobId': '3', 'transferId': '3', 'hero_name': '知源·小魔女'},
             {'jobId': '4', 'transferId': '9', 'hero_name': '光启·光明骑士(男)'},
             {'jobId': '4', 'transferId': '0', 'hero_name': '光启·蓝拳使者'},
             {'jobId': '4', 'transferId': '1', 'hero_name': '光启·驱魔师'},
             {'jobId': '4', 'transferId': '2', 'hero_name': '光启·惩戒者'},
             {'jobId': '14', 'transferId': '49', 'hero_name': '光启·光明骑士(女)'},
             {'jobId': '14', 'transferId': '50', 'hero_name': '光启·正义审判者'},
             {'jobId': '14', 'transferId': '51', 'hero_name': '光启·驱魔师'},
             {'jobId': '14', 'transferId': '52', 'hero_name': '光启·除恶者'},
             {'jobId': '6', 'transferId': '9', 'hero_name': '隐夜·暗星'},
             {'jobId': '6', 'transferId': '0', 'hero_name': '隐夜·黑夜术士'},
             {'jobId': '6', 'transferId': '1', 'hero_name': '隐夜·忍者'},
             {'jobId': '6', 'transferId': '2', 'hero_name': '隐夜·影舞者'},
             {'jobId': '12', 'transferId': '52', 'hero_name': '皓曦·龙骑士'},
             {'jobId': '12', 'transferId': '49', 'hero_name': '皓曦·精灵骑士'},
             {'jobId': '12', 'transferId': '51', 'hero_name': '皓曦·帕拉丁'},
             {'jobId': '12', 'transferId': '50', 'hero_name': '皓曦·混沌魔灵'},
             {'jobId': '13', 'transferId': '49', 'hero_name': '千魂·征战者'},
             {'jobId': '13', 'transferId': '50', 'hero_name': '千魂·决战者'},
             {'jobId': '13', 'transferId': '51', 'hero_name': '千魂·狩猎者'},
             {'jobId': '13', 'transferId': '52', 'hero_name': '千魂·暗枪士'},
             {'jobId': '15', 'transferId': '49', 'hero_name': '苍暮·暗刃'},
             {'jobId': '15', 'transferId': '50', 'hero_name': '苍暮·特工'},
             {'jobId': '15', 'transferId': '51', 'hero_name': '苍暮·战线佣兵'},
             {'jobId': '15', 'transferId': '52', 'hero_name': '苍暮·源能专家'},
             {'jobId': '9', 'transferId': '8', 'hero_name': '极诣·黑暗武士'},
             {'jobId': '10', 'transferId': '48', 'hero_name': '知源·缔造者'}]

URL = "https://mwegame.qq.com/yoyo/dnf/getrenownrank"

pbar1 = tqdm(desc='已写入', total=0, leave=True, position=0, unit='条')
pbar2 = tqdm(desc='重新发送失败请求', total=0, leave=False, position=5, bar_format='{l_bar}{bar} | {n}/{total}')
pbar3 = tqdm(leave=False, position=4, bar_format='正在处理: {desc}', total=1, miniters=0)

n = 0


async def get_rank(curRank, transferId, jobId, worldId, name, hero_name, word_name):
    """
   获取排名
    :param name: 小区
    :param word_name:跨区
    :param hero_name: 职业名
    :param curRank:获取排名起始开头
    :param transferId:转职id
    :param jobId:职业ID
    :param worldId:跨区id
    :return:[
             ['排名','名字','名望','用户ID','职业名','大区','小区'],
             ['排名','名字','名望','用户ID','职业名','大区','小区'],
             ...
            ]
    """
    rank_data = []
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=1),
                                         connector=aiohttp.TCPConnector(limit=64, ssl=False, )) as session:
            async with await session.post(
                    url=URL,
                    data={
                        'curRank': curRank,
                        'transferId': transferId,
                        'jobId': jobId,
                        'worldId': worldId,
                        'token': token,
                        'userId': userId,
                    }) as resp:
                dt = json.loads(await resp.text())

        for dta in dt['data']['list']:
            rank_data.append(
                [
                    dta['rank'],
                    dta['roleName'],
                    dta['renownValue'],
                    dta.get('userId', '0'),
                    hero_name,
                    word_name,
                    name,
                ]
            )
        csvwriter.writerows(rank_data)
        pbar1.update(len(rank_data))
        pbar3.set_description_str(f'{hero_name} | {word_name} | {name}')
    except :
        global n
        n += 1
        pbar2.total = n
        await get_rank(curRank, transferId, jobId, worldId, name, hero_name, word_name)
        pbar2.update(1)


if __name__ == '__main__':
    save_path = r'C:\Users\lnori\Desktop\dnf.csv'  # 保存位置
    token = 'rCBfwB4P',  # 抓包获得 有时效
    userId = '235025306',  # 抓包获得
    max_post = 30  # 并发数,最好不要大于100,否则可能会有大量需要重新发送的失败请求
    ###########################
    csvfile = open(save_path, 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows([['排名', '名字', '名望', '用户ID', '职业', '跨区', '小区']])
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    _curRank = [i for i in range(1, 488, 50)]
    task = []

    for hero in tqdm(HERO_LIST, desc='职业', position=1, bar_format='{l_bar}{bar} | {n}/{total}'):
        for wn, v in tqdm(WORD_DICT.items(), leave=False, desc=f"跨区", position=2,
                          bar_format='{l_bar}{bar} | {n}/{total}'):
            for _ in tqdm(v, leave=False, desc='小区', position=3, bar_format='{l_bar}{bar} | {n}/{total}'):
                keys = {
                    'word_name': wn,
                    **hero, **_
                }
                for cr in _curRank:
                    _ = loop.create_task(get_rank(curRank=cr, **keys))
                    task.append(_)
                if len(task) >= max_post:
                    loop.run_until_complete(asyncio.wait(task))
                    task = []

    csvfile.close()
