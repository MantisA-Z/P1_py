import time

#main function
def count_down(duration):
    for i in range(duration, 0, -1):
        seconds = duration % 60
        mins = int(duration / 60) % 60
        hrs = int(duration / 3600)
        print(f'{hrs:02}:{mins:02}:{seconds:02}')
        time.sleep(1)
        duration -= 1

#Taking time from user
try:
    duration = input('Enter the time: ') #example: 12:03:02 (Enter a valid time)
    duration = duration.split(':')
    duration = int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2])
    count_down(duration)#Calling function after taking a specific time
except TypeError:
    print('please enter a valid time')
except ValueError:
    print('please enter a valid time')

