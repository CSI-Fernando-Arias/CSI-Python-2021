import random 

#All words thats can be used in my hangman
word_list = ["CLUE", "LIFE", "JESUITA", "LOYOLA", "IGLESIA", "BUENOSAIRES", "BOGOTA", "QUITO", "LOOPS", "FAJARDO", "OROCOVIS", "ISABELA", "RINCON", "GURABO", "PONCE", "BAYAMON", "CAYEY", "MONOPOLIO", "STRING", "LIST", "FLOAT", "ARECIBO", "DORADO", "LUQUILLO"]
#Every step in hangman
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

#This code is to select a random word from my word list
def getWord(word_list):
    word = random.choice(word_list)
    return word.upper()
#This is a list of the letters I cant use
incompleteLetters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

#This code is going to print an error if I select a letter thats is in my list of incomplete letters and going to make it a upper case letter.
def getInput():
   Letter = input("Select letter")
   while(Letter.upper() not in incompleteLetters):
      print("Error")
#To start playing
def play(word):
    word_completion = "-" * len(word) #This will show me the amount of spaces the letter chosen has
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 #amount of tries to guess the word chosen
    print("Lets play Hangman")
    print("No use of lowercase, must be Upper Case letters always.")
    print(display_hangman(tries))#Print the steps so you see how much tries you have left 
    print(word_completion)#prints the spaces of the letter
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already used that letter", guess, "!")
            elif guess not in word:
                print(guess, "Not the word :(")     
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
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guessed in guessed_words:
                print("Already tried that", guess,)
            elif guess != word:
                print(guess, "Not the word : (")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    #I use an if else that tells me either you got the correct word or you ran out of opportunities.
    if guessed:
        print("You got the word correct")
    else: 
        print("No more tries left. The correct word"+word+" Better luck next time.")
                
    
def main():
    word = getWord(word_list)
    play(word)
    while input("Go again (Y/N)").upper() == "Y":
        word = getWord(word_list)
        play(word)

if __name__ == "__main__":
    main() 