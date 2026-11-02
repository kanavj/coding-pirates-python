name = "Elastigirl"
age = 40
married = True
kids = ["Violet", "Dash", "Jack-Jack"]
villain_nearby = True

if villain_nearby:
    print(name, "stretches into action!")
else:
    print(name, "relaxes at home.")

if age > 30:
    print(name, "is older than 30.")
else:
    print(name, "is 30 or younger.")

if married:
    print(name, "is married.")

if len(kids) == 0:
    print(name, "has no kids.")
elif len(kids) == 1:
    print(name, "has one kid.")
else:
    print(name, "has", len(kids), "kids.")
