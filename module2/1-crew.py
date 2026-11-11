# 🧭 1-crew.py: Pick your crew!
# Fill in every ___ and do the TODOs from top to bottom.
# Press ▷ after every step. An error about ___ means you still have a blank to fill in!

import random  # borrows Python's box of random things (for the bonus)


# ---------- Step 1: invent your crew ----------
# TODO 1: Invent your own crew of 5 pirates!
#         Friends, pets, superheroes, a talking banana... you decide.
crew = ["___", "___", "___", "___", "___"]


# ---------- Step 2: pick pirates ----------
# TODO 2: The captain is the FIRST pirate. Remember: Python counts from 0!
print("🏴‍☠️ Captain:", crew[___])

# TODO 3: The cook is the LAST pirate. Can you do it with -1?
print("🍳 Cook:", crew[___])

# TODO 4: Let the player pick a pirate, just like the chest game!
#         Ask for a number from 0 to 4 with input(), then print that pirate.
#         Remember: input() gives text, so use int().
#         No blank this time: write the lines yourself!


# ---------- Step 3: man overboard! ----------
# TODO 5: Oh no! The THIRD pirate fell overboard! 🌊
#         Put a brand-new pirate in their place.
#         Remember: Python counts from 0. Which place is the third pirate in?


print("Your crew is now:", crew)

# ⭐ OPTIONAL BONUS: Who has to walk the plank?
#    random.randint(0, 4) gives you a random number from 0 to 4.
#    1. Put a random number in a variable called number
#    2. Use it to pick a pirate: crew[number]
#    3. Print a dramatic announcement. As silly as you like!

# ⭐ OPTIONAL BONUS 2: What happens with crew[10]? Try it and read the error out loud.
