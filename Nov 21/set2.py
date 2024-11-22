s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,4,3}

# result = s1 & s2
# print(result)


# result = s1.intersection(s2)
# print(result)


result = s1 ^ s2
print("result of ^ is :",result)

result = s1 | s2 
print("result of |  is : ",result)


result = s1.union(s2)
print("Union : ",result)


result = s1.symmetric_difference(s2)
print("symmertic differecne" , result)

