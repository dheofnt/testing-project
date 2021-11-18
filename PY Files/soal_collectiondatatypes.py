numbers = [41, 5, 1, 3, 89, 32]
maxVal = numbers[0]
minVal = numbers[0]

for num in numbers :
    if num < minVal :
        minVal = num
    if num > maxVal :
        maxval = num

print('Numbers = {}'.format(numbers))
print('Minimum Value = {}'.format(minVal))
print('Maximum Value = {}'.format(maxVal))

