story = {
    "start": {
        "description": """"
                        |>>>     
                        |                         
                    _  _|_  _                    
                   |;|_|;|_|;|                   
                   \..      /                   
                    \..    /                    
                     ||  |                     
                     ||  |                     
                     ||  |                     
               ,     ||  |     ,               
              /|     ||  |     |\              
             / |     ||  |     | \             
            |  |     ||  |     |  |            
    ________|  |____||__|_____|  |________    
     -[____|____]--'--[____]--[____|____]-    
        |                             |       
    ----|   𝔓𝔞𝔱𝔥 𝔬𝔣 𝔏𝔦𝔤𝔥𝔱 𝔞𝔫𝔡 𝔖𝔥𝔞𝔡𝔬𝔴𝔰 |----   
        |   | |                       |       
        |   |_|                       |       
        |_____________________________|       
       (______________________________)       
        |  |                       |  |     
        |  |                       |  |     
        |  |                       |  |     
        |  |                       |  |     
        |__|                       |__|    
        (__)                       (__)

    """
        
    "\n\n✨ The world around you begins to twist and distort.\n "
    "The ground vanishes beneath your feet, and a rush of wind pulls\n you into a swirling vortex of light and shadow...\n\n"
    "A moment ago, you were in the real world. Now, you wake up in a strange,\n enchanted land where the sky shimmers with emerald hues\n "
    "and the trees whisper in voices not their own.\n\n"
    "A cloaked figure steps forward, their eyes glowing with an eerie light.\n"
    "'You are not alone,' they say. 'Three of your friends have been\n taken—scattered across this world in new avatars. If you wish to escape,\n "
    "you must find them before time runs out. But beware… this land is alive,\n and it plays by its own rules.'\n\n"
    "As their voice fades, you hear distant drums pounding like a heartbeat.\n\n"
        "🎲 The game has begun... 🎲\n\nMake your choices wisely:",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
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
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins"
        },
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
            "follow the sound of a familiar voice": "the luminescent cavern"
        },
        "shop": {
            "weapons": {"sword of radiance": 500, "shield of dawn": 400},
            "potions": {"health potion": 100, "mana potion": 150}
        }
    },
    "radiant hall": {
        "description": "You enter a vast, shimmering hall lit by eternal lights that reflect off polished stone floors. The air is warm, and the atmosphere is calm, though there’s a sense of ancient power that lurks beneath the beauty.\n\nA mysterious voice echoes: 'Solve this riddle to proceed.'\n\n'What has to be broken before you can use it?'",
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
    "the eternal garden": {
        "description": "A mystical garden where flowers bloom under the light of a perpetual sun. Time flows differently here, and the player must deal with time loops that can either help or hinder their progress.",
        "choices": {
            "return to the eternal garden": "the eternal garden",
            "follow the echo of a familiar voice": "castle of the doomed"
        },
        "minigame": {
            "win": "boss 2",
            "loss": "start",
            "penalty": 100 * (1 / 5)
        }
    },
    "the luminescent cavern": {
        "description": "A glowing cave filled with creatures and shimmering crystals. It's peaceful yet haunted by whispers of forgotten spirits.",
        "choices": {
            "return to the luminescent cavern": "the luminescent cavern",
            "follow the echo of a familiar voice": "castle of the doomed"
        },
        "minigame": {
            "win": "boss 2",
            "loss": "start",
            "penalty": 100 * (1 / 5)
        }
    },
    "castle of the doomed": {
        "description": "You enter a shadowy arena, facing the Shade of the Forgotten King!",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins"
        },
        "boss": {
            "name": "Shade of the Forgotten King",
            "description": "A dark, shadowy figure from an ancient time, twisted by the corruptive forces of the temple.\n\nIts power is tied to the absence of light.",
            "abilities": ["Shadow Strikes", "Summoning Dark Minions", "Teleportation"],
            "health": 100
        }
    },
    "the forgotten forge": {
        "description": "You enter a scorching-hot tunnel, the obsidian walls radiate such heat that the very air ripples around you. Small spurts of lava leak from the cracks in the wall onto the brimstone floor. At the end of the tunnel lies an empty minecart sitting on a track.",
        "choices": {
            "take the minecart": "the smelting pits",
            "return to start": "start"
        }
    },
    "the smelting pits": {
        "description": "You find yourself in the midst of an active underground metalworking and smelting facility. Dwarves with skin made of stone wheel carts full of ingots of varying metals.",
        "choices": {
            "visit item shop": "the forgotten forge item shop",
            "return to smelting pit": "the smelting pits"
        },
        "riddle": {
            "question": "What is the name of the dwarven smelters' boss?",
            "options": ["john anvil", "smeltmiser", "the forge guardian", "grimthar steelfather"],
            "correct": "the forge guardian",
            "penalty": 25
        }
    },
    "the forgotten forge item shop": {
        "description": "Welcome to the Forgotten Forge Item Shop! Here's what you can buy:",
        "choices": {
            "follow the oxidizing air": "the rusted chamber",
            "return to item shop":"the forgotten forge item shop"
        },
        "shop": {
            "weapons": {"sword of titanium": 500, "shield of lava": 400},
            "potions": {"health potion": 100, "mana potion": 150}
        }
    },
        "the rusted chamber": {
        "description": """
            "Hmm...", the dwarf ponders quizzically,
            "That is indeed correct, however I need more proof of identification"
            "Please, follow me."
            The dwarf guides you through all the hussle and bussle of the main factory floor, he takes you to a rusty old mineshaft elevator and pressed a button. Suddenly it plunges deep within the earth, at an immense speed, just like the minecart.
            When you feel like you are just about to hurl, it stops suddenly. The dwarf guides you into his office. You sit down in a wooden chair right in front of his desk, seemingly very calm even after the death-defying ride you two just went on.
            "Now...", he says as he pushes up his glasses,
            "I have a record of every non-dwarf worker in this facility, and I can easily verify your identity this way, so please... Tell me your name"
            You panic internally, as you know for a fact your name is not in their records at all, but you keep your cool and say...
        """,
        "choices": {
            "continue on with the story": "the furnace core",
            "return to chamber": "the rusted chamber"
        },
        "riddle": {
            "question": "what is your name?",
            "options": ["lillia everbloom", "titania bloodseeker", "mira la blanc", "lucy emberheart"],
            "correct": "lucy emberheart",
            "penalty": 25
        }

    },
    "the furnace core": {
        "description": """ 
        "Hmm, yeah you check out, you are indeed Lucy Emberheart". says the dwarf.
        "You are dismissed, get back to work!"
        You take the elevator but instead of going back up you decide to go even deeper into the earth. 
        Once again it dives into the earth, almost feeling impossible that the earth is THIS deep. You almost hurl again once more, you keep it in.
        You find yourself in a room facing a golem made of obsidian and lava with a flaming skull for a head. He is guarding a large, ominous door.
        "Halt! He exclaims.
        "You must play a game with me in order to see my boss". 
        "It's simple. rock, paper, scissors, you know how to play".
        """,
        "choices": {
            "continue down the mine shaft":"the forge guardian",
            "return to furnace":"the furnace core"
        },
        "minigame": {
            "win": "the forge guardian",
            "loss": "start",
            "penalty": 100 * (1 / 5)
        }
    },
    "the forge guardian": {
        "description": "You face The Forge Guardian, an enormous golem made of obsidian and lava!",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins"
        },
        "boss": {
            "name": "The Forge Guardian",
            "description": "A Golem made with an outer shell composed of obsidian while its inner core contains hot lava, a flaming skull appears right above its torso, possessing the body.",
            "abilities": ["Slag Iron Steel Smash", "Call of the Fire Spirits", "Forge Shield"],
            "health": 100
        }
    },
        "the verdant ruins": {
    "description": "Once a grand garden, now abandoned and overtaken by nature. Vines crawl along cracked stone walls, and strange creatures can be seen dashing between the trees.",
    "choices": {
        "enter the overgrown courtyard": "the overgrown courtyard",
        "return to start": "start",
        }
    },
    "corrupted beast of the ruins": {
        "description": "You enter a castle, facing the Corrupted Beast of the Ruins! A massive, twisted creature once a protector of the forest, now corrupted by dark magic. It has the ability to summon storms and manipulate the plants around it.",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
        },
        "boss": {
            "name": "The Corrupted Beast of the Ruins",
            "description": "A massive, twisted creature that was once a protector of the forest. Now, it is corrupted by dark magic. It summons storms and controls the plants around it, making it a dangerous foe.",
            "abilities": ["Summons poisonous vines", "Creates thunderstorms", "Commands creatures of the forest"],
            "health": 100,
            "weakness": "Vulnerable to fire and light-based attacks. Larken can help control nature to turn the tide of battle."
        }
    },
    "the verdant ruins item shop": {
        "description": "Welcome to the Verdant Ruins Item Shop! Here's what you can buy:",
        "choices": {
            "follow the luscious path":"the twisted thicket",
            "follow an enlightend feeling": "the ancient tree of life",
            "return to item shop": "the verdant ruins item shop"
        },
        "shop": {
            "weapons": {"feathered bow of wilds": 650, "vine whip": 250},
            "armor": {"mossy cloak": 100}
        }
    },
    "the overgrown courtyard": {
        "description": "You step into the overgrown courtyard. Once a grand garden, now overtaken by nature. Vines crawl along cracked stone walls, and strange creatures flit between the trees.",
        "choices": {
            "item shop": "the verdant ruins item shop",
            "return to overgrown courtyard": "the overgrown courtyard"
        },
        "riddle": {
            "question": "What is always in front of you but can't be seen?",
            "options": {"the future", "the past", "the present", "a shadow"},
            "correct": "the future",
            "penalty": 25
        }
    },
    "the twisted thicket": {
        "description": "A dense forest filled with dangerous creatures and magical plants that can either help or hinder you. Some paths are deceptive.",
        "choices": {
            "cross a long wooden bridge": "corrupted beast of the ruins",
            "return to thicket": "the twisted thicket"
        },
        "riddle": {
        "question": "I can be chopped, but I don't cry, \nI can be climbed, but I don't fly. \nI have rings, but I don't wear a thing, \nWhat am I, with roots that cling?",
        "options": ["The Tree", "A Bird", "A Rock", "A Cloud"],
        "correct": "The Tree",
        "penalty": 25
        }
    },
    "the ancient tree of life": {
        "description": "A massive, ancient tree at the center of the ruins, its roots stretch deep into the earth. The tree is a source of powerful magic, but it is dying and needs restoration.",
        "choices": {
            "cross a long wooden bridge": "corrupted beast of the ruins",
            "return to tree of life": "the ancient tree of life"
        },
        "minigame": {
            "win": "corrupted ceast of the cuins",
            "loss": "start",
            "penalty": 100 * (1 / 5)
        },
    },
  }



