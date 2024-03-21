import math

x = 0.4

deg = 3 * (x ** 2) + 4

res = math.exp(deg) - (abs(x) ** 3) + (math.log(x) ** 2)

print (res)