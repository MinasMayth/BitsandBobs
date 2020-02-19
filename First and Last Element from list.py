import random
    

def list_checker ():
    a = random.sample(range(1,30), 12)
    x = []
    print (a)
    x.append (a [0])
    x.append (a [len (a) - 1])
    print (x)
    print (len(x))
    input ()
    
while True:
    list_checker()
