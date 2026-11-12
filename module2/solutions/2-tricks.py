# 🪄 2-tricks.py: one possible solution (for helpers)

import random

# ========== PART 1: before the break ==========


def show_stats(hearts, gold, inventory):
    print("-" * 32)
    print("Hearts:", "💙 " * hearts)
    print("Gold:", gold)
    print("Inventory:", inventory)
    print("-" * 32)


show_stats(3, 10, ["half a sandwich"])
show_stats(1, 99, ["kazoo"])


def battle_cry(name):
    print(name, "yells: AAARRRGH! 🏴‍☠️")


battle_cry("Kat")
battle_cry("Jumping Jack")
battle_cry("Cookie the Banana")

# ========== PART 2: after the break ==========


def roll_dice():
    return random.randint(1, 6)


roll = roll_dice()
print("🎲 You rolled", roll)
if roll == 6:
    print("CRITICAL HIT! 💥")


# ⭐ OPTIONAL BONUS
def roll_big_dice(sides):
    return random.randint(1, sides)


print("🎲 20-sided dice:", roll_big_dice(20))
