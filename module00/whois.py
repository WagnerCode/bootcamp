import sys


if (len(sys.argv) > 1) & (len(sys.argv) < 3):
    if (sys.argv[1]).isnumeric():
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("argument is not an integer")
else:
    print("more than one argument is provided")