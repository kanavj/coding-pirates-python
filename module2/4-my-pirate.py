# 🏴‍☠️ 4-my-pirate.py: BOSS LEVEL! Lists + functions + dictionaries.
# OPTIONAL: an extra challenge to explore if you finish your shop early.
# Nobody has to do it, so pick whatever looks fun!

# TODO 1: Design your pirate! Change the values, and add at least
#         ONE key of your own: "pet", "ship", "superpower", "favourite_snack"...
pirate = {
    "name": "___",
    "hearts": 3,
    "gold": 0,
    "inventory": ["___", "___"],
}

# TODO 2: Print the FIRST thing in the inventory.
#         A list inside a dictionary! Hint: pirate["inventory"][0]


# TODO 3: Finish the function so it prints EVERYTHING about a pirate
def show_pirate(p):
    print("-" * 32)
    print("🏴‍☠️", p["name"])
    # print the hearts, the gold, the inventory and your own key!

    print("-" * 32)


show_pirate(pirate)

# TODO 4: Write a function find_treasure(p, amount) that adds
#         amount to the pirate's gold. Call it, then show the pirate again.
#         Hint: p["gold"] = p["gold"] + amount


# TODO 5: Write a function pick_up(p, item) that puts an item in the inventory.
#         Hint: remember append() from Snake Island?


# ⭐ OPTIONAL BONUS: Make a second pirate and let them battle!
#    Who has more gold? Use an if to find out.
