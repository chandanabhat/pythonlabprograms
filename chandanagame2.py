numbers = [i+1 for i in range(100)]
numbers = numbers[::-1]
levels = [i for i in numbers[::-10]]
is_reversed = False

for level in levels:

    if is_reversed:
        for number in reversed(numbers[level-1:level+9]):
            print('{:4}'.format(number), end='')
    else:
        for number in numbers[level-1:level+9]:
            print('{:4}'.format(number), end='')

    is_reversed = not is_reversed
    print()