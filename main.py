from replit import clear
import random


# Track generation
track_length = random.randint(25, 50)
track = [["-"] * track_length, ["-"] * track_length]  # Two lanes


# Marking segments
for i in range(10, track_length, 10):  
    track[0][i] = f"{i: >3}"  # Player's lane, right-aligned in a 3-character space
    track[1][i] = f"{i: >3}"  # Computer's lane
    
# Player setup
player_position = 0
computer_position = 0

player_symbol = "🚗"  # any car emoji 
computer_symbol = "🚕"

def display_track():
    clear()
    print("########################################################")  
    player_track = track[0].copy()
    computer_track = track[1].copy()

    player_track[player_position] = player_symbol 
    computer_track[computer_position] = computer_symbol 

    # Enhanced lane visuals
    for i in range(len(player_track)):
        if player_track[i] == "-":
            player_track[i] = " "  # Empty lane space
        if computer_track[i] == "-":
            computer_track[i] = " "

    print("".join(player_track))
    print("".join(computer_track))
    print("#######################################################")  
    
# Game loop
while player_position < track_length and computer_position < track_length:
    display_track()
    # Player's turn
    print("Your position:", player_position)
    print("Computer's position:", computer_position)
    print(f"Track length: {track_length}")

    choice = input("Choose your risk level (High, Medium, Low, None): ")

    if choice.lower() == "high":
        if random.random() < 0.3:  # 30% chance
            player_progress = random.randint(4, 6)  # Positive movement
        else:
            player_progress = random.randint(-4, -2)  # Negative movement

    elif choice.lower() == "medium":
        if random.random() < 0.5: # 50% chance
            player_progress = random.randint(2, 4) #Possitive movement
        else:
            player_progress = random.randint(-2, 0) #Negative movement
            
    elif choice.lower() == "low":
        if random.random() < 0.8: # 80% chance
            player_progress = random.randint(1, 2)
        else:
            player_progress = random.randint(-1, 0)
    else:
        player_progress = 1
    player_position += player_progress


    # Computer's turn
    computer_choice = random.choice(["Low", "Low", "Low"])  
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
