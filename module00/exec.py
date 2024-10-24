import sys

k = 1
arr = ''
if len(sys.argv) > 1:
    while len(sys.argv) > k:
        arr += sys.argv[k]
        arr += " "
        k += 1
    arr = arr.rstrip()

    beginning = len(arr) - 1
    arr2 = []
    for letter in arr:
        arr2.append(arr[beginning])
        beginning -= 1
    i = 0
    for letter in arr2:
        if i == len(arr) - 1:
            print(arr2[i])
            break
        print(arr2[i], end="")
        i += 1
else:
    print ("")

