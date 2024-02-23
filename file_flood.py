i = 0
text = f'Hello World!\n' * 500
while i <= 1000:
    with open(f'file.txt{i}', 'w') as file:
        file.write(text)
    i += 1
    print(':)\n')
