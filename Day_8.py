# >>> Normal Function >>>

def greet():
    print('')
    print("Hello  :(")
    print("We have nothing to talk about so.....")
    print("Bye  :)")
    print('')

greet()



def greet_with_name(name):
    print("")
    print(f"Hello {name} :(")
    print("We have nothing to talk about so.....")
    print(f"Bye {name} :)")
    print('')

greet_with_name(input("What is your name? \n"))

def greet_with_name_and_where(name, location):
    print("")
    print(f"Hello {name} :(")
    print('I know where you live.....')
    print(f"You live in {location} :)")
    print('')

greet_with_name_and_where(name=input("What is your name? \n"),location=input("Where do you live? \n"))



