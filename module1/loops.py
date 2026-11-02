import time

name = "Elastigirl"
kids = ["Violet", "Dash", "Jack-Jack"]

for kid in kids:
    print(name, "hugs", kid)

for number in range(5, 0, -1):
    print(number)
    time.sleep(0.5)
print("Blast off!")

stretch = 1
while stretch < 100:
    time.sleep(0.3)
    print(name, "stretches to", stretch, "meters")
    stretch = stretch * 2
