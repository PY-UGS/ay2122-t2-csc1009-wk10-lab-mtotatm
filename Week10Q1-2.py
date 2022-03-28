#Question1
def Question1Function():
    print("Hello Glasgow!")

#Question2
def Question2Function():
    x = 0
    y = 0

    while True:
        x = input("Enter the value for x :\n")
        try:
            val = int(x)
            print("You have enter: " + x)
            break
        except ValueError:
            print("x is not a number, please enter a number\n")

    while True:
        y = input("Enter the value for y :\n")
        try:
            val = int(y)
            print("You have enter: " + y)
            break
        except ValueError:
            print("y is not a number, please enter a number\n")

    avg = float(int(x) + int(y)) / 2
    print("The average of these 2 numbers: " + str(avg))


Question1Function()
Question2Function()