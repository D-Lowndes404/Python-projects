from cryptography.fernet import Fernet

'''
def write_key():
  key = Fernet.generate_key()
  with open('key.key', "wb") as key_file:
    key_file.write(key)
'''
## Key write function quoted out until issue can be resolved.
def load_key():
  file = open ("key.key", "rb")
  '''
  Issues ^^^^^^^^^^^^^^^^^^^^^^,
  Line is having issues with callback dictation.
  initialize does not develop encrypted key for auth display
  '''
  key = file.read()
  file.close()
  return key
## Fernet encrpytion key must be left above the input defenitions left below

Master_Pwd = input("Password?  ")
key = load_key() + Master_Pwd.encode()
'''
line 23 has issues due to line 10 not being able to find the callback encryption key .
issues with this should clear once the callback function has been solved.
'''
fer = Fernet(key)
## view defined section
## !!! function has not been determined to work due to above issues !!! ##
def view():
  with open("passwords.txt","r") as f:
    for line in f.readlines():
      data = line.rstrip()
      user, passw = data.split('|')
      print("User:", user, "| Password:", 
            fer.decrypt(passw.encode()).decode())

## add defined section
## !!! function has not been determined to work due to above issues !!! ###

def add():
  name = input('account name: ')
  pwd = input('Password: ')
  with open("passwords.txt","a") as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()) +"\n")


## action request below ##
while True:
    mode = input("Add or view?(or q to quit.)  ").lower().strip()
    if mode =="q":
     break
    elif mode == "view":
     view()
    elif mode == "add":
     add()
    else:
     print("Invalid mode.")
     continue