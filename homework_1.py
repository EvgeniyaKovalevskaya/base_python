#Task 1
month = input('What month is it?')
if (int(month) == 0 or int(month) > 12):
    print("It must be since 1 till 12. Try again")
else:
    print(f"Your month is {month}")


#Task 2
name = input("What is your name?")
last_name = input("What is your last name?")
age = input("How old are you?")

if (int(age) < 18):
    print(f"Your name is {name}. Your last name is {last_name}. You are {age}, this web-site is not for you. Good bye")

else:
    print(f"Your name is {name}. Your last name is {last_name}. You are {age}, it is ok. Welcome to uor web-site")