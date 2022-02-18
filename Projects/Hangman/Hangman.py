from curses.ascii import isalpha
import random


word_list = ["Clue", "Life", "Jesuita", "Loyola", "Iglesia", "Buenos Aires", "Bogota", "Quito", "loops", "Fajardo", "Orocovis", "Isabela", "Rincon", "Gurabo", "Ponce", "Bayamon", "Cayey", "Monopolio", "string", "list", "float", "Arecibo", "Dorado", "Luquillo"]


def display_hangman(tries):
      steps = ['''
     |---|
         |
         |
         |
        ===''', '''
     |---|
     O   |
         |
         |
       ===''', '''
    |---|
    O   |
    |   |
        |
       ===''', '''
    |---|
    O   |
   /|   |
        |
       ===''', '''
    |---|
    O   |
   /|\  |
        |
       ===''', '''
    |---|
    O   |
   /|\  |
   /    |
       ===''', '''
    |---|
    O   |
   /|\  |
   / \  |
       ===''']

      return steps[tries]



def get_word(word_list):
   word = random.choice(word_list)
   return word.upper()


def get_letter():
   letter = input("choose letter")
   return letter


def play(word):
   word_completion = "_ "* len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 6
   print("Lets play")
   print(display_hangman(tries))
   print(word_completion)
   print("\n")
   while not guessed and tries > 0:
      guess = input("Guess the word:").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
            print("already used that letter", guess)
         elif guess not in word:
            print(guess, "Not the word: (")
            tries -= 1
            guessed_letters.append(guess)
         else:
            print("Yes", guess, "that letter is in the word")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
               guessed = True
      elif len(guess) == len(word) and guess.isalpha():
         if guessed in guessed_words:
            print("already tried that", guess, "!")
         elif guess != word:
            print(guess, "Not the word: (")
            tries -= 1
            guessed_letters.append(guess)
         else:
            guessed = True
            word_completion = word
      else:
         print("Invalid input")
         print(display_hangman(tries))
         print(word_completion)
         print("\n")


         if guessed:
            print("Nice, you got the word correct!! :)")
         else:
            print("No more tries left. The correct word"+word+" Better luck next time.")

         
