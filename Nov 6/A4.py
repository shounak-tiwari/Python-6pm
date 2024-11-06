no1 = 79 
no2 = 59

print("The binary of number 1  : ",bin(no1))

print("The binary of number 2 : ",bin(no2))

binary1 = no1

binary2 = no2

and_result = binary1 & binary2

or_result = binary1 | binary2

xor_result = binary1 ^ binary2

print(f"The AND of {bin(no1)} and {bin(no2)} result is : ",and_result,"(",bin(and_result),")")

print("The OR result is : ",or_result)

print("The XOR result is : ",xor_result)



"""
output : 

The binary of number 1  :  0b1001111
The binary of number 2 :  0b111011
The AND result is :  11
The OR result is :  127
The XOR result is :  116

"""
