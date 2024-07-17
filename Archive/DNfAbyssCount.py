# coding=utf-8
import json

import requests

context = 20240120
url = "https://mwegame.qq.com/yoyo/dnf/getdnfuserdiary"
payload = "userId=748807497&token=BuUsRjx4&roleId=5750507&uniqueRoleId=1067948569&sdate=20240120&context="
headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 9; TAS-AN00 Build/PQ3A.190705.09211555; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 GH_QQConnect GameHelper_1006/2103150011",
    'Accept': "application/json",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'clsq-verify': "QnVVc1JqeDQ7MTI5MDA0NTkwMTs3NDg4MDc0OTc=",
    'origin': "https://mwegame.qq.com",
    'x-requested-with': "com.tencent.gamehelper.dnf",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://mwegame.qq.com/fe/dnf/weekly/daily?toOpenid=1E69404B7C419CB2A65A519BBD44E5FD&serverName=%E5%8D%8E%E5%8C%97%E4%B8%80%E5%8C%BA&toUin=1080501622100094&cGameId=1006&serverId=10&gameName=DNF&areaName=%E5%8D%8E%E5%8C%97&nickname=%E7%94%A8%E6%88%B73927&uin=1290045901&roleLevel=110&accType=qc&roleId=53936308&uniqueRoleId=3617794916&avatar=https%3A%2F%2Fcdn.helper.qq.com%2Fimages%2Fdefault_avatar.png%3Flevel%3D%2Fl%2F1006%2F23.png&accessToken=09A1C6A6FDABBF3EE2EC583F0F587D81&userId=748807497&token=BuUsRjx4&isMainRole=0&subGameId=10014&appOpenid=1E69404B7C419CB2A65A519BBD44E5FD&areaId=29&roleJob=%E9%87%8D%E9%9C%84%C2%B7%E5%90%88%E9%87%91%E6%88%98%E5%A3%AB&appid=1105742785&roleName=%E9%98%BF%E7%B1%B3%E5%91%80&gameId=10014&_v=2&",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'Cookie': "access_token=09A1C6A6FDABBF3EE2EC583F0F587D81; appOpenId=1E69404B7C419CB2A65A519BBD44E5FD; appOpenid=1E69404B7C419CB2A65A519BBD44E5FD; "
              "openId=1E69404B7C419CB2A65A519BBD44E5FD; openid=1E69404B7C419CB2A65A519BBD44E5FD; appid=1105742785; appId=1105742785; uin=o01290045901; "
              "accessToken=09A1C6A6FDABBF3EE2EC583F0F587D81; acctype=qc; access_token=09A1C6A6FDABBF3EE2EC583F0F587D81; appOpenId=1E69404B7C419CB2A65A519BBD44E5FD; "
              "appOpenid=1E69404B7C419CB2A65A519BBD44E5FD; openId=1E69404B7C419CB2A65A519BBD44E5FD; openid=1E69404B7C419CB2A65A519BBD44E5FD; appid=1105742785; appId=1105742785; "
              "uin=o01290045901; accessToken=09A1C6A6FDABBF3EE2EC583F0F587D81; acctype=qc "
}

count = {}
while True:
    payload = f"{payload}{context}"
    res = requests.post(url, data=payload, headers=headers)
    res = json.loads(res.text)

    data = {}
    if 'data' in res:

        data = res['data']

        for k, v in data.items():
            if k == 'context':
                context = v
            else:
                if v['copys']:
                    count[k] = v['copys'].get('1', {}).get('times', 0)

    else:
        break
num = 0
for k, v in count.items():
    print(k, ":", v)
    num += v
print(f"共计:{num}")
