import random
elements = ["rock", "paper", "scissors", "lizard", "spock"]
another_view_of_elements = "(rock paper scissors lizard spock)?"

def choose_element():
    player_choice = input(f"Make your choise {another_view_of_elements}\n>>>  ").lower()
    system_choice = random.choice(elements)
    if player_choice not in elements:
        print(f"invalid input {player_choice}")
        choose_element()
    else:
        if player_choice == system_choice:
            print(f"Player: {player_choice}\nComputer: {system_choice}\nDraw")

        if player_choice == "scissors":
            if system_choice == "spock" or system_choice == "rock":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nComputer WIN!")
            elif system_choice == "paper" or system_choice == "lizard":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nPlayer WIN!")

        elif player_choice == "paper":
            if system_choice == "scissors" or system_choice == "lizard":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nComputer WIN!")
            elif system_choice == "rock" or system_choice == "spock":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nPlayer WIN!")

        elif player_choice == "rock":
            if system_choice == "paper" or system_choice == "spock":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nComputer WIN!")
            elif system_choice == "scissors" or system_choice == "lizard":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nPlayer WIN!")

        elif player_choice == "lizard":
            if system_choice == "rock" or system_choice == "scissors":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nComputer WIN!")
            elif system_choice == "paper" or system_choice == "spock":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nPlayer WIN!")

        elif player_choice == "spock":
            if system_choice == "paper" or system_choice == "lizard":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nComputer WIN!")
            elif system_choice == "scissors" or system_choice == "rock":
                print(f"Player: {player_choice}\nComputer: {system_choice}\nPlayer WIN!")

        def next_game():
            next_play = input("Repeat (Y/N)?\n").lower()
            if next_play == "y" or next_play == "yes":
                choose_element()
            elif next_play == "n" or next_play == "no":
                exit()
            else:
                print(f"invalid input {next_play}\nDo you want to repeat the game?")
                next_game()
        next_game()

choose_element()