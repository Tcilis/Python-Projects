import random

# Define the choices available for the game
choices = ["rock","paper","scissors"]

# Computer makes its choice
cpu = random.choice(choices)

# Welcome the user and explain the rules
print("Welcome to Rock Paper Scissors")
print("First player to reach 3 points WINS!")

# Get the player's choice
player = str(input("Make a choice: ")).upper() # use .upper() to convert input to uppercase

# Initialize points
cpu_points = 0
player_points = 0

# Loop until one player reaches 3 points
while cpu_points < 3 and player_points < 3:
    if player == "rock":
        if cpu == "paper":
            cpu_points += 1
            print("CPU has WON the round")
        elif cpu == "scissors":
            player_points += 1
            print("Player has WON the round")
        else:
            print("The round ended with a DRAW")
    elif player == "paper":
        if cpu == "rock":
            player_points += 1
            print("Player has WON the round")
        elif cpu == "scissors":
            cpu_points += 1
            print("CPU has WON the round")
        else:
            print("The round ended with a DRAW")
    else:
        if cpu == "rock":
            cpu_points += 1
            print("CPU has WON the round")  
        elif cpu == "paper":
            player_points += 1
            print("Player has WON the round")
        else:
            print("The round ended with a DRAW")
    
    # If neither player has won yet, ask for the next input
    if player_points < 3 and cpu_points < 3:
        cpu = random.choice(choices)
        player = str(input("Make a choice: ")).upper() # use .upper() to convert input to uppercase
        
# Declare the winner
if player_points > cpu_points:
    print("Player has WON THE GAME")
else:
    print("CPU has WON THE GAME")