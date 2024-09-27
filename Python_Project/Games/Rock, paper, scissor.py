import random


choices = ["Rock", "Paper", "Scissor"]
computer = random.choice(choices)

youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissor): ")

youDict = {"r" : "Rock", "s":"Scissor" , "p": "Paper"}

you = youDict[youstr]

print(f"Computer choise {computer} and You choise  {you}")

if(computer == you):
    print("Its a draw")
    
else:
    if(computer == "Rock" and you == "Paper"):
        print("You win!!!")
        
    elif(computer == "Rock" and you == "Scissor"):
        print("You Lose!!!")
            
    elif(computer == "Scissor" and you == "Rock"):
        print("You win!!!")
        
    elif(computer == "Scissor" and you == "Paper"):
        print("You Lose!!!")  
        
    elif(computer == "Paper" and you == "Scissor"):
        print("You win!!!")
        
    elif(computer == "Paper" and you == "Rock"):
        print("You Lose!!!")    
    else :
        print("Somethink Want wrong")