li = [[],[]]
counter = 1
lenth = int(input("How many Element?: "))
while counter <= lenth:
    x = input("Enter A value: ")
    counter+=1
    if x.isnumeric() == True:
        li[0].append(x)
    else:
        li[1].append(x)
print(li)
