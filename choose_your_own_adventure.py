name = input("Enter your name: ")
print("Welcome to The Mysterious Forest Adventure", name)

answer = input(
    "You wake up at the edge of a mysterious forest. You see a dark cave on your left "
    "and a wooden bridge on your right. What do you do? " 
    "1. Enter the cave, 2. Cross the bridge, 3. Walk into the forest "
).lower()

if answer == "enter the cave":
    answer = input(
        "You find a treasure chest guarded by a sleeping dragon. What do you do? " 
        "1. Take the treasure, 2. Wake the dragon, 3. Leave the cave "
    ).lower()

    if answer == "take the treasure":
        print("You win! You found the hidden treasure!")
    elif answer == "wake the dragon":
        print("The dragon chases you away. Game Over.")
    elif answer == "leave the cave":
        print("You return to the forest.")
    else:
        print("Please enter a valid option! You lose")
elif answer == "cross the bridge":
    answer = input(
        "You find an old man who gives you a mysterious map. What do you do? " 
        "1. Follow the map, 2. Give the map back, 3. Ignore the old man "
    ).lower()
    if answer == "follow the map":
        print("You get lost! Game Over!")
    elif answer == "give the map back":
        print("The old man rewards your honesty. You win!")
    elif answer == "ignore the old man":
        print("You continue into the forest.")
    else:
        print("Please enter a valid option! You lose")

elif answer == "walk into the forest":
    answer = input(
        "You find three paths. What do you do? "
        "1. Take the dark path, 2. Take the sunny path, 3. Climb the tree "
    ).lower()
    if answer == "take the dark path":
        print("You get lost! Game Over!")
    elif answer == "take the sunny path":
        print("You discover a safe road home. You win!")
    elif answer == "climb the tree":
        print("You spot the way out but fall down. Game Over!")
    else:
        print("Please enter a valid option! You lose")
else:
    print("Please enter a valid option! You lose")

print("Thanks for playing", name + ".")