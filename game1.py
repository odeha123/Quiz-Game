print("Welcome to my quiz game!")
playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play")

answer = input("What does CPU stand for? ")
if answer == "Central processing unit": 
    print("Correct!")
else:
    print("False")

answer = input("What does GPU stand for? ")
if answer == "Graphics processing unit": 
    print("Correct!")
else: 
    print("False")

answer = input("What does AI stand for? ")
if answer == "Artifical Intelligence": 
    print("Correct!")
else:
    print("False")