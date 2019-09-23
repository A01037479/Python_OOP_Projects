import random


class Mini_games:
    @staticmethod
    def rock_paper_scissors(pet):
        options = ["Rock", "Paper", "Scissors"]
        print('Let\'s play some rock, paper and scissors!')
        pet_play = options[random.randint(0, 2)]
        player_play = options[int(input("Rock, Paper, Scissors?\n"
                                        " 1. Rock\n 2. Paper\n 3. Scissors\n  ")) - 1]
        if player_play == pet_play:
            print("Tie!")
        elif player_play == "Rock":
            if pet_play == "Paper":
                print("You lose!", pet_play, "covers", player_play)
            else:
                print("Ok..You win..", player_play, "smashes", pet_play)
        elif player_play == "Paper":
            if pet_play == "Scissors":
                print("You lose!", pet_play, "cut", player_play)
            else:
                print("Ok..You win..", player_play, "covers", pet_play)
        elif player_play == "Scissors":
            if pet_play == "Rock":
                print("You lose!", pet_play, "smashes", player_play)
            else:
                print("Ok..You win..", player_play, "cut", pet_play)
        else:
            print("That's not a valid play!")
