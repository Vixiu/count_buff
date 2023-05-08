# importing library sympy
from sympy import symbols, Eq, solve

x, y, z = symbols('x,y,z')

eq1 = Eq((x + y + z+10), 16)

eq2 = Eq((x + y + z), 6)

eq3 = Eq((x + y + z+100), 160)

print(solve((eq1, eq2, eq3), (x, y, z)))
