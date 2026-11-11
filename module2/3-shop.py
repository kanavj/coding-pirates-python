# 🛒 3-shop.py: Open your own pirate shop!
# Fill in every ___ and do the TODOs from top to bottom.
# Press ▷ after every step.


# ---------- Step 1: stock your shop ----------
# TODO 1: Stock your shop! At least 4 items, and YOU invent the prices.
#         Parrots? Cursed socks? A map to the toilet? You decide.
shop = {
    "parrot": 30,
    "___": ___,
    "___": ___,
    "___": ___,
}
gold = 50  # how much gold the customer has

# TODO 2: Give your shopkeeper a name and a welcome message
print("___")

# TODO 3: Print the price of the parrot
print("A parrot costs", shop["___"], "gold")


# ---------- Step 2: sale & delivery ----------
# TODO 4: SALE! Make one item cheaper.
#         No blank this time: write the whole line yourself!


# TODO 5: A delivery just arrived! Add a brand-new item to the shop.


print("Today in the shop:", shop)


# ---------- Step 3: sell something ----------
# The customer chooses something
choice = input("What do you want to buy? ")

# TODO 6: Is the item in the shop? Fill in the blanks!
if choice in ___:
    price = shop[___]
    print("That costs", price, "gold.")
    # TODO 7: Enough gold? Take the gold and say thank you.
    #         Not enough? Your shopkeeper says something grumpy 😤
    if gold >= price:
        gold = gold - price
        print("___")
    else:
        print("___")
else:
    print("We don't sell that here!")  # TODO 8: make this message funnier

# ⭐ OPTIONAL BONUS: Show a price list before the customer chooses:
#    for item in shop:
#        print(item, "costs", shop[item])
# ⭐ OPTIONAL BONUS 2: Put the shopping part in a while loop, so the customer
#    can keep buying until they type "bye"
