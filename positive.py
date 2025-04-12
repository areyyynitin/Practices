
def func(num):
    if(num > 0):
        print(num , "is Positive number")
    elif(num < 0):
        print(num,"is Negative number")
    else:
        print(num , "is zero")

user = int(input("Enter a number:"))
func(user)
