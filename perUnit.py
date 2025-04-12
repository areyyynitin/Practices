

user = input("Enter which  type of user you are [Business for 'B' , Household for 'H' , Industrial for 'I']:")
consumption = float(input("Enter the how much consumption you used in a month:"))

if user == "H":
    print("Your total bill is:", consumption * 2)
elif user == "B":
    print("You total bill is:" , consumption * 5)
elif user == "I" :
    print("You total bill is:", consumption * 10)
else:
    print("You are not a valid user")



