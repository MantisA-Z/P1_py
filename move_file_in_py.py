import os

#variable (source) and (destinantion) not necessary you can directly change the src and dest while calling the function in the last line
source = 'test.txt'
destination = 'C:\\Users\\MANTIS\\OneDrive\\new'

#main function
def move_file(source, destination):
    try:
        if not os.path.exists(destination):
            os.replace(source, destination)
            print(source +'File was moved to ' + destination)
        else:
            print(f'There is already a file in {destination}')
    except FileNotFoundError:
        print(f'There is no file at {source}')

#Executing code
move_file(source, destination)
