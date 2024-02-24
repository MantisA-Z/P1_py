import random

game = 'yes'
moves = ['rock', 'paper', 'scissors']
score = {'wins' : 0, 'loose' : 0, 'ties' : 0}

def play_game():
    computer = random.choice(moves)
    player_choice = input("Enter your coice (rock, paper, scissors): ").lower()
    while player_choice not in moves:
        print("Invalid, please type a valid choice.")
        player_choice = input("Enter your coice (rock, paper, scissors): ").lower()


    if computer == 'rock':
        if player_choice == 'rock':
            print('Tie')
            score['ties'] += 1
        elif player_choice == 'scissors':
            print('You loose')
            score['loose'] += 1
        elif player_choice == 'paper':
            print('You win')
            score['wins'] += 1
    if computer == 'scissors':
        if player_choice == 'scissors':
            print('Tie')
            score['ties'] += 1
        elif player_choice == 'rock':
            print('You loose')
            score['loose'] += 1
        elif player_choice == 'rock':
            print('You win')
            score['wins'] += 1
    if computer == 'paper':
        if player_choice == 'paper':
            print('Tie')
            score['ties'] += 1
        elif player_choice == 'rock':
            print('You loose')
            score['loose'] += 1
        elif player_choice == 'scissors':
            print('You win')
            score['wins'] += 1
    print(f'Wins: {score['wins']} \nLosses: {score['loose']} \nTies: {score['ties']}')
    return input('Do you want to play again? (Yes/No): ').lower()

try:
    while game == 'yes' or game == 'y':
        game = play_game()
        print('-' * 180)
    print(f'Thank you for playing! your score is: \nWins: {score['wins']} \nLosses: {score['loose']} \nTies: {score['ties']}')
except KeyboardInterrupt:
    print('\nGoodbye!')
