# Create a welcome message for the user
print("Welcome to The Color of Words!")
print("====================")
print("You have 6 attempts to guess the correct word.")
print("The word is SIX CHARACTERS long (which is why you get SIX tries)!")
print("So you MUST enter a guess of this length.")
print("If a letter is in the correct place, it will be green.")
print("If a letter is in the word, but NOT in the correct place,")
print("it will be yellow.")
print("If the letter is NOT in the word, it will be red.")
print()
# Create a function that prints out a letter with a colorful background 
from colorama import Fore, Back, Style

def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secret = actual

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secret):
      
      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
        
    # ...but if the letter is not in the word at all...
    else:
      
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# Write a Function that takes in a six-lettered word from the user
def userInput():
  # Create a variable that holds a default value for the users guess
  userGuess = ""
  
  # Continue to loop the users guess as long as it's NOT six characters
  while(len(userGuess) != 6):
    
    # Ask the user to enter a six letter word
    userGuess = input("Please enter a six letter word: ")
    print()
    
    # Return the users guess in lower case
  return userGuess.lower()
  
### Main Program ###
  
# Create a variable that stores the secret word
secretWord = "flames"

# Create a variable that counts the number of guess attempts
countTurns = 0

# Create a variable that holds the default value for the last attempt
lastTurn = ""

# Create a while loop that loops as long as the guess attempts are less than 6 and NOT the secret word
while countTurns < 6 and lastTurn != secretWord:

  # Prompt the user to enter a six letter word by calling the userInput function
  lastTurn = userInput()

  # Display the user's guess using the printGuessAccuracy function
  printGuessAccuracy(lastTurn, secretWord)
  print()
  print()

  # Increase the user's guess attempts by 1 
  countTurns += 1

    # If the user's attempts are less than six and do NOT equal the secret word,       display a message to the user that their guess is incorrect
  if(countTurns < 6 and lastTurn != secretWord):
    remainingTurns = 6 - countTurns
    print("Nice try, but your guess is incorrect.")
    print(f"Please try again.  You have {remainingTurns} turns left.")
    print()
  
# if guesses equals 6, display message to user that they've reached max attempts
if countTurns == 6:
    print("You've exceeded your max attempts.  Thanks for playing.")
  
# if user enters the correct word, display 'Good Job' message
if lastTurn == secretWord:
    print("GOOD JOB!")
  