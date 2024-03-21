import math

x = 0.5

fst = ((x + 1) / (x + 2)) ** (1/3)

arc = math.asin(x**(1/2))

res = fst + arc

print (res)