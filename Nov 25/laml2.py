import functools

lst = [1,2,3,4,5,6,7,8,9,10]

# result = functools.reduce(lambda x,y:x+y,lst)

# result = functools.reduce(lambda x,y: x if y%2!=0 else x+y ,lst)


result = functools.reduce(lambda x, y: x + y if y % 2 == 0 else x, lst)
print(result) 