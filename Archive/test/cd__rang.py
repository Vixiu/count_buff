cd = 40.0  # 初始CD
# 公共CD
X = 1 - 0.05  # 宠物称号单独加算CD
Y = 0.9 * 0.95 * 0.95 * 0.9
Z = 1 + 0.15 + 0.3 + 0.2 + 0.12
# 私有CD
yq_y = 0.8 * 0.93  # 勇气圣歌
xs_y = 0.8 * 0.85 * 0.95 * 0.95  # 新生圣歌

print(f'勇气圣歌{cd * 0.3}', cd * X * Y * yq_y / Z)
print(f'新生圣歌{cd * 0.3}', cd * X * Y * xs_y / Z)
print(50 * X * Y*0.8 / Z)
print('新生', 600 * 1.1 * 1.15 * 1.15 * 1.06 * 1.06, 1020)  # 范围计算
print('勇气', 600 * 1.1 * 1.15 * 1.15 * 1.15 * 1.06, 1020)  # 范围计算
