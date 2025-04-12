inputString = "string and string functions"

resultstr =""

print("Original string: ",inputString)

for char in inputString.split(' '):
    if char not in resultstr:
        resultstr = resultstr + " " + char


print("String after removing duplicates: ",resultstr)

# input_string = "string and string functions"

# result_str=""

# print("Original String :",input_string)

# for char in input_string.split(' '):
#     if char not in result_str:
#         result_str+=' '+char

# print("string as duplicate removed : ",result_str)