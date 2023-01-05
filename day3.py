# Goal: To create a choose your own adventure game using conditionals.
# Depending on the user's input, there will be different outcomes.

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

firstDecision = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()

if firstDecision != 'left' :
  print("Fall into a hole. Game over.")
else :
  secondDecision = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

  if secondDecision != 'wait' :
    print("Attacked by trout. Game over.")
  else :
    thirdDecision = input("You come across a set of three colored doors. Which door do you go through? Red, blue or yellow?\n").lower()

    if thirdDecision == 'red' :
      print("Burned by fire. Game over.")
    elif thirdDecision == 'yellow' :
      print("You win!")
    elif thirdDecision == 'blue' :
      print("Eaten by beasts. Game over.")
    else :
      print("Game over.")