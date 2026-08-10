playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Let's Play!")

score = 0

answer = input("What's a race condition? ").lower()

if answer == "when two threads access shared data at the same time and the outcome depends on unpredictable timing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does 'DRY' stand for? ").lower()

if answer == "don't repeat yourself -- a principle to reduce code duplication":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What's the difference between git pull and git fetch? ").lower()

if answer == "fetch downloads changes without merging; pull downloads and merges them immediately":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What's a null pointer dereference? ").lower()

if answer == "when your code tries to access memory through a pointer that points to nothing -- and crashes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")