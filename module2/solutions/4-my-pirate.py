# 🏴‍☠️ 4-my-pirate.py: one possible solution (for helpers)

pirate = {
    "name": "Captain Kat",
    "hearts": 3,
    "gold": 0,
    "inventory": ["kazoo", "map"],
    "pet": "a grumpy crab",
}

print("First thing in the bag:", pirate["inventory"][0])


def show_pirate(p):
    print("-" * 32)
    print("🏴‍☠️", p["name"])
    print("Hearts:", "❤️ " * p["hearts"])
    print("Gold:", p["gold"])
    print("Inventory:", p["inventory"])
    print("Pet:", p["pet"])
    print("-" * 32)


show_pirate(pirate)


def find_treasure(p, amount):
    p["gold"] = p["gold"] + amount
    print("💰", p["name"], "finds", amount, "gold!")


def pick_up(p, item):
    p["inventory"].append(item)
    print("🎒", p["name"], "picks up a", item)


find_treasure(pirate, 25)
pick_up(pirate, "rubber duck")
show_pirate(pirate)

# ⭐ BONUS
rival = {"name": "One-Eyed Sam", "hearts": 2, "gold": 40, "inventory": [], "pet": "a moth"}
if pirate["gold"] > rival["gold"]:
    print(pirate["name"], "is the richest pirate!")
else:
    print(rival["name"], "is the richest pirate!")
