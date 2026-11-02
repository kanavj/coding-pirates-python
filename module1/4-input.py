# input() asks the player a question and waits for them to type an answer
name = input("What is your name? ")
print("Hello", name, "!")

power = input("If you could have one superpower, what would it be? ")
print(name, "now has the power of", power, "! 🦸")

# input() always gives you text, even when you type a number!
age = input("How old are you? ")
age = int(age)  # int() turns the text "11" into the number 11
print("Next year you will be", age + 1)

# You can use the answer in an if, just like in the game
answer = input("A villain appears! Do you want to fight? (yes/no) ")
if answer == "yes":
    print(name, "uses", power, "and wins! 💥")
elif answer == "no":
    print(name, "runs away screaming. 🏃")
else:
    print(name, "is so confused that the villain gets bored and leaves.")
