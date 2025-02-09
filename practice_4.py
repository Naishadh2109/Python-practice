name = input("Enter your name: ")

# This is the same as Switch case in C or Java
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Newt":
        print("Hufflepuff")
    case _:
        print("Who?")