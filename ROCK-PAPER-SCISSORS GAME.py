import random

print("\n\n ~~~~ Welcome to the Game of Rock - Paper - Scissor ~~~~ \n")
print("Let's Start the Game\n")

u_s=0
c_s=0

while True: 
    user_choice = (input("Rock,Paper or Scissor?: ")).lower()
    print("\n")
    if user_choice in ("rock","paper","scissor"):
        print("You Chose: ",user_choice)
    else:
        print("Invalid Choice.Please Enter Your Choice Again(Rock,Paper or Scissor)")

    print("\n")
    ch=["rock","paper","scissor"]
    computer_choice = random.choice(ch)
    print("Computer Chose: ",computer_choice)
     
    if  (user_choice == "rock" and computer_choice == "scissor"):
        u_s=u_s+1

    elif  (user_choice == "paper" and computer_choice == "rock"):
        u_s=u_s+1

    elif  (user_choice == "scissor" and computer_choice == "paper"):
        u_s=u_s+1

    elif (user_choice == computer_choice):
        u_s=u_s
        c_s=c_s
        

    else:
        #print("\nComputer Win")
        c_s=c_s+1

    print("\nDo you want to continue playing?(Yes/No)")
    r=input("Enter your response: ")
    if(r=="No" or r=="no"):
        break
    if(r=="Yes" or r=="yes"):
        continue
    else:
        print("Invalid Choice.")
        break
        
print("\n       ~~~~~       Final Score       ~~~~~      \n")
print("Your Score: ",u_s)
print("\nComputer Score: ",c_s)
if(u_s>c_s):
    print("\nYou Win")
elif(u_s==c_s):
    print("\nIt's a Tie")
else:
    print("\nComputer Win")
print("\n     ~~~~~     Thank You for Playing     ~~~~~     ")   
    
    
    
            
        

       
