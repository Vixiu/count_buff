from DataClass.SaveData import save,Data
from DataClass.InputData import InputData
from DataClass.Job import *

save.add_default_config('ma',Data('默认配置',InputData()))
save.add_default_config('ba',Data('默认配置',InputData()))
save.add_default_config('luo',Data('默认配置',InputData()))
save.add_default_config('gong',Data('默认配置',InputData()))
save.add_default_config('qiang',Data('默认配置',InputData()))
save.load_config()
# -------------------------------------------------------------
# 职业数据
# passive_skill,skill_form要按技能等级从小到大

JobData:dict[str,Job]={}
# passive_skill_15=lambda lv:
# todo 公式计算有问题需要改为固定数据
# 数据源 https://developers.neople.co.kr/contents/apiDocs/df
passive_skill_50=lambda lv: 14 + (lv+1 )// 2 * 23 + (lv // 2) * 22
passive_skill_75=lambda lv: 140 + lv * 10
passive_skill_95=lambda lv: 150 + lv * 10
#---------------------------------
JobData['ma']=Job(
    id='ma',name='',attribute='智力',increase=1.141,
    ty1=TY1(name='圣光天启'),
    ty3=TY3(name='祈愿·天使赞歌'),
    buff=Buff(
        name='勇气祝福',
        attack=(39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62, 63, 65, 67, 69, 70, 71, 73, 75,77, 79, 80, 81, 83, 85, 86, 88, 89, 90, 92, 94, 95, 97, 98, 100),
        intellect = (154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290, 302, 311, 321, 332, 342, 353, 363,374, 385, 395, 406, 415, 425, 437, 447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563),
    ),
    skill_form=(
        SkillFrom(
            name='勇气颂歌',
            lv=35,
            multiplier=0.15,
            show=(True,True,False)),# 是否显示(三攻,力智,倍率)
        SkillFrom(
            name='勇气祝福+勇气颂歌',
            lv=35,
            multiplier=1.15,
            show=(True,True,True)),
    ),
    passive_skill=(
        PassiveSkill(
            lv=15,
            out_map=True,
            name='启示:颂歌',
            data=(86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290,301,313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457,473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725,741,756, 772, 788,804, 820, 835, 851, 867, 883, 899)
        ),
        PassiveSkillInf(
            lv=50,
            out_map=False,
            name='虔诚信念',
            max_lv=999,
            _fnc=passive_skill_50
         ),
        PassiveSkillInf(
            lv=75,
            out_map=True,
            name='大天使庇护',
            max_lv=999,
            
            _fnc=passive_skill_75
        ),
        PassiveSkillInf(
            lv=95,
            out_map=True,
            name='圣天使之光',
            max_lv=999,
            
            _fnc=passive_skill_95
        ),

    ),
    total_buff=(
        TotalBuff(
            
            name = '总(一绝下)' ,
            lv=-1,
            skill_from=1,
            is_ty=True
        ),
        TotalBuff(
            
            lv=-1,
            name='总(三绝下)',
            skill_from=1,
            is_ty=False
        ),
    )
)
# --------------------------------------------------------
JobData['gong']=Job(
    id='gong',name='',attribute='精神',increase=1.174,
    ty1=TY1(name='梦想的舞台'),
    ty3=TY3(name='终曲:霓虹蝶梦'),
    buff=Buff(
        name='可爱节拍',
        attack=(40, 42, 44, 46, 47, 49, 51, 52, 54, 55, 56, 58, 60, 61, 63,
                       64, 65, 67, 70, 72, 73, 74, 76, 78, 80, 82, 83, 84, 86, 88,
                       89, 92, 93, 94, 96, 98, 99, 101, 102, 104),
        intellect = (162, 173, 186, 196, 207, 217, 227, 239, 249, 262, 272, 283,
                          295, 306, 318, 328, 338, 350, 360, 372, 382, 394, 406, 416,
                          428, 437, 448, 460, 471, 482, 493, 503, 516, 527, 539, 548,
                          559, 570, 581, 593),
    ),
    skill_form=(
        SkillFrom(
            name='燃情狂想曲',
            lv=35,
            multiplier=0.1,
            show=(True,True,False)),# 是否显示(三攻,力智,倍率)
        SkillFrom(
            name='可爱节拍+燃情狂想曲',
            lv=35,
            multiplier=1.1,
            show=(True,True,True)),
    ),
    passive_skill=(
        PassiveSkill(
            lv=15,
            out_map=True,
            name='多彩感性',
            
            data=(276, 280, 284, 288, 292, 297, 302, 307, 313, 319, 325, 331, 337, 344, 351, 359, 367, 375, 383, 391, 400,
                        409, 419, 428, 438, 448, 459, 469, 480,
                        491, 503, 515, 527, 539, 551,
                        565, 578, 591, 605, 619, 633, 647, 663, 677, 693, 709, 725, 741, 757, 774, 788, 804, 820, 836, 852, 867,
                        883, 899, 915, 931, 946, 962, 978, 994,
                        1010, 1025, 1041, 1057, 1073, 1089)
        ),
        PassiveSkillInf(
            lv=20,
            out_map=False,
            name='主角登场',
            max_lv=999,
            _fnc=passive_skill_50
        ),
        PassiveSkillInf(
            lv=50,
            out_map=False,
            name='明星气场',
            max_lv=999,
            
            _fnc=passive_skill_50
         ),
        PassiveSkillInf(
            lv=75,
            out_map=True,
            name='崭新曲风',
            max_lv=999,
            
            _fnc=passive_skill_75
        ),
        PassiveSkillInf(
            lv=95,
            out_map=True,
            name='和茉霓之歌',
            max_lv=999,
            
            _fnc=passive_skill_95
        ),

    ),
    total_buff=(
        TotalBuff(
            name = '总(一绝下)' ,
            skill_from=1,
            lv=-1,
            is_ty=True
        ),
        TotalBuff(
            
            name='总(三绝下)',
            lv=-1,
            skill_from=1,
            is_ty=False
        ),
    )
)
#---------------------------------------------------
JobData['luo']=Job(
    id='luo',name='',attribute='智力',increase=1.141,
    ty1=TY1(name='开幕！人偶剧场'),
    ty3=TY3(name='终幕！人偶剧场'),
    buff=Buff(
        name='禁忌诅咒',
        
        attack=(34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54,
                       55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76,
                       77, 78, 80, 81, 82, 84, 85, 87),
        intellect = (131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247,
                          256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371,
                          380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478),
    ),
    skill_form=(
        SkillFrom(
            name='疯狂召唤',
            lv=35,
            
            multiplier=0.25,
            show=(True,True,False)
        ),# 是否显示(三攻,力智,倍率)
        SkillFrom(
            name='禁忌诅咒+疯狂召唤',
            lv=35,
            
            multiplier=1.25,
            show=(True,True,True)
        ),
        SkillFrom(
            name='偏爱(禁忌诅咒+疯狂召唤)',
            lv=35,
            
            multiplier=1.4375,
            show=(True, True, True)
        ),
    ),
    passive_skill=(
        PassiveSkill(
            lv=15,
            out_map=True,
            name='人偶操纵者',
            
            data=( 69, 73, 77, 81, 85, 90, 95, 100, 106, 112, 118, 124, 130, 137, 144, 152, 160, 168, 176, 184, 193, 202,
                         212, 221, 231, 241, 252, 262, 273, 284,
                         296, 308, 320, 332, 344, 358, 371, 384, 398, 412, 426, 440, 456, 470, 486, 502, 518, 534, 550, 567, 581,
                         597, 613, 629, 645, 660, 676, 692, 708,
                         724, 739, 755, 771, 787, 803, 818, 834, 850, 866, 882)),
        PassiveSkillInf(
            lv=50,
            out_map=False,
            name='少女的爱',
            max_lv=999,
            
            _fnc=passive_skill_50
         ),
        PassiveSkillInf(
            lv=75,
            out_map=True,
            name='冥月绽放',
            max_lv=999,
            
            _fnc=passive_skill_75
        ),
        PassiveSkillInf(
            lv=95,
            out_map=True,
            name='不祥的微笑',
            max_lv=999,
            
            _fnc=passive_skill_95
        ),

    ),
    total_buff=(
        TotalBuff(
            name = '总(一绝下)' ,
            lv=-1,
            skill_from=1,
            is_ty=True
        ),
        TotalBuff(
            
            name='总(三绝下)',
            lv=-1,
            skill_from=1,
            is_ty=False
        ),
    )
)
#---------------------------------------------------
JobData['ba']=Job(
    id='ba',name='',attribute='体精',increase=1.141,
    ty1=TY1(name='天启之珠'),
    ty3=TY3(name='生命礼赞:神威'),
    buff=Buff(
        name='荣誉祝福',
        attack=(44, 45, 47, 49, 50, 52, 54, 55, 57, 59, 60, 62, 64, 65, 67, 69,
                       70, 72, 74, 77, 78, 80, 82, 83, 85, 87, 88, 90, 92, 93, 95, 97,
                       98, 100, 102, 103, 105, 107, 108, 111),
        intellect = (171, 182, 193, 206, 217, 228, 239, 251, 263, 275, 286, 297, 310, 321,
                          333, 343, 355, 367, 379, 390, 401, 414, 425, 437, 448, 459, 471, 483,
                          494, 505, 518, 529, 541, 552, 565, 575, 587, 598, 609, 622),
         
    ),
    skill_form=(
        SkillFrom(
            name='荣誉祝福(24层)',
            lv=35,
            multiplier=1.12,
            show=(True,True,True)
        ),
    ),
    passive_skill=(
        PassiveSkill(
            lv=15,
            out_map=True,
            name='守护恩赐',
            data=( 0,)),
        PassiveSkill(
            lv=25,
            out_map=False,
            name='守护徽章',
            data=( 0,)),
        PassiveSkillInf(
            lv=50,
            out_map=False,
            name='信念光环',
            max_lv=999,
            _fnc=passive_skill_50
         ),
        PassiveSkillInf(
            lv=75,
            out_map=True,
            name='神圣之光',
            max_lv=999,
            _fnc=passive_skill_75
        ),
        PassiveSkillInf(
            lv=95,
            out_map=True,
            name='神之代行者',
            max_lv=999,
            _fnc=passive_skill_95
        ),

    ),
    total_buff=(
        TotalBuff(
            
            name = '总(一绝下)' ,
            lv=-1,
            skill_from=0,
            is_ty=True
        ),
        TotalBuff(
            
            name='总(三绝下)',
            lv=-1,
            skill_from=0,
            is_ty=False
        ),
    )
)
JobData['qiang']=Job(
    id='qiang',name='',attribute='精神',increase=1.174,
    ty1=TY1(name='强袭策略:区域肃清'),
    ty3=TY3(name='空袭策略:神兵天降'),
    buff=Buff(
        name='军械强化',
        attack=(44,),
        intellect = (171, ),
         
    ),
    skill_form=(
        SkillFrom(
            name='军械强化(进阶)',
            lv=35,
            multiplier=0.12,
            show=(True,True,False)
        ),
        SkillFrom(
            name='军械强化(总)',
            lv=35,
            multiplier=1.12,
            show=(True, True, True)
        ),
    ),
    passive_skill=(
        PassiveSkill(
            lv=15,
            out_map=True,
            name='系统·战场信息',
            data=( 0,)),
        PassiveSkill(
            lv=25,
            out_map=False,
            name='装甲强化',
            data=(0,)),
        PassiveSkill(
            lv=50,
            out_map=False,
            name='系统·作战应对',
            data=(0,)),
        PassiveSkill(
            lv=75,
            out_map=True,
            name='系统·限制解除',
            data=(0,)),
        PassiveSkill(
            lv=95,
            out_map=True,
            name='系统·临战编程',
            data=(0,)),
    ),
    total_buff=(
        TotalBuff(
            name = '总(一绝下)' ,
            lv=-1,
            skill_from=1,
            is_ty=True
        ),
        TotalBuff(
            name='总(三绝下)',
            lv=-1,
            skill_from=1,
            is_ty=False
        ),
    )
)