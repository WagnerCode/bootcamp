import sys
import re
if (len(sys.argv) > 1) & (len(sys.argv) < 4):
    if (sys.argv[1]).isascii() & (sys.argv[2].isnumeric()):
        punctuation_minus = (re.sub(r'[.,!?;:—-]', '', sys.argv[1]))
        arr = punctuation_minus.split(' ')
        arr2 = []
        for i in range(len(arr)):
            if len(arr[i]) > int(sys.argv[2]):
                 arr2.append(arr[i])

        print(arr2)
    else:
        print("ERROR")
else:
    print("ERROR")
