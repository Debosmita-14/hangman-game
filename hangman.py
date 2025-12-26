import random
random.choice(["APPLE","BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "HONEYDEW"])
word=random.choice(["APPLE","BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "HONEYDEW"])
blank=["_"]*len(word)
print(" ".join(blank))
print("Welcome to the word guessing game!")
print("Try to guess the word letter by letter.")
print("You can guess one letter at a time.")
print("Let's start!")
print("The word has", len(word), "letters.")
guessed_letters = []
lives = len(word) + 3 

while "_" in blank:
        guesses=input("enter a letter").upper()
        if not guesses.isalpha() or len(guesses) != 1:
         print("Please enter only one letter (A-Z).")
         continue

    
        if guesses in guessed_letters:
         print("You already guessed that letter. Try again.")
         continue
        guessed_letters.append(guesses)
        if guesses in word:
            for i in range(len(word)):
                if word[i]==guesses:
                    blank[i]=guesses
            print("Good guess"," ".join(blank))
        else:
            print("wrong guesses"," ".join(blank))
print("Congratulations! You've guessed the word:", word)
print("Game Over!")

        
    



