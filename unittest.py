# import unittest

# def number(lines):
#     return [f'{i+1}: {lines[i]}' for i in range(len(lines))]
# print(number(["y", "l", "m", "p"]))



mylist = [1,2,3,4,5,6]
evenNumbers = []
[evenNumbers.append(num) for num in mylist if num % 2 == 0]
print(evenNumbers)

for num in mylist:
    if num % 2 == 0:
        evenNumbers.append(num)
print(evenNumbers)

