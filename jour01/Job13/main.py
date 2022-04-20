from array import array

x = 0
array = []

while x < 5:
    print('Veuillez entrer un nombre entier')
    num = int(input())
    array.append(num)
    x = x + 1

array.sort()

print(array)
