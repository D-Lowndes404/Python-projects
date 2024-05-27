import random

print('Need a password?')

response = input("Y/N?: ").strip().upper()

if response == "Y":
 chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890"
 number = input ("How many choices?:  ")
 number = int(number)
 length = input("How many characters?:  ")
 length = int(length)

 print('\nHere you go:')
 print("\n")
 for pwd in range(number):
    passwords = ""
    for c in range(length):
     passwords += random.choice(chars)
    print(passwords)
    print('\n')
else:
  print("Program doesnt nothing else. Ending.")
