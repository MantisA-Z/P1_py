i = 0
text = f'Hello World!\n' * 5
while i <= 0:
    with open(f'file.txt{i}', 'w') as file:
        file.write(text)
    i += 1
    print(':)\n')
