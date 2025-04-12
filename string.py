# str = "App dev using python!! 2025"
 # print(str[0])

# upr,lwr,num,spl = 0,0,0,0
# for i in range(len(str)):
#     if(str[i] >= 'A' and str[i] <= 'Z'):
#         upr +=1
#     elif(str[i] >= 'a' and str[i] <= 'z'):
#         lwr +=1
#     elif(str[i] >= '0' and str[i] <= '9'):
#         num +=1
#     else:
#         spl +=1

# print("Upper case: ",upr)
# print("Lower case: ",lwr)
# print("Number: ",num)
# print("Special char: ",spl)


str1 = "Nitin Prajapat TYBCA"
count = 0


for i in str1:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        count +=1


print("Vowels in the string: ",count)
    