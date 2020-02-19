a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []
for element in a:
    if int (element) in b and int (element) not in x:
        x.append(element)

print (x)
