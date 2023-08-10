# --- Notes ---
# Getting stuck on the Space detection section, everything else seems to run fine as is and loops work ok.
# Number detection does not seem to always work but feels more of the fault of line 17 - 19.
#

print ("*must contain 3 numbers, no spaces, and less than 15 characters*")

Username = input("Enter a username: ")

if  len(Username) <= 0:
    print("You didn't enter anything!")
    name = input("Please type something this time: ")
    
while len(Username) > 15:
    print("Your username can't be more than 15 character!")
    name = input("Please enter a username: ")

while Username.find("") >= -1:
    print ("Your username can't have spaces!")
    name = input("Please enter a username: ")

while Username.isalpha() < 2:
    print ("Your username needs to have 3 numbers!")
    name = input("Please enter a username: ")

else:
    print(f"Welcome {Username}")
