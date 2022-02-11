import random

options = ['ROCK', 'PAPER', 'SCISSORS']

def start():
    print("Let's play Rock, Paper and Scissors!")
    print()
    user_choice = input('What do you choose? rock, paper or scissors? ')
    user_choice = user_choice.upper()
    cpu = random.choice(options)
    return user_choice, cpu

def results(user,cpu):
    if user == cpu:
        print()
        print("It's a draw!")

    elif user == 'ROCK' and cpu == 'SCISSORS':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Congratulations!! you won!')

    elif user == 'ROCK' and cpu == 'PAPER':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Oh! It looks like you lost :( ')
        print('Good luck next time :)')

    elif user == 'SCISSORS' and cpu == 'PAPER':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Congratulations!! you won!')

    elif user == 'SCISSORS' and cpu == 'ROCK':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Oh! It looks like you lost :( ')
        print('Good luck next time :)')

    elif user == 'PAPER' and cpu == 'ROCK':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Congratulations!! you won!')

    elif user == 'PAPER' and cpu == 'SCISSORS':
        print(f"You've chosen {user} and the computer chose {cpu}")
        print()
        print('Oh! It looks like you lost :( ')
        print('Good luck next time :)')

user, cpu = start()
results(user,cpu)