phrase1 = str(input('Veuillez entrer une chaine de caractère'))
phrase2 = str(input('Veuillez entrer une deuxième chaine de caractère'))

if phrase1.islower() and phrase2.islower():
    if phrase1 == phrase2:
        print(1)
    else:
        print(2)    
else:
    print('Vos chaines de caractères doivent être en minuscule')    
