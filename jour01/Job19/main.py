print('Veuillez entrer une hauteur')
height = int(input())
print('Veuillez entrer une largeur')
width = int(input())

for i in range(height):
    if(i == height - 1 or i == 0):
        print('|' , '-' * width , '|') 
    else:
        print('|' ,' ' * width, '|')
