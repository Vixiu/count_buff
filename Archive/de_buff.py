z = 1


def count_buff(lv, buff_amount, intellect):
    basic_attack = BASIC_DATA[lv - 1]
    xs = 665
    x, y = (4350, 3500)
    old_buff = basic_attack * ((intellect / xs) + 1)

    new_buff = basic_attack * ((intellect + x) / xs + 1) * (
            buff_amount + y) * z if buff_amount != 0 else 0

    buff = (old_buff + new_buff)
    return round(buff)


def binary_de():
    global z, n
    max_num = 1
    min_num = 0
    flag = True
    num = 1
    # 使用二分查找

    while flag:
        z = (max_num + min_num) / 2
        print(f'第{num}次-----------------')
        num += 1
        for i,ls in enumerate(sg):
            c = count_buff(*ls[:-1]) - ls[-1]
            print(f'Z值:{z} 与 第{i}项 的误差为:{c}')
            if c < -n:
                min_num = z
                flag = True
            elif c > n:
                max_num = z
                flag = True

            else:
                flag = False

        if num > 100:
            n += 1
            num = 1

# 力智
BASIC_DATA = [154, 164, 176, 186, 197, 206, 216, 227, 237, 249, 259, 269, 280, 290,
              302, 311, 321, 332, 342, 353, 363, 374, 385, 395, 406, 415, 425, 437,
              447, 458, 468, 478, 489, 500, 511, 520, 530, 541, 551, 563]
# 三公
BASIC_DATA2=[39, 41, 43, 44, 45, 47, 49, 50, 52, 53, 54, 56, 58, 59, 61, 62,
                     63, 65, 67, 69, 70, 71, 73, 75, 77, 79, 80, 81, 83, 85, 86, 88,
                     89, 90, 92, 94, 95, 97, 98, 100]

sg = [
    # [等级, 增益量, 适用智力, 实际理智]
    [36, 235998, 9541, 111262],
    [27, 235998, 9541, 90935],
    [25, 214268, 9207, 77668],
    [34, 214268, 9207, 95651],
    [33, 236748, 8662, 98404]

]

sg2 = [
     # [等级, 增益量, 适用智力, 实际三攻]
    [36, 235998, 9541, 20113],
    [27, 235998, 9541, 17117],
    [25, 214268, 9207, 14730],
    [34, 214268, 9207, 17217],
    [33, 236748, 8662, 17910]
 ]

# 不要穿戴任何百分比加成的装备(光环,宠物,辟邪玉)来填写数值
n = 0  # 误差
binary_de()
print()
print(f'Z={z:.35f}', '科学计数', z)
print('----------------------------------------------------')