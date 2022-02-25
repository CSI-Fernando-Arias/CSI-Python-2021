import random

#All words that can be guessed in my hangman
word_list = ["CLUE", "LIFE", "JESUITA", "LOYOLA", "IGLESIA", "BUENOS AIRES", "BOGOTA", "QUITO", "LOOPS", "FAJARDO", "OROCOVIS", "ISABELA", "RINCON", "GURABO", "PONCE", "BAYAMON", "CAYEY", "MONOPOLIO", "STRING", "LIST", "FLOAT", "ARECIBO", "DORADO", "LUQUILLO"]
#All hangman steps
def showHangman(tries):
               
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

#Every letter I cant use or not possible to use
incompleteLetters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

#Selecting a word from my word list
def get_word():
   word = random.choice(word_list)
   return word.upper()


def getInput():
   Letter = input("Select letter")
   while(Letter.upper() not in incompleteLetters):
      print("Error")

#Start playing hangman 
def play(word):
   wordSpaces = "-" * len(word) 
   guessed = ()
   guessedLetters = []  #This code is for every letter that is guessed 
   guessedWords = []
   tries = 6   #Amount of tries
   print("Vamos a jugar Hangman")
   print("No use of lowercase, Upper Case only")
   print(showHangman(tries))#This will show or display the hangman when I run the code
   print(wordSpaces)#This code will make it show the spaces of each word

   while not guessed and tries > 0:
         guess = input("Guess the word:").upper()
   if len(guess) == 1 and guess.isalpha():
         if guess in guessedLetters:
            print("already used that letter", guess)
         elif guess not in word:
            print(guess, "Not the word: (")
            tries -= 1
            guessedLetters.append(guess)
         else:
            print("Yes", guess, "that letter is in the word")
            guessedLetters.append(guess)
            word_as_list = list(wordSpaces)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
               guessed = True
   elif len(guess) == len(word) and guess.isalpha():
         if guessed in guessedWords:
            print("already tried that", guess, "!")
         elif guess != word:
            print(guess, "Not the word: (")
            tries -= 1
            guessedLetters.append(guess)
         else:
            guessed = True
            word_completion = word
   else:
        
         if guessed:
            print("Nice, you got the word correct!! :)")
         else:
            print("No more tries left. The correct word"+word+" Better luck next time.")

play(get_word())