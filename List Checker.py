#List Checker
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

number = int(input ("Give me a number! "))

for element in a:
    if int (element) < number:
        x.append(element)

print (x)
