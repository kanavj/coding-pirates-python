import time  # gives us time.sleep() to pause the game

# Your starting stats. TRY: give yourself more hearts!
hearts = 3
gold = 0
inventory = ["half a sandwich"]  # a list of the things you carry

print("🏴‍☠️ Ahoy! Welcome aboard, matey!")
time.sleep(1)
name = input("What is your pirate name? ")
print("Captain", name, "... what a silly name. I LOVE it!")
time.sleep(1)
print("CRASH! Your ship smashes into SNAKE ISLAND. Oops.")
time.sleep(2)

# 🏖️ THE BEACH
print()  # an empty print() makes an empty line
print("-" * 32)  # "-" * 32 prints 32 dashes
print("🏖️  THE BEACH")
print("The sand is warm. A crab is staring at you. Very rudely.")
print()
# Show your stats. "❤️ " * hearts prints one heart for each heart you have
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)
print("1) Dig in the sand")
print("2) Chase the crab")
print("3) Take a nap")
choice = input("> ")

# input() gives text, so we check for "1" in quotes, not the number 1
if choice == "1":
    print("You dig and dig... and find a KAZOO! 🎺")
    inventory.append("kazoo")  # append() adds something to the end of a list
elif choice == "2":
    print("The crab pinches your bum! OUCH! 🦀")
    print("But it drops 5 gold coins while running away.")
    hearts = hearts - 1  # take the old number of hearts, subtract 1, and store it again
    print("💔 You lose a heart!")
    gold = gold + 5
elif choice == "3":
    print("You nap for 6 hours and wake up red as a lobster. Sunburn! 🦞")
    hearts = hearts - 1
    print("💔 You lose a heart!")
else:  # anything that isn't 1, 2 or 3 ends up here
    print(
        "That's not a choice! While you stand there confused, a seagull poops on you. 🐦"
    )
    hearts = hearts - 1
    print("💔 You lose a heart!")
time.sleep(2)

# After every room we check if you are out of hearts
if hearts <= 0:  # <= means "smaller than or equal to"
    print("💀 You ran out of hearts! GAME OVER")
    exit()  # exit() stops the program right here

# 🌴 THE JUNGLE
print()
print("-" * 32)
print("🌴 THE JUNGLE")
print("A grumpy monkey blocks the path. His tummy is rumbling.")
print()
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)
print("1) Give him your sandwich")
print("2) Do a silly dance")
print("3) Tickle him")
choice = input("> ")

if choice == "1":
    print("The monkey gobbles it up and burps in your face. 🐒")
    print("As a thank you, he gives you a RUBBER DUCK. 🦆")
    inventory.remove("half a sandwich")  # remove() takes something out of a list
    inventory.append("rubber duck")
elif choice == "2":
    print("The monkey laughs so hard he falls out of the tree!")
    print("He throws 3 gold coins at you to make you stop.")
    gold = gold + 3
elif choice == "3":
    print("The monkey does NOT like tickles. He throws a coconut. BONK! 🥥")
    hearts = hearts - 1
    print("💔 You lose a heart!")
else:
    print("That's not a choice! The monkey steals your hat and laughs at you. 🐒")
    hearts = hearts - 1
    print("💔 You lose a heart!")
time.sleep(2)

if hearts <= 0:
    print("💀 You ran out of hearts! GAME OVER")
    exit()

# 🐍 THE SNAKE PIT
print()
print("-" * 32)
print("🐍 THE SNAKE PIT")
print("Hundreds of snakes. They all stare at you. One is wearing a tiny hat.")
print()
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)
print("1) Play some music")
print("2) Tiptoe across")
print("3) Tell them a joke")
choice = input("> ")

if choice == "1":
    # An if inside an if! "in" checks if something is in the list
    if "kazoo" in inventory:
        print("You play the kazoo. 🎺 The snakes start a CONGA LINE!")
        # The for loop runs once for every snake in the list
        for snake in ["Sid", "Sally", "Steve", "Tiny Hat"]:
            print("  🐍", snake, "joins the conga! 💃")
            time.sleep(0.5)
        print("You dance across safely.")
    else:
        print("You have no instrument, so you hum. Badly. A snake bites your toe!")
        hearts = hearts - 1
        print("💔 You lose a heart!")
