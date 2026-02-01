const JOB_LABELS = {
  ma: "奶妈",
  ba: "奶爸",
  luo: "奶萝",
  gong: "奶弓",
  qiang: "奶枪",
};

const TY1_DEFAULT = {
  intellect: [
    43, 57, 74, 91, 111, 131, 153, 176, 201, 228,
    255, 284, 315, 346, 379, 414, 449, 487, 526, 567,
    608, 651, 696, 741, 789, 838, 888, 939, 993, 1047,
    1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668,
  ],
  xs: 750,
  xyz: [5250, 5000, 0.000025],
  lv: 50,
};

const TY3_DEFAULT = {
  lv: 100,
  bind1: 1.08,
  bind2: 1.23,
  growth: 0.01,
};

const BUFF_DEFAULT = {
  lv: 35,
  xs: 665,
  xyz: [4350, 3500, 3.78880649805069e-05],
};

const JOB_DATA = {
  ma: {
    id: "ma",
    name: "奶妈",
    attribute: "智力",
    increase: 1.141,
    buff: {
      ...BUFF_DEFAULT,
      name: "勇气祝福",
      attack: [39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62, 63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88, 89, 90, 92, 94, 95, 97, 98, 100],
      intellect: [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290, 302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437, 447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563],
    },
    ty1: { ...TY1_DEFAULT, name: "圣光天启" },
    ty3: { ...TY3_DEFAULT, name: "祈愿·天使赞歌" },
    skill_form: [
      { name: "勇气颂歌", lv: 35, multiplier: 0.15, show: [true, true, false] },
      { name: "勇气祝福+勇气颂歌", lv: 35, multiplier: 1.15, show: [true, true, true] },
    ],
    passive_skill: [
      {
        lv: 15,
        out_map: true,
        name: "启示:颂歌",
        data: [
          86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290, 301, 313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457, 473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725, 741, 756, 772, 788, 804, 820, 835, 851, 867, 883, 899,
        ],
      },
      {
        lv: 50,
        out_map: false,
        name: "虔诚信念",
        data: [
          14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442, 464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892, 914, 937, 959, 982, 1004, 1027, 1049, 1072, 1094, 1117,
        ],
      },
      {
        lv: 75,
        out_map: true,
        name: "大天使庇护",
        data: [
          150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
        ],
      },
      {
        lv: 95,
        out_map: true,
        name: "圣天使之光",
        data: [
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
        ],
      },
    ],
    total_buff: [
      { name: "总(一绝下)", lv: -1, skill_from: 1, is_ty: true },
      { name: "总(三绝下)", lv: -1, skill_from: 1, is_ty: false },
    ],
  },
  gong: {
    id: "gong",
    name: "奶弓",
    attribute: "精神",
    increase: 1.174,
    buff: {
      ...BUFF_DEFAULT,
      name: "可爱节拍",
      attack: [40, 42, 44, 46, 47, 49, 51, 52, 54, 55, 56, 58, 60, 61, 63, 64, 65, 67, 70, 72, 73, 74, 76, 78, 80, 82, 83, 84, 86, 88, 89, 92, 93, 94, 96, 98, 99, 101, 102, 104],
      intellect: [162, 173, 186, 196, 207, 217, 227, 239, 249, 262, 272, 283, 295, 306, 318, 328, 338, 350, 360, 372, 382, 394, 406, 416, 428, 437, 448, 460, 471, 482, 493, 503, 516, 527, 539, 548, 559, 570, 581, 593],
    },
    ty1: { ...TY1_DEFAULT, name: "梦想的舞台" },
    ty3: { ...TY3_DEFAULT, name: "终曲:霓虹蝶梦" },
    skill_form: [
      { name: "燃情狂想曲", lv: 35, multiplier: 0.1, show: [true, true, false] },
      { name: "可爱节拍+燃情狂想曲", lv: 35, multiplier: 1.1, show: [true, true, true] },
    ],
    passive_skill: [
      {
        lv: 15,
        out_map: true,
        name: "多彩感性",
        data: [
          276, 280, 284, 288, 292, 297, 302, 307, 313, 319, 325, 331, 337, 344, 351, 359, 367, 375, 383, 391, 400, 409, 419, 428, 438, 448, 459, 469, 480, 491, 503, 515, 527, 539, 551, 565, 578, 591, 605, 619, 633, 647, 663, 677, 693, 709, 725, 741, 757, 774, 788, 804, 820, 836, 852, 867, 883, 899, 915, 931, 946, 962, 978, 994, 1010, 1025, 1041, 1057, 1073, 1089,
        ],
      },
      {
        lv: 20,
        out_map: false,
        name: "主角登场",
        data: [94, 98, 102, 107, 112, 116, 122, 127, 131, 137, 141, 147, 153, 158, 163, 169, 175, 181, 187, 192],
      },
      {
        lv: 50,
        out_map: false,
        name: "明星气场",
        data: [
          6, 25, 44, 63, 82, 101, 120, 139, 158, 177, 196, 215, 234, 253, 272, 291, 310, 329, 348, 367, 386, 405, 424, 443, 462, 485, 507, 530, 552, 575, 597, 620, 642, 665, 687, 710, 732, 755, 777, 800, 822, 845, 867, 890, 912, 935, 957, 980, 1002, 1025,
        ],
      },
      {
        lv: 75,
        out_map: true,
        name: "崭新曲风",
        data: [
          150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
        ],
      },
      {
        lv: 95,
        out_map: true,
        name: "和茉霓之歌",
        data: [
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
        ],
      },
    ],
    total_buff: [
      { name: "总(一绝下)", lv: -1, skill_from: 1, is_ty: true },
      { name: "总(三绝下)", lv: -1, skill_from: 1, is_ty: false },
    ],
  },
  luo: {
    id: "luo",
    name: "奶萝",
    attribute: "智力",
    increase: 1.141,
    buff: {
      ...BUFF_DEFAULT,
      name: "禁忌诅咒",
      attack: [34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 87],
      intellect: [131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478],
    },
    ty1: { ...TY1_DEFAULT, name: "开幕！人偶剧场" },
    ty3: { ...TY3_DEFAULT, name: "终幕！人偶剧场" },
    skill_form: [
      { name: "疯狂召唤", lv: 35, multiplier: 0.25, show: [true, true, false] },
      { name: "禁忌诅咒+疯狂召唤", lv: 35, multiplier: 1.25, show: [true, true, true] },
      { name: "偏爱(禁忌诅咒+疯狂召唤)", lv: 35, multiplier: 1.4375, show: [true, true, true] },
    ],
    passive_skill: [
      {
        lv: 15,
        out_map: true,
        name: "人偶操纵者",
        data: [
          130, 136, 143, 150, 157, 165, 172, 180, 188, 196, 205, 214, 223, 232, 242, 252, 262, 272, 282, 292, 303, 314, 325, 336, 348, 360, 372, 384, 397, 410, 423, 436, 449, 463, 477, 491, 505, 519, 534, 549, 564, 579, 595, 611, 627, 643, 660, 676, 693, 710,
        ],
      },
      {
        lv: 50,
        out_map: false,
        name: "少女的爱",
        data: [
          36, 54, 73, 91, 110, 129, 147, 166, 185, 203, 222, 241, 259, 278, 297, 315, 334, 353, 371, 390, 409, 427, 446, 465, 483, 502, 521, 539, 558, 577, 595, 614, 633, 651, 670, 689, 707, 726, 745, 763, 782, 801, 819, 838, 857, 875, 894, 913, 931, 950,
        ],
      },
      {
        lv: 75,
        out_map: true,
        name: "冥月绽放",
        data: [
          150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
        ],
      },
      {
        lv: 95,
        out_map: true,
        name: "不祥的微笑",
        data: [
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
        ],
      },
    ],
    total_buff: [
      { name: "总(一绝下)", lv: -1, skill_from: 1, is_ty: true },
      { name: "总(三绝下)", lv: -1, skill_from: 1, is_ty: false },
    ],
  },
  ba: {
    id: "ba",
    name: "奶爸",
    attribute: "体力",
    increase: 1.141,
    buff: {
      ...BUFF_DEFAULT,
      name: "荣誉祝福",
      attack: [44, 45, 47, 49, 50, 52, 54, 55, 57, 59, 60, 62, 64, 65, 67, 69, 70, 72, 74, 77, 78, 80, 82, 83, 85, 87, 88, 90, 92, 93, 95, 97, 98, 100, 102, 103, 105, 107, 108, 111],
      intellect: [171, 182, 193, 206, 217, 228, 239, 251, 263, 275, 286, 297, 310, 321, 333, 343, 355, 367, 379, 390, 401, 414, 425, 437, 448, 459, 471, 483, 494, 505, 518, 529, 541, 552, 565, 575, 587, 598, 609, 622],
    },
    ty1: { ...TY1_DEFAULT, name: "天启之珠" },
    ty3: { ...TY3_DEFAULT, name: "生命礼赞:神威" },
    skill_form: [
      { name: "荣誉祝福(24层)", lv: 35, multiplier: 1.12, show: [true, true, true] },
    ],
    passive_skill: [
      {
        lv: 15,
        out_map: true,
        name: "守护恩赐",
        data: [
          220, 224, 228, 232, 236, 241, 246, 251, 257, 263, 269, 275, 281, 288, 295, 303, 311, 319, 327, 335, 344, 353, 363, 372, 382, 392, 403, 413, 424, 435, 447, 459, 471, 483, 495, 509, 522, 535, 549, 563, 577, 591, 607, 621, 637, 653, 669, 685, 701, 718, 732, 748, 764, 780, 796, 811, 827, 843, 859, 875, 890, 906, 922, 937, 953, 969, 985, 1001, 1016, 1032,
        ],
      },
      {
        lv: 25,
        out_map: false,
        name: "守护徽章",
        data: [94, 98, 102, 107, 112, 116, 122, 127, 131, 137, 141, 147, 153, 158, 163, 169, 175, 181, 187, 192],
      },
      {
        lv: 50,
        out_map: false,
        name: "信念光环",
        data: [
          10, 29, 48, 67, 86, 105, 124, 143, 162, 181, 200, 219, 238, 257, 276, 295, 314, 333, 352, 371, 390, 409, 428, 447, 466, 489, 511, 534, 556, 579, 601, 624, 646, 669, 691, 714, 736, 759, 781, 804, 826, 849, 871, 894, 916, 939, 961, 984, 1006, 1029,
        ],
      },
      {
        lv: 75,
        out_map: true,
        name: "神圣之光",
        data: [
          150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
        ],
      },
      {
        lv: 95,
        out_map: true,
        name: "神之代行者",
        data: [
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
        ],
      },
    ],
    total_buff: [
      { name: "总(一绝下)", lv: -1, skill_from: 0, is_ty: true },
      { name: "总(三绝下)", lv: -1, skill_from: 0, is_ty: false },
    ],
  },
  qiang: {
    id: "qiang",
    name: "奶枪",
    attribute: "精神",
    increase: 1.174,
    buff: {
      ...BUFF_DEFAULT,
      lv: 30,
      name: "军械强化",
      attack: [41, 42, 44, 45, 46, 48, 50, 51, 53, 55, 56, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 81, 83, 85, 86, 88, 90, 91, 93, 94, 95, 97, 99, 100, 103],
      intellect: [161, 171, 181, 193, 204, 214, 224, 236, 247, 258, 269, 279, 291, 301, 313, 322, 333, 345, 356, 366, 377, 389, 399, 410, 421, 431, 442, 454, 464, 474, 486, 497, 508, 518, 531, 540, 551, 562, 572, 584],
    },
    ty1: { ...TY1_DEFAULT, name: "强袭策略:区域肃清" },
    ty3: { ...TY3_DEFAULT, name: "空袭策略:神兵天降" },
    skill_form: [
      { name: "军械强化(进阶)", lv: 35, multiplier: 0.12, show: [true, true, false] },
      { name: "军械强化(总)", lv: 35, multiplier: 1.12, show: [true, true, true] },
    ],
    passive_skill: [
      {
        lv: 15,
        out_map: true,
        name: "系统·战场信息",
        data: [
          266, 270, 274, 278, 282, 287, 292, 297, 303, 309, 315, 321, 327, 334, 341, 349, 357, 365, 373, 381, 390, 399, 409, 418, 428, 438, 449, 459, 470, 481, 493, 505, 517, 529, 541, 555, 568, 581, 595, 609, 623, 637, 653, 667, 683, 699, 715, 731, 747, 764, 778, 794, 810, 826, 842, 857, 873, 889, 905, 921, 936, 952, 968, 983, 999, 1015, 1031, 1047, 1062, 1078,
        ],
      },
      {
        lv: 25,
        out_map: false,
        name: "装甲强化",
        data: [94, 98, 102, 107, 112, 116, 122, 127, 131, 137, 141, 147, 153, 158, 163, 169, 175, 181, 187, 192],
      },
      {
        lv: 50,
        out_map: false,
        name: "系统·作战应对",
        data: [
          10, 29, 48, 67, 86, 105, 124, 143, 162, 181, 200, 219, 238, 257, 276, 295, 314, 333, 352, 371, 390, 409, 428, 447, 466, 489, 511, 534, 556, 579, 601, 624, 646, 669, 691, 714, 736, 759, 781, 804, 826, 849, 871, 894, 916, 939, 961, 984, 1006, 1029,
        ],
      },
      {
        lv: 75,
        out_map: true,
        name: "系统·限制解除",
        data: [
          150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640,
        ],
      },
      {
        lv: 95,
        out_map: true,
        name: "系统·临战编程",
        data: [
          160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
        ],
      },
    ],
    total_buff: [
      { name: "总(一绝下)", lv: -1, skill_from: 1, is_ty: true },
      { name: "总(三绝下)", lv: -1, skill_from: 1, is_ty: false },
    ],
  },
};

