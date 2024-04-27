from replit import clear
import random
message = ''

# Track generation
track_length = random.randint(25, 51) #add 1 extra
track = [[" "] * track_length, [" "] * track_length]  # Two lanes


# Marking segments
for i in range(10, track_length, 10):  # Key Change
    if i < track_length:  # Ensure don't go beyond the track boundaries
        track[0][i] = f"{i: >1}"
        track[1][i] = f"{i: >1}" 
    
# Player setup
player_position = 0
computer_position = 0

# Message Setup
high_risk_success_messages = [
    "You took a massive risk and it paid off! + ", 
    "Fortune favors the bold! + ",
    "That gamble paid off handsomely! + "
]
high_risk_failure_messages = [
    "Your gamble backfired! ",
    "Ouch! That risk didn't quite work out. ",
]

# Medium Risk Messages
medium_risk_success_messages = [
    "Nice steady progress! + ",
    "A calculated risk pays off! + ",
   
]
medium_risk_failure_messages = [
    "Uh oh, a slight setback. ",
    "Not your best move, but onward! ",
   
]

# Low Risk Messages
low_risk_success_messages = [
    "Safe and steady wins the race! + ",
    "A cautious approach yields a small gain. + ",
]

low_risk_failure_messages = [
    "Not good but not so bad. ",
    "Try a little harder next time. ",
]
no_risk_messages = [
    "Taking it slowly is always the best option. + ",
    "You're not taking any risks, but you still made some progress. + ",
    "No risk, small gains. +"
]

player_symbol = "🚗"  # car emoji 
computer_symbol = "🚕"

def display_track():
    half_track = track_length // 2
    clear()
    border = "~~." * half_track
    print(border)  # Top border
    player_track = track[0].copy()
    computer_track = track[1].copy()

    player_track[player_position] = player_symbol 
    computer_track[computer_position] = computer_symbol 

    print("".join(player_track))
    print(border) #Middle border
    print("".join(computer_track))
    print(border)  # Bottom border
    
# Game loop
while player_position < track_length and computer_position < track_length:
    display_track()
    print(message)
    print("Your position:", player_position)
    print("Computer's position:", computer_position)
    print(f"Track length: {track_length - 1}")

    choice = input("Choose your risk level (High, Medium, Low, None): ")

    if choice.lower() == "high":
        if random.random() < 0.4:  # 40% chance
            player_progress = random.randint(4, 6)  
            message = random.choice(high_risk_success_messages) + str(player_progress)
        else:
            player_progress = random.randint(-4, -2) 
            message = random.choice(high_risk_failure_messages) + str(player_progress)

    elif choice.lower() == "medium":
        if random.random() < 0.6: 
            player_progress = random.randint(2, 4)
            message = random.choice(medium_risk_success_messages) + str(player_progress)
        else:
            player_progress = random.randint(-2, 0) 
            message = random.choice(medium_risk_failure_messages) + str(player_progress)

    elif choice.lower() == "low":
        if random.random() < 0.8: 
            player_progress = random.randint(1, 2)
            message = random.choice(low_risk_success_messages) + str(player_progress)
        else:
            player_progress = random.randint(-1, 0) 
            message = random.choice(low_risk_failure_messages) + str(player_progress)
    else:
        player_progress = 1  # Default movement, no need for flavor text
        message = random.choice(no_risk_messages) + str(player_progress)
    player_position += player_progress


    # Computer's turn
    computer_choice = random.choice(["Low", "Low", "Medium"])  
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
