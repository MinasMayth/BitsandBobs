import random

def password_generator():
    passwordlist = []
    actual_length = 0
    final_length = int (input ("How many characters long should the password be? "))

    while actual_length != final_length:
        
        option = random.randint(1,4)
        
        if option == 1:
            passwordlist.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
            actual_length = actual_length + 1
        elif option == 2:
            passwordlist.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            actual_length = actual_length + 1
        elif option == 3:
            passwordlist.append(str (random.randint(0,9)))
            actual_length = actual_length + 1
        elif option == 4:
            passwordlist.append(random.choice('!@#$%^&*()?'))
            actual_length = actual_length + 1

    password = "".join(passwordlist)
    return password

while True:
    print (password_generator())
