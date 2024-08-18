# previous learned concepts:
# machine learning - linear/polynomial regression, SVM, etc

# actual programming problem that involves AI game of rock, paper, scissors where the computer always wins

# finding the hidden patterns within a game is the key to winning

# in this FIRST EXAMPLE using random creates random choices for the computer and the player but only provides a ~%33 of either player to win, which is not a very efficient AI player

import random

for i in range(5):
  print("Game", i+1)
  comp = random.randint(1,3) # generates a number from 1 to 3
  user = int(input("Please enter a number: 1) Rock 2) Paper or 3) Scissors: ")) # ask the user to input a number

  if comp == 1 and user == 1:
    print("It's a tie!")
    
  elif comp == 1 and user == 2:
    print("The user wins!")
    
  elif comp == 1 and user == 3:
    print("The comp wins!")  
  
  elif comp == 2 and user == 1:
    print("The comp wins!")
    
  elif comp == 2 and user == 2:
    print("It's a tie!")
    
  elif comp == 2 and user == 3:
    print("The user wins!")
  
  elif comp == 3 and user == 1:
    print("The user wins!")
    
  elif comp == 3 and user == 2:
    print("The comp wins!")
    
  elif comp == 3 and user == 3:
    print("It's a tie!!")