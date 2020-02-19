import random

def Max_of_Three():
    x = random.randint(1,99)
    y = random.randint(1,99)
    z = random.randint(1,99)

    print ("Number 1: " + str (x))
    print ("Number 2: " + str (y))
    print ("Number 3: " + str (z))

    if x > y and x > z:
        return ("Largest number is " + str(x) +".")
    elif y > x and y > z:
        return ("Largest number is " + str(y) +".")
    elif z > x and z > y:
        return ("Largest number is " + str(z) +".")
    elif x == y and x > z:
        return ("Largest numbers are " + str(x) + " and " + str(y) + ".")
    elif x == z and x > y:
        return ("Largest numbers are " + str(x) + " and " + str(z) + ".")
    elif y == z and y > x:
        return ("Largest numbers are " + str(z) + " and " + str(y) + ".")
    else:
        return ("Something went wrong.")

if __name__ == "__main__":
    while True:
        print (Max_of_Three())
        input()