elif choice == "2":
    print("You tiptoe... right onto the snake with the tiny hat. He is FURIOUS.")
    hearts = hearts - 1
    print("💔 You lose a heart!")
elif choice == "3":
    print("Snakes have no ears. Nobody laughs. One bites your nose out of pity.")
    hearts = hearts - 1
    print("💔 You lose a heart!")
else:
    print("That's not a choice! You trip and fall face first into the snakes. 🐍")
    hearts = hearts - 1
    print("💔 You lose a heart!")
time.sleep(2)

if hearts <= 0:
    print("💀 You ran out of hearts! GAME OVER")
    exit()

# 🚪 THE TEMPLE DOOR
print()
print("-" * 32)
print("🚪 THE TEMPLE DOOR")
print("Carved in the stone: 'Say what a snake says, and I shall open.'")
print()
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)
password = input("Password: ")

# The loop keeps asking until the password is right. != means "is NOT equal to"
while password != "hiss":
    print("WRONG! The door sneezes slime all over you. 🤧")
    hearts = hearts - 1
    print("💔 You lose a heart!")
    if hearts <= 0:
        print("💀 You ran out of hearts! GAME OVER")
        exit()
    print("Psst... it starts with an h and ends with ss.")
    print("Hearts:", "❤️ " * hearts)
    password = input("Password: ")

print("The door giggles and swings open. Behind it: 10 gold coins! 💰")
gold = gold + 10
time.sleep(2)

# 👑 MONTY'S LAIR
print()
print("-" * 32)
print("👑 MONTY'S LAIR")
print("A GIANT python in pyjamas wakes up. 'WHO DARES WAKE THE MIGHTY MONTY?!'")
time.sleep(2)

# No choice here: the duck only helps if you picked it up in the jungle
if "rubber duck" in inventory:
    print("Monty sees your rubber duck. 'Is that... a BATH DUCKY?!' 🦆")
    print("He trades it for 20 gold coins and hugs it tightly.")
    inventory.remove("rubber duck")
    gold = gold + 20
    time.sleep(2)

print("'Answer my riddle, or I will squeeze you like a toothpaste tube!'")
print("'What do you call a snake that builds houses?'")
print()
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)
print("1) A boa constructor")
print("2) A sssssbuilder")
print("3) Bob")
choice = input("> ")

if choice == "1":
    print("'CORRECT!' Monty grumbles and hands you his treasure chest. 💎")
    gold = gold + 50
elif choice == "2":
    print("'A sssssbuilder?! That's not even a WORD!' Monty squeezes you. SQUEEEEEZE!")
    hearts = hearts - 2
    print("💔💔 You lose two hearts!")
elif choice == "3":
    print(
        "'BOB?! My cousin is called Bob... but WRONG!' Monty squeezes you. SQUEEEEEZE!"
    )
    hearts = hearts - 2
    print("💔💔 You lose two hearts!")
else:
    print("'That's not an answer!' Monty sneezes on you. Snake snot everywhere. 🤧")
    hearts = hearts - 1
    print("💔 You lose a heart!")
time.sleep(2)

if hearts <= 0:
    print("💀 You ran out of hearts! GAME OVER")
    exit()

# 🏆 THE END
print()
print("-" * 32)
print("🏆 Captain", name, "escapes Snake Island!")
print("Hearts:", "❤️ " * hearts)
print("Gold:", gold)
print("Inventory:", inventory)

# Your rank depends on your gold. The biggest number is checked first
if gold >= 70:
    print("You are a LEGENDARY pirate! 🏴‍☠️")
elif gold >= 30:
    print("You are a pretty good pirate.")
else:
    print("Your pockets are empty... but at least you are alive?")
