list1 = [1,2,3,4]
list2 = [5,6,7,8]

# result = [(x,y) for x in list1 for y in list2]

# print(result)

result =[]

for x in list1:
    for y in list2:
        result.append([(x,y)])

print(result)
