import time, sys

# Define the story structure using a dictionary
story = {
    "start": {
        "description": "\n✨ The world around you begins to twist and distort.\n "
    "The ground vanishes beneath your feet, and a rush of wind pulls\n you into a swirling vortex of light and shadow...\n\n"
    "A moment ago, you were in the real world. Now, you wake up in a strange,\n enchanted land where the sky shimmers with emerald hues\n "
    "and the trees whisper in voices not their own.\n\n"
    "A cloaked figure steps forward, their eyes glowing with an eerie light.\n"
    "'You are not alone,' they say. 'Three of your friends have been\n taken—scattered across this world in new avatars. If you wish to escape,\n "
    "you must find them before time runs out. But beware… this land is alive,\n and it plays by its own rules.'\n\n"
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
           "enter hall" : "radiant hall",
           "return to start" : "start"
        }
    },
    "radiant": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
    "the forgotten forge": { #still needs editing
        "description": "You arrive at a fast-flowing river. There's a bridge and a boat.",
        "choices": {
            "cross bridge": "troll",
            "take boat": "island"
        }
    },
        "radiant": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
    "the verdant ruins": { #still needs editing
        "description": "A bear opens the door and chases you! You run back.",
        "choices": {
            "run": "start",
            "shoot bear": "river"
        }
    },
        "radiant": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "location": {
        "description" : "",
        "choices": {
            "" : "",
            "" : ""
        }
    },
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
        scroll_text("\nWhat path will you choose?:")
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
