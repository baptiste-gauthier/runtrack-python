x = 0
list_mark = []
new_list_mark = []

while x < 5:
    print('Veuillez entrer les 5 notes')
    num = int(input())
    list_mark.append(num)
    x = x + 1

for mark in list_mark:
    if(mark % 5 > 2 and mark > 40):
        while mark % 5 != 0:
            mark = mark + 1
        new_mark = mark
        new_list_mark.append(mark)
           
    else:
        new_list_mark.append(mark)

print("Anciennes notes : " , list_mark)
print("Voila vos nouvelles notes Luc ! " , new_list_mark) 



