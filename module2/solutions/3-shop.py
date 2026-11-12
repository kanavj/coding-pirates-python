# 🛒 3-shop.py: one possible solution (for helpers)

shop = {
    "parrot": 30,
    "cursed sock": 5,
    "map to the toilet": 15,
    "golden spoon": 80,
}
gold = 50

print("Welcome to Grumpy Greta's Shop! Don't touch anything.")
print("A parrot costs", shop["parrot"], "gold")

shop["golden spoon"] = 45  # SALE!
shop["rubber duck"] = 10  # new delivery
print("Today in the shop:", shop)

# ⭐ BONUS: price list
for item in shop:
    print(item, "costs", shop[item])

choice = input("What do you want to buy? ")

if choice in shop:
    price = shop[choice]
    print("That costs", price, "gold.")
    if gold >= price:
        gold = gold - price
        print("Here's your", choice, "! You have", gold, "gold left. Now go away.")
    else:
        print("You can't afford that, you penniless barnacle! 😤")
else:
    print("A", choice, "?! Do I look like a", choice, "shop?")
