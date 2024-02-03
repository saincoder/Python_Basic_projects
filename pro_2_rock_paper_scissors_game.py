# Rock Paper Scissor game

import random

# item list
options_list = ['rock', 'paper', 'scissor']
while True:
    user_count = 0
    computer_count = 0

    user_choice = int(input(
        '''
        Game Start
        CLick 1 for play 
        CLick 2 for Exit / Close
        '''
    ))
    if user_choice == 1:
        for a in range(1, 6):
            user_input = int(input(
                '''
                1 Rock
                2 Scissor
                3 Paper
                '''
            ))
            if user_input == 1:
                u_choice = 'rock'
            elif user_input == 2:
                u_choice = 'paper'
            elif user_input == 3:
                u_choice = 'scissor'
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue

            computer_choice = random.choice(options_list)
            if u_choice == computer_choice:
                print(f'Your choice: {u_choice}')
                print(f'Computer choice: {computer_choice}')
                print("It's a tie!")
                user_count = user_count + 1
                computer_count = computer_count + 1

            elif (u_choice == "rock" and computer_choice == "scissor") or (
                    u_choice == "paper" and computer_choice == "rock") or (
                    u_choice == "scissor" and computer_choice == 'paper'):
                print(f'Your choice: {u_choice}')
                print(f'Computer choice: {computer_choice}')
                print('You Win!')
                user_count = user_count + 1
            else:
                print(f'Your choice: {u_choice}')
                print(f'Computer choice: {computer_choice}')
                print('Computer Win!')
                computer_count = computer_count + 1

        # score
        if user_count == computer_count:
            print("Final Game Draw")
            print(f"Your Points: {user_count}")
            print(f"Computer Points: {computer_count}")
        elif user_count > computer_count:
            print("Final You win the game")
            print(f"Your Points: {user_count}")
            print(f"Computer Points: {computer_count}")
        else:
            print("Final Computer win the game")
            print(f"Your Points: {user_count}")
            print(f"Computer Points: {computer_count}")
    else:
        break
