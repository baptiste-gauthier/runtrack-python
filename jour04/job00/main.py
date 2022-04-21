# recursité de 4 = 1 * 2 * 3 * 4 = 24
# recursité de 7 = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5 040

print('Veuillez entrer un nombre')

num = int(input())

def factorielle(x):
    if x == 0:
        return 1

    return x * factorielle(x-1) 

print(factorielle(num))





