import random

user_wins = 0
comp_wins = 0
draw=0
options = ["r", "p", "s"]

while True:
    user_choose =input("What so you want to choose? Type r for Rock 🧱, p for Paper 📄, s for Scissors ✂ or Q to quit: ").lower()
    
    if user_choose == "q":
        break
    if user_choose not in options:
            continue
    random_number = random.randint(0, 2)
    comp_choose= options[random_number]
    print ("Computer choose", comp_choose +"." )
    
    if user_choose == "r" and comp_choose =="s":
        print("You Won!")
        user_wins +=1
        
    
    elif user_choose == "p" and comp_choose =="r":
        print("You Won!")
        user_wins +=1
        
    
    elif user_choose == "s" and comp_choose =="p":
        print("You Won!")
        user_wins +=1
        
    elif user_choose == comp_choose:
        print('Draw!')
        draw += 1
        continue
    else:
        print("You Lost") 
        comp_wins +=1   
    
print("You won", user_wins,"times")   
print("Computer won", comp_wins,"times")  
print ("Thanks for playing")
        