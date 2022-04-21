
print('Veuillez entrer un nombre')

num = int(input())

def dames(x, n):

    if(n == x):
        return 1
    else:
        print('O' * x)
        dames(x, n + 1)

dames(num , 0)    