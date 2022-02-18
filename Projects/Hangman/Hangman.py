import random


word_list = ["Clue", "Life", "Jesuita", "Loyola", "Iglesia", "Buenos Aires", "Bogota", "Quito", "loops", "Fajardo", "Orocovis", "Isabela", "Rincon", "Gurabo", "Ponce", "Bayamon", "Cayey", "Monopolio", "string", "list", "float", "Arecibo", "Dorado", "Luquillo"]



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


def get_word(word_list):
   word = random.choice(word_list)
   return word.upper()


def get_letter():
   letter = input("choose letter")


def play(word):
   word_completion = "_ "* len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 6
   print("Lets play")
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