import time, sys
import random

# Player attributes
player = {"health": 100, "coins": 2000}

def solve_riddle(location):
    riddle = story[location].get("riddle", {})  # Get riddle data safely
    if not riddle:
        return location  # Return immediately if no riddle exists

    scroll_text(f"Riddle: {riddle['question']}")

    while True:
        scroll_text("Choose your answer:")
        for option in riddle["options"]:
            scroll_text(f"- {option}")

        # Normalize input and correct answer for better matching
        answer = input("Enter your choice --> ").strip().lower()
        correct_answer = riddle["correct"].strip().lower()

        if answer == correct_answer:
            scroll_text("Correct! You may proceed.")
            break  # Exit the riddle and move forward
        else:
            player["health"] -= riddle["penalty"]
            scroll_text(f"Wrong! You lose {riddle['penalty']}% health. Current health: {player['health']}%")
            if player["health"] <= 0:
                scroll_text("You have died... Game Over.")
                exit()

    # After solving the riddle, show choices for the location
    choices = story[location].get("choices", {})
    if choices:
        scroll_text("\nWhat will you do next?")
        for choice in choices:
            scroll_text(f"- {choice}")

        while True:
            action = input("\nEnter your choice here ---> ").strip().lower()
            if action in choices:
                return choices[action]  # Move forward in the game
            else:
                scroll_text("Invalid choice, try again.")

    return location  # Stay at the same location if no choices exist


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
            break  # Exit the shop loop and show location choices

        for category, items in shop.items():
            if choice in items:
                if player["coins"] >= items[choice]:  # Ensure enough funds
                    player["coins"] -= items[choice]
                    scroll_text(f"You purchased {choice}! Coins left: {player['coins']}")

                    # Restore health if health potion is bought
                    if choice == "health potion":
                        player["health"] = 100
                        scroll_text("Your health has been fully restored to 100%!")
                    if choice == "mossy cloak":
                        player["health"] = 100
                        scroll_text("Your health has been fully restored to 100%!")
                    break  # Exit loop after successful purchase
                else:
                    scroll_text("Insufficient funds! Try again.")
                    break  # Prevent further processing if player lacks coins
        else:
            scroll_text("Invalid choice. Try again.")

    # After exiting the shop, present choices available at the current location
    choices = story[location].get("choices", {})
    if choices:
        scroll_text("\nWhat will you do next?")
        for choice in choices:
            scroll_text(f"- {choice}")

        while True:
            action = input("\nEnter your choice here ---> ").lower()
            if action in choices:
                return choices[action]  # Move forward in the game
            else:
                scroll_text("Invalid choice, try again.")

    return location  # If no choices exist, stay at the current location


