import random


def guessing_game():
    rnd_number = random.randint(0, 100)
    user_number = rnd_number + 1
    print('Welcome to not too funny game, now we choose the number!')
    while rnd_number != user_number:
        user_input = input('What number has been chosen?\n')
        try:
            user_number = int(user_input)
            if user_number < rnd_number:
                print('Too low')
            elif user_number > rnd_number:
                print('Too high')
            else:
                print(f'{user_number} - BINGO!!!')
        except ValueError:
            print('ERROR: Not an INT number! Enter again!')


if __name__ == '__main__':
    guessing_game()
