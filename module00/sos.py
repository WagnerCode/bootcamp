import re
import sys

k = 1
arr = ''
if len(sys.argv) > 1:
    while len(sys.argv) > k:
        arr += sys.argv[k]
        if k == len(sys.argv) - 1:
            break
        arr += " "
        k += 1
    i = 0
    print(arr)
    arr = arr.upper()
    arr2 = []
    for i in range(len(arr)):
        if arr[i] == 'A':
            arr2.append('.-')
        elif arr[i] == 'B':
            arr2.append('-...')
        elif arr[i] == 'C':
            arr2.append('-.-.')
        elif arr[i] == 'D':
            arr2.append('-..')
        elif arr[i] == 'E':
            arr2.append('.')
        elif arr[i] == 'F':
            arr2.append('..-.')
        elif arr[i] == 'G':
            arr2.append('--.')
        elif arr[i] == 'H':
            arr2.append('....')
        elif arr[i] == 'I':
            arr2.append('..')
        elif arr[i] == 'J':
            arr2.append('.---')
        elif arr[i] == 'K':
            arr2.append('-.-')
        elif arr[i] == 'L':
            arr2.append('.-..')
        elif arr[i] == 'M':
            arr2.append('--')
        elif arr[i] == 'N':
            arr2.append('-.')
        elif arr[i] == 'O':
            arr2.append('---')
        elif arr[i] == 'P':
            arr2.append('.--.')
        elif arr[i] == 'Q':
            arr2.append('--.-')
        elif arr[i] == 'R':
            arr2.append('.-.')
        elif arr[i] == 'S':
            arr2.append('...')
        elif arr[i] == 'T':
            arr2.append('-')
        elif arr[i] == 'U':
            arr2.append('..-')
        elif arr[i] == 'V':
            arr2.append('...-')
        elif arr[i] == 'W':
            arr2.append('.--')
        elif arr[i] == 'X':
            arr2.append('-..-')
        elif arr[i] == 'Y':
            arr2.append('-.--')
        elif arr[i] == 'Z':
            arr2.append('--..')
        elif arr[i] == 'B':
            arr2.append('-...')
        elif arr[i] == ' ':
            arr2.append(' / ')
        i += 1
    output = ''
    for i in range(len(arr2)):
        output += arr2[i]
    print(output)


else:
    print ("")
