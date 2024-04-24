import random

track_length = 0
successful_moves = 0
current_speed = 0  # Initial speed

# List of possible track sections.
track_parts = [
    {
        "name": "Start/Finish Straight",
        "distance": 2,
        "difficulty": 1,
        "description": "A long straight stretch to build up speed."
    },
    {
        "name": "Curvy Hill",
        "distance": 1,
        "difficulty": 3,
        "description": "A winding uphill section that tests your handling."
    },
    {
        "name": "Wet Tunnel",
        "distance": 1,
        "difficulty": 2,
        "description": "A dark and slippery tunnel with limited visibility."
    },
    # Add more track sections as needed
]


def display_finish_art():
    print(r"""
       _______       _      __  
       / ____(_)___  (_)____/ /_ 
      / /_  / / __ \/ / ___/ __ \
     / __/ / / / / / (__  ) / / /
    /_/   /_/_/ /_/_/____/_/ /_/ 
    """)


# Function to generate a track of varying length
def generate_track(length_min, length_max):
    track = []
    current_distance = 0
    while current_distance < length_min:
        chosen_part = random.choice([
            part for part in track_parts
            if part["name"] != "Start/Finish Straight"
        ])
        track.append(chosen_part)
        current_distance += chosen_part["distance"]

    while current_distance < length_max:
        if random.random() < 0.7:
            chosen_part = random.choice(track_parts)
            track.append(chosen_part)
            current_distance += chosen_part["distance"]
        else:
            break

    track.insert(0,
                 track_parts[0])  # Add Start/Finish Straight at the beginning
    track.append(track_parts[0])  # Add Start/Finish Straight at the end
    track_length = sum(section["distance"] for section in track)

    return track, track_length


# Function to print the game title (ASCII art))
def print_title():
    print(r"""
   _   _   _   _     _   _   _   _     _   _   _  
  / \ / \ / \ / \   / \ / \ / \ / \   / \ / \ / \ 
 ( R | a | c | e ) ( T | e | x | t ) ( G | o | ! )
  \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/   \_/ \_/ \_/ 
""")


# Function to display player stats (Expand this)
def display_stats():
    print(
        "current options are: accelerate or ( a ), maintain or ( m ), brake or ( b )"
    )
    #print(f"Successful Moves: {successful_moves}")


# Function to get player input (Add more options)
def get_player_input():
    global successful_moves, current_speed  # Make current_speed global

    while True:
        choice = input("> pick an option: ").lower()

        if choice in ["accelerate", "a"]: 
              if random.random() < 0.7:  # Check for success
                print("You accelerate successfully!")
                current_speed = min(5, current_speed + 1)  
                successful_moves += 1
              else:  # Handling failed acceleration
                print("Your engine sputters! Unable to gain speed.")

        elif choice in ["brake", "b"]:
            print("Applying brakes!")  # Add a message for braking
            current_speed = max(0, current_speed - 2)  # Limit min speed to 0

        elif choice in ["maintain", "m"]:
            print("Maintaining speed.")  # Add a message for maintaining
            # No change in speed for "maintain"

        else:  # Invalid choice
            print("Invalid choice. Try again.")
            continue  # Go back to the beginning of the input loop

        return choice  # Return the valid choice


# Main Game Loop
def game_loop():
    speed_descriptions = {
        0: "Player is stopped",
        1: "Slowly picking up speed",
        2: "Moving at a comfortable pace",
        3: "Getting up to race speed",
        4: "Pushing the limits",
        5: "Flying over the track!"
    }

    # Generate a new track for the race
    track, track_length = generate_track(
        length_min=3, length_max=5)  # Adjust lengths as needed
    sections_completed = 0

    for section in track:
        print_title()
        print(
            f"Track Turns: {len(track)}, Sections Completed: {sections_completed}"
        )
        display_stats()
        print(section["description"])
        player_choice = get_player_input()

        sections_completed += 1
        if sections_completed == len(track):
            display_finish_art()
            break


# Start the game
print_title()
print("Welcome to the text-based racing game!")
game_loop()
