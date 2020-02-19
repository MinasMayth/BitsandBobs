import random

a = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 7]
print (a)

def lists():
    b = []
    for element in a:
        if element not in b:
            b.append(element)

    return b


def sets():
    b = [element for element in set(a)]

    return (b)


while True:
    usrinput = input ("lists or sets? ")

    if usrinput == ("lists"):
        print (lists())
    elif usrinput == ("sets"):
        print (sets())
    else:
        print ("False input.")

    
