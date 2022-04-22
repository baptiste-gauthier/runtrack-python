print('Veuillez entrer une chaine de caractere')

string = str(input()) 

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(string)