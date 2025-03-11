import time, sys

# Define the story structure using a dictionary
story = {
    "start": {
        "description": 
    "🎲 The game has begun... 🎲"
    "\n\nMake your choices wisely:",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
            "test":"boss 1"
        }
    },
    "temple of eternal light": { #still needs editing
        "description": "The Temple of Eternal Light stands as a towering monument of shimmering stone,\n\n its walls etched with celestial runes that glow with an otherworldly brilliance.\n\n At its heart, an arched doorway bathed in golden radiance beckons you forward—the Radiant Hall lies beyond,\n\n its secrets waiting to be unveiled.",
        "choices": {
           "enter hall":"radiant hall",
           "return to start":"start"
        }
    },
    "radiant hall": {
        "description" : "You enter A vast, shimmering hall lit by eternal lights that\n\n reflect off polished stone floors. The air is warm, and the atmosphere is calm,\n\n though there’s a sense of ancient power that lurks beneath the beauty.",
        ""
        "choices": {
            "follow beautiful fragrance" : "the eternal garden",
            "follow the sound of a familiar voice" : "the eternal garden"
        }
    },
        "the luminescesnt cavern": {
        "description" : "the luminescesnt cavern",
        "choices": {
            "" : "",
            "" : ""
        }
    },
        "the eternal garden": {
        "description" : "the eternal garden",
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
    "boss 1": {
        "name": "Shade of the Forgotten King",
        "description": "A dark, shadowy figure from an ancient time, twisted by the corruptive forces of the temple. Its power is tied to the absence of light.",
        "abilities": {
            "Shadow Strikes",
            "Summoning Dark Minions",
            "Teleportation"
        },
        "weakness": "Vulnerable to light-based magic",
        "special_ability": {
            "name": "Light-based Magic",
            "trigger": "Boss health below 25%",
            "description": "Elira can use her light-based magic to significantly weaken the Shade."
        },
        "responses": {
            "hit": "You landed an exact hit, dealing {damage} damage to the Shade.",
            "boss_hit": "The Shade attacks back, dealing {damage} damage to you."
        }
    },
    "temple of eternal light item shop": {
        "description":"",
        "choices": {
            "" : "the luminescent cavern",
            "" : "the eternal garden"
        }
    },
    "the forgotten forge item shop": {
        "description":"",
        "choices": {
            "" : "the luminescent cavern",
            "" : "the eternal garden"
        }
    },
    "the verdant ruins item shop": {
        "description":"",
        "choices": {
            "" : "the luminescent cavern",
            "" : "the eternal garden"
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

