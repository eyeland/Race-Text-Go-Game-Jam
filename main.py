import random

# Track generation
track_length = random.randint(25, 40)
track = ["-"] * track_length
track[0] = "<0->"  # Starting Point


# Marking segments
for i in range(10, track_length, 10): 
    track[i] = str(i)
    
# Player setup
player_position = 0
computer_position = 0

player_symbol = "🏎️"  # Or any car emoji you prefer
computer_symbol = "🚗"

def display_track():
    track[player_position] = player_symbol
    track[computer_position] = computer_symbol
    print("######################################################################################")
    print("".join(track)) 
    print("######################################################################################")
    track[player_position] = "-"  # Reset positions back to "-" 
    track[computer_position] = "-"


# Game loop
while player_position < track_length and computer_position < track_length:
    display_track()
    # Player's turn
    print("Your position:", player_position)
    print("Computer's position:", computer_position)

    choice = input("Choose your risk level (High, Medium, Low, None): ")

    if choice.lower() == "high":
        if random.random() < 0.3:  # 30% chance
            player_progress = random.randint(1, 4)  # Positive movement
        else:
            player_progress = random.randint(-3, 0)  # Negative movement

    elif choice.lower() == "medium":
        if random.random() < 0.5: # 50% chance
            player_progress = random.randint(1, 3) #Possitive movement
        else:
            player_progress = random.randint(-1, 0) #Negative movement
            
    elif choice.lower() == "low":
        if random.random() < 0.9: # 90% chance
            player_progress = random.randint(1, 2)
        else:
            player_progress = random.randint(-1, 0)
    else:
        player_progress = 0
    player_position += player_progress


    # Computer's turn
    computer_choice = random.choice(["High", "Medium", "Low"])  
    if computer_choice == "High":
        if random.random() < 0.3: # 30% chance
            computer_progress = random.randint(1, 4)
        else:
            computer_progress = random.randint(-3, 0)
            
    elif computer_choice == "Medium":
        if random.random() < 0.5: # 50% chance
            computer_progress = random.randint(1, 3)
        else:
            computer_progress = random.randint(-1, 0)
    elif computer_choice == "Low":
        if random.random() < 0.9: # 90% chance
            computer_progress = random.randint(1, 2)
        else:
            computer_progress = random.randint(-1, 0)
    else:
        computer_progress = 0
    computer_position += computer_progress

print("Game Over!")
if player_position >= track_length:
    print("You Win!")
else:
    print("Computer Wins!")
