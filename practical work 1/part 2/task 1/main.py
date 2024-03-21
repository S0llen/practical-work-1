import math

u = 0 
v = 0

a = u + v
s = 2 * u

up = math.sin(a) + 3 * math.exp(-s)
down = 1 + math.tan(a) ** 2

res = up / down

print(res)