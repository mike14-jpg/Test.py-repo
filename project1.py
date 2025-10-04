#quiz game

print("Welcome to my computer quiz")
# user input
playing = input("Do yo want to play:  ")

if playing.lower() != "yes":
    quit()
print("okay! let's play ✌️")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("your correct gang")
    score += 1
else:
    print("go back to grade 1") 

answer = input("What colour is the sky during day time? ")
if answer.lower() == "blue":
    print("your correct gang🐺")
    score += 1
else:
    print("go back to grade 1") 

answer = input("What colour do get when you mix white and black? ")
if answer.lower() == "grey":
    print("your correct gang🐺") 
    score += 1
else:
    print("go back to grade 1 ") 

answer = input("Who is the G.O.A.T of football? ")
if answer.lower() == "messi":
    print("your correct gang🐺")
    score += 1
else:
    print("go back to grade 1 ") 

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
     print("your correct gang🐺")
     score += 1   
else:
    print("go back to grade 1 ") 
    
print(f"you got {score} questions correct ")
print(f"you got {(score/5) * 100} % ")



 