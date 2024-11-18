lst = [] 
for x in range(2):
    obj = "listobj"
    obj =  obj + str(x)
    obj = list()
    while True:
        name = input('enter the items : ')
        if name =='' or name ==' ':
            break
        obj.append(name)
    lst.append(obj)
print(lst)