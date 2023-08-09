# Practice sheet
print ("*must contain 3 numbers, no spaces, and less than 15 character*")

Username = input("Enter a username: ")

if len(Username) > 15:
    print("Your username can't be more than 15 character!")
elif not Username.find(" ") == -1:
    print ("Your username can't have spaces!")
elif Username.isalpha() > 3:
    print ("Your username needs to have 3 numbers!")
else:
    print(f"Welcome {Username}")
