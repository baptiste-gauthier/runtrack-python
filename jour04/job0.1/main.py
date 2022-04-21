print('Veuillez entrer un nombre')

num = int(input())

def puissance(x, n):
    if (n==0):
        return(1)

    resultat = x * puissance(x, n - 1)
    return (resultat)

print(puissance(2, num))