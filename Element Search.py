def normal_search():
    a = [1, 3, 5, 30, 42, 43, 500]
    number = int (input("Type a number to see if it is in the list: "))

    result = number in a
    return result

def binary_search():
    a = [1, 3, 5, 30, 42, 43, 500]
    b = []
    number = int (input("Type a number to see if it is in the list: "))
    result = False

    while True:
        if number != a[int((len(a)-1)/2)] and len(a) == 1:
            result = False
            return result
        if number > a[int((len(a)-1)/2)]:
            b += a[int(len(a)/2):]
        elif number < a[int((len(a)-1)/2)]:
            b += a[:int(len(a)/2)]
        elif number == a[int((len(a)-1)/2)]:
            result = True
            return result
        else:
            print ("Error")



        #print (type (a[int(len(a)/2)]))
        #print (type (b[int(len(b)/2)]))
        #print (a)
        #print (b)
        
        a = []     
        
        if number != b[int((len(b)-1)/2)] and len(b) == 1:
            result = False
            return result
        elif number > b[int((len(b)-1)/2)]:
            a += b[int(len(b)/2):]
        elif number < b[int((len(b)-1)/2)]:
            a += b[:int(len(a)/2)]
        elif number == b[int((len(b)-1)/2)]:
            result = True
            return result
        else:
            print ("Error")

        #print (a)
        b = []

while True:
    print (binary_search())
