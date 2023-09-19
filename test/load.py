from copy import deepcopy

a = {
    1: [1, [1, 2]]
}

b = deepcopy(a)

print(id(a[1][1]), id(b[1][1]))

a[1].append(3)
print(id(a[1]), id(b[1]))

print(b)
