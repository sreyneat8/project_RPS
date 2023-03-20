import random
user = int(input('Please enter a choice:'))# rock, paper, scissor
possible_action = [1,2,3]
computer_choice = random.choice(possible_action)
print(f'Your choice is:{user} and Computer choice is:{computer_choice}')

if user == computer_choice:
    print('You tie.')
elif user == 1:
    if computer_choice == 2:
        print('You lose')
    else:
        print('You win')
elif user == 2:
    if computer_choice == 3:
        print('You lose')
    else:
        print('You win')
elif user == 3:
    if computer_choice == 1:
        print('You lose')
    else:
        print('You win')
