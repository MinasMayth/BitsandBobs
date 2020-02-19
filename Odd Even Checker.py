#File Checking for if a number is odd or even

#This first asks for the number, which is given by the user
Num = int ( input ("Hi! Give me a number, and I'll tell you if it's odd or even! "))

#Divides the number by 2. An even number will be whole, will an odd number will result in a float. This can be used for checking.
Result = Num / 2

#Checks if the number is divisible by four
Div_by_four = Num / 4

#3 steps. If Num is divisible by four, first message will print (regardless of it being even or odd), then, if the number is not divisble by four, but even, second message will print.
#Finally, if both previous conditions are false, the final message will play
if int(Div_by_four) == float (Div_by_four):
    print ("Your number is not only even, but also a multiple of four!")
elif int (Result) == float (Result):
    print ("Your number is even!")
else:
    print ("Your number is odd!")

#Extra! Division checker

print ("You're going to now give me two numbers. I will then tell you if the first number is divisble by the second number!")

nombre = int (input ("Give me the first number (The one that will be divided): "))

check = int (input ("Give me the second number (The one that will divide by): "))

div = nombre / check

if int (div) == float (div):
    print ("The first number is divisible by the second number!")
else:
    print ("The first number is NOT divisible by the second number!")
