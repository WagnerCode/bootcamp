import sys
if (len(sys.argv) > 1) & (len(sys.argv) < 4):
    if (sys.argv[1]).isnumeric() & (sys.argv[2].isnumeric()):
        A = int(sys.argv[1])
        B = int(sys.argv[2])

        print("Sum: \t\t", A + B)
        print("Difference: \t", A - B)
        print("Product: \t", A * B)
        if B == 0:
            print("Quotient: \t Error")
            print("Remainder: \t Error")
        else:
            print("Quotient: \t", A / B)
            print("Remainder: \t", A % B)
    else:
        print("AssertionError: only integers")
elif (len(sys.argv) > 3):
    print("AssertionError: too many arguments")
else:
    print("Usage: python operations.py <number1> <number2>")