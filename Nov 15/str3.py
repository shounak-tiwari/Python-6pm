Name = "harshal"

Name = list(Name)

flag = 0

for x in Name:
    flag = Name.count(x)
    print(x,"==>",flag)
    while flag !=0:
        Name.remove(x)
        flag-=1
    
    
