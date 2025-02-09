# from curses.ascii import isdigit


name = input("Enter your name: ")
length = len(name)

# This will only work with names having <=1 blank space
# if name.find(" "):
#     length -= 1

# print(f"Your name contains {length} letters")

if length > 12:
    print("Username must be less than 12 characters")
elif not name.find(" ") == -1:
    print("Username must not contain spaces")
elif not name.isalpha():
    print("Username must not contain digits")
else:
    print(f"Welcome {name}")