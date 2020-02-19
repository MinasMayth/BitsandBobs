number = int(input ("Give me a number! "))

a = []
x = range(1, number)

for element in x:
    divisible = number / int (element)
    if int (divisible) == float(divisible):
        a.append(element)

print ("The divisors of " + str (number) + " are: ")
print (a)
