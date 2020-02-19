import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

x = [element for element in set (a) if int (element) in b]
print (x)
