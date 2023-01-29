# Rockk , Paperr , Scissorss! 
import random
def play():
        Player1 = input("rock , paper , scissors\n").lower()      
        print("you chose" , Player1)              

        #computer input
        choices = ["rock" , "paper" , "scissors"]
        Enemy1 = random.choice(choices)
        print("Enemy1 chose" , Enemy1)                                     

        #choices loop       
        if Player1 == "rock":       
            if Enemy1 == "rock":
                print("tie , try again!")       
            elif Enemy1 == "paper":
                print("Enemy1 wins!")
            elif Enemy1 == "scissors":
                print("Player1 wins!")                   

        if Player1 == "paper":
            if Enemy1 == "paper":
                print("tie , try again!")
            elif Enemy1 == "scissors":
                print("Enemy1 wins!")  
            elif Enemy1 == "rock":
                print("Player1 wins!")

        if Player1 == "scissors":
            if Enemy1 == "scissors":
                print("tie , try again!")
            elif Enemy1 == "rock":
                print("Enemy1 wins!") 
            elif Enemy1 == "paper": 
                print("Player1 wins!")       

#play again 
def main():
    play()
    while True:
        user = input("do you want to play again?"+ "y/n?\n").lower()
        if user == "y":
            play()
        else:
            break    
main()
