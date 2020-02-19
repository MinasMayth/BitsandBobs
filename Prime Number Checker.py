def get_number(prompt):
    return int(input (prompt))

def prime_checker(number):
    a = []
    x = range(2, number)

    for element in x:
        divisible = number / int (element)
        if int (divisible) == float(divisible):
            a.append(element)

    if number == int ("1"):
        print ("1 is not a prime number.")
    elif not a:
        print ("Your number is a prime number!")
    else:
        print ("Your number is not a primber number! The divisors of " + str (number) + " are: ")
        print (a)
    


while True:
    prime_checker (get_number("Enter a postive integer to check. Ctl-C to exit. "))
