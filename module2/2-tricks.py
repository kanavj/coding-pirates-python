# 🪄 2-tricks.py: Teach Python new tricks!
# Fill in every ___ and do the TODOs from top to bottom.
# Press ▷ after every step.

import random  # borrows Python's box of random things (for the dice)


# ========== PART 1: before the break ==========

# ---------- Trick 1: a stats bar ----------
# This function gets 3 inputs: hearts, gold and inventory.
def show_stats(hearts, gold, inventory):
    print("-" * 32)
    # TODO 1: Pick your own heart emoji! 💙 💚 🧡 💜 🖤 ...
    print("Hearts:", "___ " * hearts)
    # TODO 2: Print the gold (the line above can help you)

    # TODO 3: Print the inventory

    print("-" * 32)


show_stats(3, 10, ["half a sandwich"])
# TODO 4: Call show_stats again with 1 heart, 99 gold and a kazoo in your bag


# ---------- Trick 2: YOUR trick ----------
# TODO 5: Invent your OWN function! It needs at least ONE input.
#         Some ideas:
#           battle_cry(name)     ->  Kat yells: AAARRRGH!
#           magic_spell(animal)  ->  Abracadabra! You turn into a frog 🐸
#           pirate_insult(food)  ->  You smell like a rotten banana!
#         Then call it 3 times with different inputs.


# ⭐ OPTIONAL BONUS: Copy show_stats into Snake Island (module1/5-snake_island.py)
#    and swap all 6 copies of the stats lines for one show_stats(hearts, gold, inventory)


# 🍪 BREAK! Save your file (Ctrl + S). Trick 3 comes after the break.


# ========== PART 2: after the break ==========

# ---------- Trick 3: roll the dice ----------
def roll_dice():
    # TODO 6: Give back a random number from 1 to 6.
    #         Hint: random.randint(1, 6)
    return ___


# TODO 7: Roll the dice! Call roll_dice(), catch the answer in a variable
#         called roll, and print it, like:  🎲 You rolled 4
#         Remember loot = double(10) on the slide? Same trick.
#         No blank this time: write both lines yourself!


# TODO 8: If the roll is 6, print "CRITICAL HIT!" (or your own celebration)
#         Tip: to test it without waiting for a 6, change the return line
#         to return 6 for a moment. Change it back afterwards!


# ⭐ OPTIONAL BONUS: Give roll_dice an input: roll_dice(sides)
#    so roll_dice(20) rolls a 20-sided dice.
