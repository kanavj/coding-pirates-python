name = "Elastigirl"
age = 40
married = True
kids = ["Violet", "Dash", "Jack-Jack"]
villain_nearby = True  # TRY: change to False and run again

# if checks if something is True. == means "is equal to"
# Only the indented lines under the right part will run
if villain_nearby == True:
    print(name, "stretches into action!")
else:  # else runs when the if is NOT True
    print(name, "relaxes at home.")

# > means "bigger than", < means "smaller than"
if age > 30:
    print(name, "is older than 30.")
else:
    print(name, "is 30 or younger.")

# An if doesn't always need an else
if married == True:
    print(name, "is married.")

# len() counts how many things are in a list
# elif means "else if": Python checks each one from the top and stops at the first True
if len(kids) == 0:
    print(name, "has no kids.")
elif len(kids) == 1:
    print(name, "has one kid.")
else:
    print(name, "has", len(kids), "kids.")
