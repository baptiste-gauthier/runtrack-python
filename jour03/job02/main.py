import re

print('Veuillez entrer un nombre entier')
num = input()

file = open('data.txt', "r")
# utilisez readline() pour lire la première ligne
line = file.readline()
count = 0
while line:
    if re.search('(\s)[a-z]{'+ num +'}(\s)' ,line): 
        count = count + 1 
    line = file.readline()
file.close()

print('Il y a', count , 'mots avec ' + num + ' caractères dans votre fichier')



