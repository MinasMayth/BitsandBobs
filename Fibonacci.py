def fib_sequence ():
    num = int (input ("How many fibonacci sequence numbers do you want? "))

    if num == 0:
        fibonnacilist = []
    elif num == 1:
        fibonnacilist = [1]
    elif num == 2:
        fibonnacilist = [1,1]
    elif num > 2:
        num = num - 2
        fibonnacilist = [1,1]
        for x in range(0,num):
            nextnumber = fibonnacilist [int(len(fibonnacilist) - 2)] + fibonnacilist [int(len(fibonnacilist) -1)]
            fibonnacilist.append (nextnumber)
    else:
        print ("invalid input")
        fibonnacilist = []
    return fibonnacilist

while True:
    print(fib_sequence())
