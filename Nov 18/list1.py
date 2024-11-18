lst = []

total = ["lst1","lst2","lst3","lst4","lst5"]

for x in total:
    x = list()

    while True:
        name = input('enter the items : ')
        if name =='' or name ==' ':
            break
        x.append(name)
    lst.append(x)

print(lst)
