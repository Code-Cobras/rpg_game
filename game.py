import time, sys

# Define the story structure using a dictionary
story = {
    "start": {
        "description": "\n✨ The world around you begins to twist and distort. "
    "The ground vanishes beneath your feet, and a rush of wind pulls you into a swirling vortex of light and shadow...\n\n"
    "A moment ago, you were in the real world. Now, you wake up in a strange, enchanted land where the sky shimmers with emerald hues "
    "and the trees whisper in voices not their own.\n\n"
    "A cloaked figure steps forward, their eyes glowing with an eerie light.\n"
    "'You are not alone,' they say. 'Three of your friends have been taken—scattered across this world. If you wish to escape, "
    "you must find them before time runs out. But beware… this land is alive, and it plays by its own rules.'\n\n"
    "As their voice fades, you hear distant drums pounding like a heartbeat.\n\n"
    "🎲 The game has begun... 🎲"
    "\n\nMake your choices wisely:",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins"
        }
    },
    "temple of eternal light": { #still needs editing
        "description": "You find an old cabin. The door is locked.",
        "choices": {
            "knock": "bear",
            "leave": "start"
        }
    },
    "the forgotten forge": { #still needs editing
        "description": "You arrive at a fast-flowing river. There's a bridge and a boat.",
        "choices": {
            "cross bridge": "troll",
            "take boat": "island"
        }
    },
    "the verdant ruins": { #still needs editing
        "description": "A bear opens the door and chases you! You run back.",
        "choices": {
            "run": "start",
            "shoot bear": "river"
        }
    },
    "troll": {
        "description": "A troll blocks the bridge and demands a toll.",
        "choices": {
            "pay toll": "win",
            "refuse": "lose"
        }
    },
    "island": {
        "description": "You row to an island and find a treasure chest!",
        "choices": {
            "open chest": "win",
            "leave it": "start"
        }
    },
    "win": {
        "description": "You found the treasure! You win the game!",
        "choices": {}
    },
    "lose": {
        "description": "The troll throws you into the river. Game over.",
        "choices": {}
    }
}

def scroll_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)   
    print()


# Game function
def play_game():
    location = "start"

    while location in story:
        scroll_text("\n" + story[location]["description"])  # Show description
        if not story[location]["choices"]:  # If no choices, game ends
            scroll_text("Game Over!")
            break

        # Display choices
        scroll_text("\nWhat will you do?:")
        for choice in story[location]["choices"]:
            scroll_text(f"- {choice}")

        # Get player input
        action = input("\nEnter your choice here ---> ").lower()

        # Move to next location if valid choice
        if action in story[location]["choices"]:
            location = story[location]["choices"][action]
        else:
            scroll_text("\nInvalid choice, try again.")

        time.sleep(1)  # Adds a small delay for effect

# Start the game
play_game()
