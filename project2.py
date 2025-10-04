import random

# number guesser
top_of_number = input("Type a number: ")

if top_of_number.isdigit():
    top_of_number = int(top_of_number)

    if top_of_number <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a whole number .")
    quit()

random_number = random.randint(0,top_of_number)

score = 0

while True:
    score += 1 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
                
    else:
      print("Please type a number next time .")
      continue

    if user_guess == random_number:
        print("you are correct! ")
        break
    else:        
        if user_guess > random_number:
            print("you are above the number")
        else:
            print("you are below the number!")

print(f"you got it in {score} gueses")
