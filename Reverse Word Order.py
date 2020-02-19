
def string_reverse():
    print ("Enter your sentence below, and I will reverse it!")
    userinput = str (input ())

    split_list = userinput.split()
    split_list = split_list [::-1]

    result = " ".join(split_list)

    return result

while True:
    print (string_reverse())
