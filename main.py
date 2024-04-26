import random

# Track generation
track_length = random.randint(25, 40)
# Player setup
player_position = 0
computer_position = 0


# Game loop
while player_position < track_length and computer_position < track_length:
    # Player's turn
    print("Your position:", player_position)
    print("Computer's position:", computer_position)

    choice = input("Choose your risk level (High, Medium, Low, None): ")

    if choice.lower() == "high":
        player_progress = random.randint(5, 10)
    elif choice.lower() == "medium":
        player_progress = random.randint(3, 6)
    elif choice.lower() == "low":
        player_progress = random.randint(1, 4)
    else:
        player_progress = 0
    player_position += player_progress


    # Computer's turn
    computer_choice = random.choice(["High", "Medium", "Low"])  
    if computer_choice == "High":
        computer_progress = random.randint(5, 10)
    elif computer_choice == "Medium":
        computer_progress = random.randint(3, 6)
    elif computer_choice == "Low":
        computer_progress = random.randint(1, 4)
    else:
        computer_progress = 0
    computer_position += computer_progress

print("Game Over!")
if player_position >= track_length:
    print("You Win!")
else:
    print("Computer Wins!")
