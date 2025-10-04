import random

# rock paper scissors
user_Wins = 0
computer_Wins = 0

options = ["rock","paper","scissors"]


while True:
    user_input = input("Type Rock/paper/Scissors or Q to quit:  ").lower()
    if user_input == "q":
        quit()

    if user_input not  in options :
        continue
    random_number = random.randint(0,2)
    # rock : 0 , paper : 1 , scissors : 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick +".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_Wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_Wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_Wins += 1
    else:
        print("you lost!")
        computer_Wins += 1    
     
print(f"user win count is {user_Wins} times")    
print(f"computer Win count is {computer_Wins} times")
print("Goodbye✌️")