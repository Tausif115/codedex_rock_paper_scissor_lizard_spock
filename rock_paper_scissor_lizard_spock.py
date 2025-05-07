import random

player = int(input("Rock Paper Scissors Lizard Spock\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\nPick a number: "))
computer = random.randint(1, 5)

print("Your chose: ", end = " ")
if player == 1:
    print("✊")
elif player == 2:
    print("✋")
elif player == 3:
    print("✌️")
elif player == 4:
    print("🦎")
elif player == 5:
    print("🖖")

print("CPU chose: ", end = " ")
if computer == 1:
    print("✊")
elif computer == 2:
    print("✋")
elif computer == 3:
    print("✌️")
elif computer == 4:
    print("🦎")
elif computer == 5:
    print("🖖")

if player == computer:
    print("Tie")
elif (player == 3 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 4) or (player == 4 and computer == 5) or (player == 5 and computer == 3) or (player == 3 and computer == 4) or (player == 4 and computer == 2) or (player == 2 and computer == 5) or (player == 5 and computer == 1) or (player == 1 and computer == 3):
    print("The player won!")
else:
    print("The CPU won!")






























