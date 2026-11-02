import time  # gives us time.sleep() to pause the program

name = "Elastigirl"
kids = ["Violet", "Dash", "Jack-Jack"]

# A for loop runs the indented lines once for each thing in the list
# Each time, kid becomes the next name in the list
for kid in kids:
    print(name, "hugs", kid)

# Countdown! time.sleep(0.5) waits half a second
for number in [5, 4, 3, 2, 1]:
    print(number)
    time.sleep(0.5)
print("Blast off!")  # not indented, so it runs once, after the loop

# A while loop keeps going as long as the check is True
stretch = 1
while stretch < 100:
    time.sleep(0.3)
    print(name, "stretches to", stretch, "meters")
    stretch = stretch * 2  # without this line the loop would never stop!
