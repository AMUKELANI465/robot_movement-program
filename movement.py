import math
import time

x = 0
y = 0
total_steps = 0

print("== A ROBOT MOVEMENT PROGRAM ==")
time.sleep(2)
print("please enter the direction/commands - U (up), L (left), R (right), D (down) or E for exit")
print("After entering your directions/commands please enter E to get the final robots results....")
time.sleep(1)

while True:
    command = input("Enter Commands (U/D/L/E/R): ").upper()
    if command == "E":
        break

    steps = int(input("please enter the number of steps : "))

    if command == "U":
        y = y + steps
        print("Your position is ", (x, y))
    elif command == "D":
        y = y - steps
        print("Your position is ", (x, y))
    elif command == "L":
        x = x - steps
        print("Your position is ", (x, y))
    elif command == "R":
        x = x + steps
        print("Your position is ", (x, y))
    elif command != "U" and command != "R" and command != "L" and command != "D":
        print("invalid command, please try again")
        total_steps = total_steps - steps  # prevent adding steps on invalid command

    total_steps = total_steps + steps

distance = math.sqrt(x ** 2 + y ** 2)

print("== FINAL RESULTS ==")
time.sleep(2)
print("Final position is : ", (x, y))
print("Total steps are : ", total_steps)
print("Distance travelled : ", distance, "metres")
