import datetime
import random
import math

import summod

print(summod.sum(2,5))
print(summod.subtract(8,5))
print(summod.multiple(9,2))
print(summod.division(6,2))


print(max(1,2,3,9,4))
print(min(60,3,51,9,66))
print(abs(-7))
print(pow(3,4))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(6.8))
print(math.floor(5.2))
print(math.factorial(8))
print(math.sin(6))
print(math.cos(53))
print(math.tan(20))

print(random.randrange(2,9))
print(datetime.datetime.now())

x=datetime.datetime(2004,4,5)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%Y"))
