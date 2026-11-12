# 🧭 1-crew.py: one possible solution (for helpers)

import random

crew = ["Captain Kat", "Jumping Jack", "Polly", "One-Eyed Sam", "Cookie the Banana"]

print("🏴‍☠️ Captain:", crew[0])
print("🍳 Cook:", crew[-1])
number = int(input("Pick a pirate (0-4): "))
print("🧭 You picked:", crew[number])

crew[2] = "Nemo"  # Polly fell overboard 🌊
print("Your crew is now:", crew)

# ⭐ BONUS
number = random.randint(0, 4)
print("🦈 BAD NEWS!", crew[number], "has to walk the plank! The sharks say thank you.")

# ⭐ BONUS 2: crew[10] crashes with
#    IndexError: list index out of range
