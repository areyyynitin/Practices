def defDivide(x,y):
    try:
        result = x/y
        print("RESULT:",result)

    except ZeroDivisionError:
        print("Divide by zero isn't allowed")




# defDivide(78,1)


def get_Input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Invalid input.")

num = get_Input("Enter a number: ")
print("Your num:",num)



# def get_input(prompt):
#     try:
#         value = int(input(prompt))
#         return value
#     except ValueError:
#         print("Error : invalid input")


# num = get_input("input an integer")
# print("input value : ", num)