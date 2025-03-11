import time, sys

# Define the story structure using a dictionary
story = {
    "start": {
        "description": "🎲 The game has begun... 🎲\n\nMake your choices wisely:",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
            "fight boss": "boss 1",
            "item shop": "temple of eternal light item shop"
        }
    },
    "temple of eternal light": {
        "description": "You arrive at the Temple of Eternal Light, its golden glow illuminating the surroundings. A grand hall awaits ahead.",
        "choices": {
            "enter radiant hall": "radiant hall",
            "return to start": "start"
        }
    },
    "boss 1": {
        "description": "You enter a shadowy arena, facing the Shade of the Forgotten King!",
        "choices": {},
        "boss": {
            "name": "Shade of the Forgotten King",
            "description": "A dark, shadowy figure from an ancient time, twisted by the corruptive forces of the temple.\n\nIts power is tied to the absence of light.",
            "abilities": ["Shadow Strikes", "Summoning Dark Minions", "Teleportation"],
            "health": 100
        }
    },
    "temple of eternal light item shop": {
        "description": "Welcome to the Temple of Eternal Light Item Shop! Here's what you can buy:",
        "choices": {
            "follow beautiful fragrance": "the eternal garden",
            "follow the sound of a familiar voice": "the luminescesnt cavern"
        },
        "shop": {
            "weapons": {"sword of radiance": 500, "shield of dawn": 400},
            "potions": {"health potion": 100, "mana potion": 150}
        }
    },
    "radiant hall": {
        "description": "You enter a vast, shimmering hall lit by eternal lights that\n\nreflect off polished stone floors. The air is warm, and the atmosphere is calm,\n\nthough there’s a sense of ancient power that lurks beneath the beauty.\n\nA mysterious voice echoes: 'Solve this riddle to proceed.'\n\n'What has to be broken before you can use it?'",
        "choices": {
            "item shop": "temple of eternal light item shop",
            "return to hall": "radiant hall"
        },
        "riddle": {
            "question": "What has to be broken before you can use it?",
            "options": ["an egg", "a door", "a secret", "a promise", "a heart", "a mirror"],
            "correct": "an egg",
            "penalty": 25
        }
    },
    "the luminescesnt cavern": {
        "description": "the luminescesnt cavern",
        "choices": {
            "item shop": "temple of eternal light item shop",
            "eternal garden": "the eternal garden"
        }
    },
    "the eternal garden": {
        "description": "the eternal garden",
        "choices": {
            "item shop": "temple of eternal light item shop",
            "start": "start"
        }
    },
}

# Player attributes
player = {"health": 100, "coins": 2000}

def solve_riddle(location):
    riddle = story[location]["riddle"]
    scroll_text(f"Riddle: {riddle['question']}")
    
    while True:
        scroll_text("Choose your answer:")
        for option in riddle["options"]:
            scroll_text(f"- {option}")
        
        answer = input("Enter your choice --> ").strip().lower()
        
        if answer == riddle["correct"]:
            scroll_text("Correct! You may proceed.")
            return location  # Stay in the location to display choices
        else:
            player["health"] -= riddle["penalty"]
            scroll_text(f"Wrong! You lose {riddle['penalty']}% health. Current health: {player['health']}%")
            if player["health"] <= 0:
                scroll_text("You have died... Game Over.")
                exit()

def item_shop(location):
    shop = story[location]["shop"]
    scroll_text(story[location]["description"])
    
    while True:
        scroll_text("\nAvailable items:")
        for category, items in shop.items():
            scroll_text(f"\n{category.capitalize()}:")
            for item, price in items.items():
                scroll_text(f"- {item}: {price} coins")
        
        choice = input("Enter the item you want to buy or type 'exit' to leave --> ").strip().lower()
        
        if choice == "exit":
            return "start"
        
        for category, items in shop.items():
            if choice in items and player["coins"] >= items[choice]:
                player["coins"] -= items[choice]
                scroll_text(f"You purchased {choice}! Coins left: {player['coins']}")
                return location
        
        scroll_text("Invalid choice or insufficient funds.")

def boss_fight(location):
    boss = story[location]["boss"]
    boss_health = boss["health"]
    scroll_text(f"You encounter {boss['name']}! {boss['description']}")
    
    while player["health"] > 0 and boss_health > 0:
        scroll_text(f"Your Health: {player['health']}% | {boss['name']} Health: {boss_health}%")
        action = input("Do you attack or defend? (attack/defend) --> ").lower()
        
        if action == "attack":
            boss_health -= 25
            scroll_text("You strike the enemy!")
        elif action == "defend":
            player["health"] -= 5
            scroll_text("You brace yourself, reducing damage taken!")
        else:
            player["health"] -= 15
            scroll_text("You hesitated! The boss lands a heavy blow!")
        
        if boss_health <= 0:
            scroll_text("You defeated the boss!")
            player["coins"] += 1500
            scroll_text(f"You earned 1500 coins! Total coins: {player['coins']}")
            return "start"
        
        if player["health"] <= 0:
            scroll_text("You have been defeated... Game Over!")
            exit()

def play_game():
    location = "start"

    while True:
        if location in story:
            scroll_text("\n" + story[location]["description"])
            if "boss" in story[location]:
                location = boss_fight(location)
                continue
            
            if "riddle" in story[location]:
                location = solve_riddle(location)
                continue
            
            if "shop" in story[location]:
                location = item_shop(location)
                continue
            
            if not story[location]["choices"]:
                scroll_text("Game Over!")
                break
            
            scroll_text("\nWhat path will you choose?:")
            for choice in story[location]["choices"]:
                scroll_text(f"- {choice}")

            action = input("\nEnter your choice here ---> ").lower()
            
            if action in story[location]["choices"]:
                location = story[location]["choices"][action]
            else:
                scroll_text("\nInvalid choice, try again.")
        else:
            break
        
        time.sleep(1)

def scroll_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

play_game()
