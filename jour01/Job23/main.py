i = 0 
y = 10

while i < 10:
    if(i == 9):
        print(y * " " , "/", i * 2 * "_", "\\")
    else:    
        print(y * " " , "/", i * 2 * " ", "\\")

    i = i + 1
    y = y - 1