# Track collected characters
collected_characters = set()



def rock_paper_scissors(location):
    rps = story[location].get("minigame", {})
    options = ["rock", "paper", "scissors"]

    while True:
        scroll_text("Choose your move:")
        for option in options:
            scroll_text(f"- {option}")

        player_choice = input("Enter your choice here ---> ").strip().lower()
        if player_choice not in options:
            scroll_text("Invalid move, try again.")
            continue

        enemy_choice = random.choice(options)
        scroll_text(f"You chose {player_choice}. The opponent chose {enemy_choice}.")

        if player_choice == enemy_choice:
            scroll_text("It's a tie! Try again.")
            continue  # Restart the loop for a new round

        # Check if the player wins
        if (player_choice == "rock" and enemy_choice == "scissors") or \
           (player_choice == "paper" and enemy_choice == "rock") or \
           (player_choice == "scissors" and enemy_choice == "paper"):
            scroll_text(f"You win! {player_choice} beats {enemy_choice}.")
            break  # Exit the loop and proceed to choices

        # Player loses
        scroll_text(f"You lose! {enemy_choice} beats {player_choice}.")
        player["health"] -= rps["penalty"]
        scroll_text(f"Your health is now {player['health']}%.")

        if player["health"] <= 0:
            scroll_text("Game over! You lost.")
            player["health"] = 100  # Reset health for replayability
            return "start"  # Send player back to the start

    # ✅ FIX: Show choices after winning instead of restarting the game
    choices = story[location].get("choices", {})
    
    if choices:
        scroll_text("\nWhat will you do next?")
        for choice in choices:
            scroll_text(f"- {choice}")

        while True:
            action = input("\nEnter your choice here ---> ").strip().lower()
            if action in choices:
                return choices[action]  # Move forward in the game
            else:
                scroll_text("Invalid choice, try again.")

    return location  # Stay at the same location if no choices are available