const defaultInputData = () => ({
  c_attack: 3350,
  c_intellect: 24500,
  buff_intellect_in_map: 0,
  buff_lv_in_map: 37,
  buff_intellect_out_map: 0,
  buff_lv_out_map: 37,
  buff_amount_in_map: 0,
  buff_amount_out_map: 0,
  buff_amount_amp: 0,
  bxy_amp: 0,
  bxy_fixed_attack: 0,
  bxy_fixed_intellect: 0,
  bxy_fixed_ty: 0,
  bxy_percentage_attack: [0],
  bxy_percentage_intellect: [0],
  bxy_percentage_ty: [0, 0],
  ty_ty1_lv: 41,
  ty_intellect: 0,
  ty_ty3_lv: 7,
  ty_is_ty1: true,
  passive_skills: Array(7).fill(1),
});

const state = {
  jobId: "ma",
  data: defaultInputData(),
  basePassiveSkill: defaultInputData().passive_skills.slice(),
  baselineResult: null,
};

const elements = {
  jobSelect: document.getElementById("jobSelect"),
  cAttack: document.getElementById("cAttack"),
  cIntellect: document.getElementById("cIntellect"),
  buffIntellectIn: document.getElementById("buffIntellectIn"),
  buffLvIn: document.getElementById("buffLvIn"),
  buffIntellectOut: document.getElementById("buffIntellectOut"),
  buffLvOut: document.getElementById("buffLvOut"),
  buffAmountIn: document.getElementById("buffAmountIn"),
  buffAmountOut: document.getElementById("buffAmountOut"),
  buffAmountAmp: document.getElementById("buffAmountAmp"),
  bxyAmp: document.getElementById("bxyAmp"),
  bxyFixedAttack: document.getElementById("bxyFixedAttack"),
  bxyFixedIntellect: document.getElementById("bxyFixedIntellect"),
  bxyFixedTy: document.getElementById("bxyFixedTy"),
  bxyPercentageAttack: document.getElementById("bxyPercentageAttack"),
  bxyPercentageIntellect: document.getElementById("bxyPercentageIntellect"),
  bxyPercentageTy: document.getElementById("bxyPercentageTy"),
  ty1Lv: document.getElementById("ty1Lv"),
  tyIntellect: document.getElementById("tyIntellect"),
  ty3Lv: document.getElementById("ty3Lv"),
  tyBind1: document.getElementById("tyBind1"),
  tyBind3: document.getElementById("tyBind3"),
  passiveSkillContainer: document.getElementById("passiveSkillContainer"),
  resultBody: document.getElementById("resultBody"),
  baselineNote: document.getElementById("baselineNote"),
  setBaseline: document.getElementById("setBaseline"),
  setSkillBaseline: document.getElementById("setSkillBaseline"),
  resetData: document.getElementById("resetData"),
};

