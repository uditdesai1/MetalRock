secret_word = 'Udit'


Guess_allowed = 3
for i in range(3):
    user_input = input("Enter your guess :)")
    if user_input == secret_word :
        print('You Won !!, You are a smartie just like the game creator Udit Desai:)')
        break
    else:
        print(' You Lost :) You are a loser, Take a BIG "L" Ha Ha Ha ')



input('Enter to exit..')