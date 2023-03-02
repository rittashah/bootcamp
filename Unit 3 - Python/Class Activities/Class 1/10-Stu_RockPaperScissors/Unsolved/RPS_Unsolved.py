# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r") and (computer_choice == 'p'): 
    print("you chose rock, computer chose paper")
    print("you lose!")
elif (user_choice == "r") and (computer_choice == 's'): 
    print("you chose rock, computer chose scissors")
    print("you win!")
elif (user_choice == "r") and (computer_choice == 'r'): 
    print("you chose rock, computer chose rock")
    print("you tie!")
elif (user_choice == "p") and (computer_choice == 'p'): 
    print("you chose paper, computer chose paper")
    print("you tie!")
elif (user_choice == "p") and (computer_choice == 's'): 
    print("you chose paper, computer chose scissors")
    print("you lose!")
elif (user_choice == "p") and (computer_choice == 'r'): 
    print("you chose paper, computer chose rock")
    print("you win!")
elif (user_choice == "s") and (computer_choice == 'p'): 
    print("you chose scissors, computer chose paper")
    print("you win!")
elif (user_choice == "s") and (computer_choice == 's'): 
    print("you chose scissors, computer chose scissors")
    print("you tie!")
elif (user_choice == "s") and (computer_choice == 'r'): 
    print("you chose scissors, computer chose rock")
    print("you lose!")
else: 
    print("You input somethign other than r, p or s.")