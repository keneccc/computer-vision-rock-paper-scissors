# %% 
import random 
rps_list=["rock", "paper","scissors"]
computer_input= random.choice(rps_list)
game_input=input("Go!")




def play():
    def get_computer_choice():
        print(computer_input )

    def get_user_choice():
        game_input
        print(game_input)

    def get_winner():
        get_computer_choice()
        get_user_choice() 
        if game_input== computer_input:
            print("Tie")
        elif game_input == "rock" and computer_input=="scissors":
            print("Winner!")
        elif game_input == "scissors" and computer_input=="paper":
            print("Winner!")
        elif game_input== "paper" and computer_input=="rock":
            print("Winner!")
        else:
            print("LOSER")
    get_winner()
    






    
    

