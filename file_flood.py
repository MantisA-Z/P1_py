i = 0
text = f'Hello World!\n' * 100000
flag = True
while flag == True:
    with open(f'file.txt{i}', 'w') as file:
        file.write(text)
    print(':)\n')
    i += 1
