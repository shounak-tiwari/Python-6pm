# import datetime

dob = input("enter dob in format of DD/MM/YYYY : ")

# # print(dob)


# day = 4
# month = 10
# year = 2000

# x = datetime.datetime(year,month,day)
# print(x)

# day = x.strftime("%A")
# print(day)






part = dob.partition('/')

day = part[0]

day = int(day)

year_month = part[2]

part = year_month.partition('/')
month = int(part[0])
year = int(part[2])


print(type(day),type(month),type(year))


import datetime

day_find = datetime.datetime(year,month,day)

print(day_find.strftime("%A"))

