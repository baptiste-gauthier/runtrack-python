import re

# Ouvrir le fichier en lecture seule
file = open('domains.xml', "r")
# utilisez readline() pour lire la première ligne
line = file.readline()
count = 0
while line:

    if re.search( '(\.)[a-z]{1,4}' ,line):
        count = count + 1 
    line = file.readline()
file.close()

print(count)
   
    # a = re.search('.com',line)
    # print(a)


 


