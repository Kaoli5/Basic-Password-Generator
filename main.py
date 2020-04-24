import random
import string

def again():
  question = input("Would you like to generate another one? (Y/N): ")
  if question == "y" or "Y":
    main_func()
  else:
    print("Goodbye.")
    exit()
 

def random_ascii(stringLength):
  characters = string.ascii_letters + string.digits + '&*-#$!^_=+@~'
  final = ''.join(random.choice(characters) for i in range (stringLength))
  print(final)
  f = open('random_pw.txt', 'w')
  f.write(final)
  f.close()
  again()
    
def main_func():
  how_many = int(input("How many characters?: "))
  random_ascii(how_many)

main_func()