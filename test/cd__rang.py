cd = 40.0

# x = 1 - 0.05
x = 1- 0.05
d = 0.8
#############################
y = d * 0.9

z = 1 + 0.15 + 0.3 + 0.5
#################
f_y = 0.93 * 0.93
f_x = 0.95*0.95*0.95

print("勇气", cd * x * (y * f_y) / z)
print("新生", cd * x * (y * f_x) / z)

print(600 * 1.06 * 1.06 * 1.06 * 1.15 * 1.15 * 1.1, 1020)  # 范围计算