# Track collected characters
collected_characters = set()

# Track collected characters
collected_characters = set()

def boss_fight(location):
    boss = story[location]["boss"]
    boss_health = boss["health"]
    scroll_text(f"You encounter {boss['name']}! {boss['description']}")

    while player["health"] > 0 and boss_health > 0:
        scroll_text(f"Your Health: {player['health']}% | {boss['name']} Health: {boss_health}%")
        action = input("Do you attack or defend? (attack/defend) --> ").strip().lower()

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
            scroll_text(f"You defeated {boss['name']}!")
            player["coins"] += 1500
            scroll_text(f"You earned 1500 coins! Total coins: {player['coins']}")

            # ✅ Ensure character collection is working properly
            boss_rewards = {
                "shade of the forgotten king": "Elira",
                "the forge guardian": "Caspian",
                "the corrupted beast of the ruins": "Larken"
            }

            boss_name = boss["name"].strip().lower()  # Normalize boss name for matching

            if boss_name in boss_rewards and boss_rewards[boss_name] not in collected_characters:
                collected_characters.add(boss_rewards[boss_name])
                scroll_text(f"✨ You have collected {boss_rewards[boss_name]}! ✨")
                scroll_text(f"🏆 Characters collected: {len(collected_characters)} of 3")

            # ✅ Check if all characters have been collected and trigger win_game
            if len(collected_characters) == 3:
                win_game()
                return "start"

            break  # Exit loop after boss is defeated

        if player["health"] <= 0:
            scroll_text("You have been defeated... Game Over!")
            exit()

    # Show choices after winning
    choices = story[location].get("choices", {})
    if choices:
        scroll_text("\nWhat will you do next?")
        for choice in choices:
            scroll_text(f"- {choice}")

        while True:
            action = input("\nEnter your choice here ---> ").strip().lower()
            if action in choices:
                return choices[action]  # Move forward in the game
            else:
                scroll_text("Invalid choice, try again.")

    return location  # Stay at the current location if no choices are available



