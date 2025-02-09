def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            # return can be used here as well, eliminating the need for an else clause:
            # return x
            # This can be further refined by not declaring a variable and simply returning:
            # return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        
main()