import time, sys
import random

# Define the story structure using a dictionary
story = {
    "start": {
        "description": "🎲 The game has begun... 🎲\n\nMake your choices wisely:",
        "choices": {
            "the luminous path": "temple of eternal light",
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
            "fight boss": "boss 1",
            "item shop": "temple of eternal light item shop",
            "rps": "the furnace core"
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
            "path of whispering leaves": "the verdant ruins",
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
    "the eternal garden": {
        "description": "A mystical garden where flowers bloom under the light of a perpetual sun. Time flows differently here, and the player must deal with time loops that can either help or hinder their progress.",
        "choices": {
            "return to the eternal garden": "the eternal garden",
            "follow the echo of a familiar voice": "castle of the doomed",
        },
    },
    "the luminescent cavern": {
        "description": "A glowing cave filled with creatures and shimmering crystals. It's peaceful yet haunted by whispers of forgotten spirits.",
        "choices": {
            "return to the luminescent cavern": "the luminescent cavern",
            "follow the echo of a familiar voice": "castle of the doomed",
    "castle of the doomed": {
        "description": "You enter a shadowy arena, facing the Shade of the Forgotten King!",
        "choices": {
            "the molten passage": "the forgotten forge",
            "path of whispering leaves": "the verdant ruins",
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
        "description": """
            You seat yourself inside the cart and pull the lever beside the track; You are taken on a wild ride. The track follows a narrow, spiralling path downwards deep into the earth. The speed you are travelling at is not what you had originally anticipated.
            After what feels like an eternity, the track comes to end, ending abruptly right in front of a "dead end" sign. 
            You find yourself in the midst of an active underground metalworking and smelting facility. Dwarves with skin made of stone wheel carts full of ingots of varying metals.
            From gold, to bronze, to iron, to nickel, to cobalt. These industrious people work their tail off producing these alloys.
            A dwarf with very nerdy glasses and a button-up shirt approaches you and questions you:
            "Hey! You are not a dwarf, nor do you seem like you work here!"
            If you are truly a member of our staff, answer me this.
            What is the name of our boss? You know, our Director of Smelting himself?
        """,
        "choices": {
            "move on to the next part of the story": "the rusted chamber",
            "return to start": "start"
        },
        "riddle": {
            "question": """What is the name of the dwarven smelters' boss?""",
            "options": ["john anvil", "smeltmiser", "the forge guardian", "grimthar steelfather"],
            "correct": "the forge guardian",
            "penalty": 25
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
            "return to start": "start"
        },
        "riddle": {
            "question": "what is your name?",
            "options": ["lillia everbloom", "titania bloodseeker", "mira la blanc", "lucy emberheart"],
            "correct": "lucy emberheart",
            "pentalty": 25
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
        "choices": {},
        "minigame": {
            "win": "boss 2",
            "loss": "start",
            "penalty": 100 * (1 / 3)
        }
    },
    "boss 2": {
        "description": """ The golem shakes its head, defeated. 
        "Well, you won. So I'll move". 
        He slowly shambles over to the corner, defeated.
        You open the rusted-over door and find an even larger golem, its voice shakes the earth underneath you.
        "WHO DARES CHALLENGE ME? IT IS I, THE FORGE GUARDIAN".
        "OVERSEER OF THIS FACILITY, THE HEAD HONCHO HIMSELF. I HOLD THE HEAT OF A THOUSAND SUNS IN MY VERY HANDS. THINK YOU CAN TAKE ME ON?"
        "TRY IT AND BE DEFEATED!"
        """,
        "choices": {},
        "boss": {
            "name": "The Forge Guardian",
            "description": """ A Golem made with an outer shell composed of obsidian while its inner core contains hot lava, a flaming skull appears right above its torso, possessing the body. """,
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
    "boss 3": {
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
            "buy feathered bow of wilds": "the verdant ruins",
            "buy vine whip": "the verdant ruins",
            "buy mossy cloak": "the verdant ruins"
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
        "question": "A voice whispers: 'What is always in front of you but can't be seen?'",
        "choices": {},
        "riddle": {
            "question": "What is always in front of you but can't be seen?",
            "options": ["the future", "the past", "the present", "a shadow"],
            "correct": "the future",
            "penalty": 25
        }
    },
    "the twisted thicket": {
        "description": "A dense forest filled with dangerous creatures and magical plants that can either help or hinder you. Some paths are deceptive.",
        "choices": {
            "cross a long wooden bridge": "the ancient tree of life",
            "return to start": "start"
        }
    },
    "the ancient tree of life": {
        "description": "A massive, ancient tree at the center of the ruins, its roots stretch deep into the earth. The tree is a source of powerful magic, but it is dying and needs restoration.",
        "choices": {
            "speak with larken": "speak with larken",
            "return to the verdant ruins": "the verdant ruins"
        }
    },
    "larken": {
        "description": "Larken is a mysterious ranger who has lived among the ruins for as long as anyone can remember. She has a deep connection to the natural world and is skilled in archery and elemental magic.",
        "abilities": {
            "communicate with nature": "Allows Larken to speak with animals and plants, using them to gain information or aid the player.",
            "summon creatures": "Larken can call upon forest creatures to assist in combat.",
            "wind and plant magic": "Larken controls the forces of wind and plant magic, enhancing the player's attacks or slowing down enemies."
        },
        "role": "Larken will guide the player and assist in the fight against Boss #3 using her knowledge of the wild and her ability to control nature."
        }
    }
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
            
            # Handle boss fights, riddles, or minigames
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

            # Check if "choices" exist before accessing them
            if "choices" in story[location]:
                if not story[location]["choices"]:
                    scroll_text("Game Over!")
                    break
                
                # If choices are available, let the player make a decision
                scroll_text("\nWhat path will you choose?:")
                for choice in story[location]["choices"]:
                    scroll_text(f"- {choice}")

                action = input("\nEnter your choice here ---> ").lower()

                if action in story[location]["choices"]:
                    location = story[location]["choices"][action]
                else:
                    scroll_text("\nInvalid choice, try again.")
            else:
                # If no choices are available, assume the game is over
                scroll_text("No further choices available. Game Over!")
                break

        else:
            break

        time.sleep(1)

def scroll_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

import random

def rock_paper_scissors(location):
    rps = story[location]["minigame"]
    options = ["rock", "paper", "scissors"]
    
    while True:
        # Ask the player to choose their move
        scroll_text("Choose your move:")
        for option in options:
            scroll_text(f"- {option}")
        
        player_choice = input("Enter your choice here ---> ").lower()
        
        if player_choice not in options:
            scroll_text("Invalid move, try again.")
            continue
        
        # Enemy chooses a random option
        enemy_choice = random.choice(options)
        scroll_text(f"You chose {player_choice}. The opponent chose {enemy_choice}.")
        
        # Check the result of the game
        if player_choice == enemy_choice:
            scroll_text("It's a tie! Try again.")
        elif (player_choice == "rock" and enemy_choice == "paper") or \
             (player_choice == "paper" and enemy_choice == "scissors") or \
             (player_choice == "scissors" and enemy_choice == "rock"):
            # Player loses, subtract health
            scroll_text(f"You lose! {enemy_choice} beats {player_choice}!")
            player["health"] -= rps["penalty"]

            # Ensure health doesn't show a small floating-point value
            if player["health"] < 1:
                player["health"] = 0  # Set health to exactly 0
                scroll_text("Game over! You lost.")
                player["health"] = 100  # Reset health for the next round
                return "start"  # Return to start if health is zero
            
            scroll_text(f"You lost {rps['penalty']} HP! Your HP is now {player['health']}")
        else:
            # Player wins, move to the next area
            scroll_text(f"You win! {player_choice} beats {enemy_choice}.")
            win_location = rps.get("win")  # Use .get() to safely access win location
            if win_location:
                return win_location  # Proceed to the next location after winning
            else:
                scroll_text("Error: No valid location found after win. Returning to start.")
                return "start"
play_game()