def win_game():
    scroll_text("\n🎉 CONGRATULATIONS! 🎉")
    scroll_text("You have collected and saved all 3 of your friends (Elira, Caspian, Larken) and completed your quest!")

    # Display ASCII Art for Victory
    victory_art = """"
                        |>>>     
                        |                         
                    _  _|_  _                    
                   |;|_|;|_|;|                   
                   \..      /                   
                    \..    /                    
                     ||  |                     
                     ||  |                     
                     ||  |                     
               ,     ||  |     ,               
              /|     ||  |     |\              
             / |     ||  |     | \             
            |  |     ||  |     |  |            
    ________|  |____||__|_____|  |________    
     -[____|____]--'--[____]--[____|____]-    
        |                             |       
    ----|   𝔓𝔞𝔱𝔥 𝔬𝔣 𝔏𝔦𝔤𝔥𝔱 𝔞𝔫𝔡 𝔖𝔥𝔞𝔡𝔬𝔴𝔰 |----   
        |   | |                       |       
        |   |_|                       |       
        |_____________________________|       
       (______________________________)       
        |  |                          |       
        |  |                          |       
        |  |                          |       
        |  |                          |       
        |__|                          |__|    
        (__)                          (__)

    """
    scroll_text(victory_art)

    scroll_text("\n🎮 Thank you for playing! 🎮")
    exit()


def play_game():
    location = "start"
    
    while True:
        if location in story:
            scroll_text("\n" + story[location].get("description", ""))
            
            if "boss" in story[location]:
                location = boss_fight(location)
                continue

            if "riddle" in story[location]:
                location = solve_riddle(location)
                continue

            if "minigame" in story[location]:
                location = rock_paper_scissors(location)
                continue

            if "shop" in story[location]:
                location = item_shop(location)
                continue

            choices = story[location].get("choices", {})
            if choices:
                scroll_text("\nWhat path will you choose?:")
                for choice in choices:
                    scroll_text(f"- {choice}")

                action = input("\nEnter your choice here ---> ").lower()
                if action in choices:
                    location = choices[action]
                else:
                    scroll_text("\nInvalid choice, try again.")
            else:
                scroll_text("No further choices available. Game Over!")
                break
        else:
            scroll_text("Error: Undefined location encountered. Exiting game.")
            break
        
        time.sleep(1)

def scroll_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

play_game()