function fillJobOptions() {
  elements.jobSelect.innerHTML = Object.keys(JOB_DATA)
    .map((id) => `<option value="${id}">${JOB_LABELS[id] || id}</option>`)
    .join("");
  elements.jobSelect.value = state.jobId;
}

function toNumber(value, fallback = 0) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function toInt(value, fallback = 0) {
  const parsed = parseInt(value, 10);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function toFloatArray(value) {
  if (!value) {
    return [];
  }
  return value
    .split(/[,，]/)
    .map((item) => item.trim())
    .filter((item) => item.length > 0)
    .map((item) => Number(item))
    .filter((num) => Number.isFinite(num));
}

function getArrayValue(array, level) {
  if (!array || array.length === 0) {
    return 0;
  }
  const index = Math.max(0, Math.min(level - 1, array.length - 1));
  return array[index];
}

function roundTo(value, digits = 2) {
  const factor = 10 ** digits;
  return Math.round(value * factor) / factor;
}

function countBuff(buffAmount, intellect, xs, xyz) {
  const [x, y, z] = xyz;
  return (fixed, percentages, basic) => {
    let oldBuff = (basic + fixed) * (intellect / xs + 1);
    percentages.forEach((percent) => {
      oldBuff *= 1 + percent / 100;
    });
    const newBuff = buffAmount !== 0
      ? basic * ((intellect + x) / xs + 1) * (buffAmount + y) * z
      : 0;
    return Math.round(oldBuff + newBuff);
  };
}

function countMultiplier(attack, intellect, data, job) {
  const multiplier = roundTo(
    (1 + attack / data.c_attack) * (1 + intellect / (data.c_intellect + 250)) * job.increase,
    2,
  );
  return { attack, intellect, multiplier };
}

function countBuffItem(intellect, buffAmount, lv, data, job) {
  const count = countBuff(buffAmount, intellect, job.buff.xs, job.buff.xyz);
  const attack = count(data.bxy_fixed_attack, data.bxy_percentage_attack, getArrayValue(job.buff.attack, lv));
  const intellectValue = count(
    data.bxy_fixed_intellect,
    data.bxy_percentage_intellect,
    getArrayValue(job.buff.intellect, lv),
  );
  return countMultiplier(attack, intellectValue, data, job);
}

function countTy(data, job, intellect) {
  const count = countBuff(data.in_map_buff_amount, intellect, job.ty1.xs, job.ty1.xyz);
  const ty1Value = count(data.bxy_fixed_ty, data.bxy_percentage_ty, getArrayValue(job.ty1.intellect, data.ty_ty1_lv));
  const ty3Value = Math.round(
    ty1Value * ((data.ty_is_ty1 ? job.ty3.bind1 : job.ty3.bind2) + data.ty_ty3_lv * job.ty3.growth),
  );
  return {
    ty1: countMultiplier(0, ty1Value, data, job),
    ty3: countMultiplier(0, ty3Value, data, job),
  };
}

function calculateResult(data, job, basePassiveSkill) {
  let intellectIn = 0;
  let intellectOut = 0;
  job.passive_skill.forEach((skill, index) => {
    const currentLv = data.passive_skills[index] ?? 1;
    const baseLv = basePassiveSkill[index] ?? 1;
    const delta = getArrayValue(skill.data, currentLv) - getArrayValue(skill.data, baseLv);
    intellectIn += delta;
    if (skill.out_map) {
      intellectOut += delta;
    }
  });

  const buffOutMap = countBuffItem(
    intellectOut + data.buff_intellect_out_map,
    data.out_map_buff_amount,
    data.buff_lv_out_map,
    data,
    job,
  );
  const buffInMap = countBuffItem(
    intellectIn + data.buff_intellect_in_map,
    data.in_map_buff_amount,
    data.buff_lv_in_map,
    data,
    job,
  );

  const skillFrom = job.skill_form.map((item) =>
    countMultiplier(
      Math.round(buffInMap.attack * item.multiplier),
      Math.round(buffInMap.intellect * item.multiplier),
      data,
      job,
    ),
  );

  const { ty1, ty3 } = countTy(data, job, intellectIn + data.ty_intellect);

  const total = job.total_buff.map((item) => {
    const source = skillFrom[item.skill_from];
    const intellect = source.intellect + (item.is_ty ? ty1.intellect : ty3.intellect);
    return countMultiplier(source.attack, intellect, data, job);
  });

  return { buffOutMap, buffInMap, skillFrom, ty1, ty3, total };
}

function updateDerivedData(data) {
  data.in_map_buff_amount = (data.buff_amount_in_map + data.buff_amount_out_map) * (1 + data.buff_amount_amp / 100 + data.bxy_amp / 100);
  data.out_map_buff_amount = data.buff_amount_out_map * (1 + data.buff_amount_amp / 100);
}

function subtractItem(current, baseline) {
  if (!baseline) {
    return { attack: 0, intellect: 0, multiplier: 0 };
  }
  return {
    attack: current.attack - baseline.attack,
    intellect: current.intellect - baseline.intellect,
    multiplier: roundTo(current.multiplier - baseline.multiplier, 2),
  };
}

function formatDelta(value) {
  if (!value) {
    return "0";
  }
  return value > 0 ? `+${value}` : `${value}`;
}

function getResultRows(result) {
  const job = JOB_DATA[state.jobId];
  const rows = [
    { label: `${job.buff.name}(图外)`, item: result.buffOutMap },
    { label: `${job.buff.name}(图内)`, item: result.buffInMap },
    ...job.skill_form.map((item, idx) => ({ label: item.name, item: result.skillFrom[idx] })),
    { label: job.ty1.name, item: result.ty1 },
    { label: job.ty3.name, item: result.ty3 },
    ...job.total_buff.map((item, idx) => ({ label: item.name, item: result.total[idx] })),
  ];
  return rows;
}

function renderResults() {
  const data = state.data;
  updateDerivedData(data);

  const job = JOB_DATA[state.jobId];
  const result = calculateResult(data, job, state.basePassiveSkill);
  const baseline = state.baselineResult;
  const baselineRows = baseline ? getResultRows(baseline) : [];
  const baselineMap = new Map(baselineRows.map((row) => [row.label, row.item]));

  elements.resultBody.innerHTML = getResultRows(result)
    .map((row) => {
      const baselineItem = baselineMap.get(row.label);
      const delta = subtractItem(row.item, baselineItem);
      const deltaClass = delta.attack > 0 || delta.intellect > 0 || delta.multiplier > 0
        ? "delta-positive"
        : delta.attack < 0 || delta.intellect < 0 || delta.multiplier < 0
          ? "delta-negative"
          : "";
      return `
        <tr>
          <td>${row.label}</td>
          <td>${row.item.attack}</td>
          <td>${row.item.intellect}</td>
          <td>${row.item.multiplier}</td>
          <td class="${deltaClass}">${formatDelta(delta.attack)}</td>
          <td class="${deltaClass}">${formatDelta(delta.intellect)}</td>
          <td class="${deltaClass}">${formatDelta(delta.multiplier)}</td>
        </tr>
      `;
    })
    .join("");
}

function updateBaselineNote() {
  elements.baselineNote.textContent = state.baselineResult
    ? "已设置基准，表格内显示当前与基准的差值。"
    : "尚未设置基准。";
}

function syncForm() {
  const data = state.data;
  elements.cAttack.value = data.c_attack;
  elements.cIntellect.value = data.c_intellect;
  elements.buffIntellectIn.value = data.buff_intellect_in_map;
  elements.buffLvIn.value = data.buff_lv_in_map;
  elements.buffIntellectOut.value = data.buff_intellect_out_map;
  elements.buffLvOut.value = data.buff_lv_out_map;
  elements.buffAmountIn.value = data.buff_amount_in_map;
  elements.buffAmountOut.value = data.buff_amount_out_map;
  elements.buffAmountAmp.value = data.buff_amount_amp;
  elements.bxyAmp.value = data.bxy_amp;
  elements.bxyFixedAttack.value = data.bxy_fixed_attack;
  elements.bxyFixedIntellect.value = data.bxy_fixed_intellect;
  elements.bxyFixedTy.value = data.bxy_fixed_ty;
  elements.bxyPercentageAttack.value = data.bxy_percentage_attack.join(",");
  elements.bxyPercentageIntellect.value = data.bxy_percentage_intellect.join(",");
  elements.bxyPercentageTy.value = data.bxy_percentage_ty.join(",");
  elements.ty1Lv.value = data.ty_ty1_lv;
  elements.tyIntellect.value = data.ty_intellect;
  elements.ty3Lv.value = data.ty_ty3_lv;
  elements.tyBind1.checked = data.ty_is_ty1;
  elements.tyBind3.checked = !data.ty_is_ty1;
  renderPassiveSkills();
  renderResults();
  updateBaselineNote();
}

function renderPassiveSkills() {
  const job = JOB_DATA[state.jobId];
  elements.passiveSkillContainer.innerHTML = job.passive_skill
    .map((skill, index) => {
      const value = state.data.passive_skills[index] ?? 1;
      return `
        <label>
          ${skill.name}(Lv${skill.lv})
          <input
            type="number"
            min="1"
            max="${skill.data.length}"
            data-passive-index="${index}"
            value="${value}"
          />
        </label>
      `;
    })
    .join("");
}

function attachInputEvents() {
  const numberFields = [
    { element: elements.cAttack, key: "c_attack", parser: toInt },
    { element: elements.cIntellect, key: "c_intellect", parser: toInt },
    { element: elements.buffIntellectIn, key: "buff_intellect_in_map", parser: toInt },
    { element: elements.buffLvIn, key: "buff_lv_in_map", parser: toInt },
    { element: elements.buffIntellectOut, key: "buff_intellect_out_map", parser: toInt },
    { element: elements.buffLvOut, key: "buff_lv_out_map", parser: toInt },
    { element: elements.buffAmountIn, key: "buff_amount_in_map", parser: toInt },
    { element: elements.buffAmountOut, key: "buff_amount_out_map", parser: toInt },
    { element: elements.buffAmountAmp, key: "buff_amount_amp", parser: toNumber },
    { element: elements.bxyAmp, key: "bxy_amp", parser: toNumber },
    { element: elements.bxyFixedAttack, key: "bxy_fixed_attack", parser: toInt },
    { element: elements.bxyFixedIntellect, key: "bxy_fixed_intellect", parser: toInt },
    { element: elements.bxyFixedTy, key: "bxy_fixed_ty", parser: toInt },
    { element: elements.ty1Lv, key: "ty_ty1_lv", parser: toInt },
    { element: elements.tyIntellect, key: "ty_intellect", parser: toInt },
    { element: elements.ty3Lv, key: "ty_ty3_lv", parser: toInt },
  ];

  numberFields.forEach(({ element, key, parser }) => {
    element.addEventListener("input", (event) => {
      state.data[key] = parser(event.target.value, 0);
      renderResults();
    });
  });

  elements.bxyPercentageAttack.addEventListener("input", (event) => {
    const values = toFloatArray(event.target.value);
    state.data.bxy_percentage_attack = values.length ? values : [0];
    renderResults();
  });
  elements.bxyPercentageIntellect.addEventListener("input", (event) => {
    const values = toFloatArray(event.target.value);
    state.data.bxy_percentage_intellect = values.length ? values : [0];
    renderResults();
  });
  elements.bxyPercentageTy.addEventListener("input", (event) => {
    const values = toFloatArray(event.target.value);
    state.data.bxy_percentage_ty = values.length ? values : [0, 0];
    renderResults();
  });

  elements.tyBind1.addEventListener("change", () => {
    state.data.ty_is_ty1 = true;
    renderResults();
  });
  elements.tyBind3.addEventListener("change", () => {
    state.data.ty_is_ty1 = false;
    renderResults();
  });

  elements.jobSelect.addEventListener("change", (event) => {
    state.jobId = event.target.value;
    state.data = defaultInputData();
    state.basePassiveSkill = state.data.passive_skills.slice();
    state.baselineResult = null;
    syncForm();
  });

  elements.passiveSkillContainer.addEventListener("input", (event) => {
    const target = event.target;
    const index = target.getAttribute("data-passive-index");
    if (index === null) {
      return;
    }
    state.data.passive_skills[Number(index)] = toInt(target.value, 1);
    renderResults();
  });

  elements.setBaseline.addEventListener("click", () => {
    const job = JOB_DATA[state.jobId];
    updateDerivedData(state.data);
    state.baselineResult = calculateResult(state.data, job, state.basePassiveSkill);
    updateBaselineNote();
    renderResults();
  });

  elements.setSkillBaseline.addEventListener("click", () => {
    state.basePassiveSkill = state.data.passive_skills.slice();
    state.baselineResult = null;
    updateBaselineNote();
    renderResults();
  });

  elements.resetData.addEventListener("click", () => {
    state.data = defaultInputData();
    state.basePassiveSkill = state.data.passive_skills.slice();
    state.baselineResult = null;
    syncForm();
  });
}

fillJobOptions();
attachInputEvents();
syncForm();
