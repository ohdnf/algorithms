import sys
input = lambda: sys.stdin.readline()

string = input()
number = ''
for c in string:
    if c.isdigit():
        number += c

number = int(number)
aliquots = [num for num in range(1, number+1) if number % num == 0]
print(number)
print(len(aliquots))