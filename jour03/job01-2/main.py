file = open('data.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Total Words:', len(per_word))