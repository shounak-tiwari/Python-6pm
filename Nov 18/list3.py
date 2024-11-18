lst = [1,2,3,4,6,6,1,2,3]
result = []
for x in lst :
    if x not in result:
        result.append(x)
lst = result.copy()
print(result)
