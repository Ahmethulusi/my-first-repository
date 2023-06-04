import random
from words import *
def play():
    category = random.choice(list(words.keys()))
   # word = get_word(category)
    word = random.choice(words[category])
    lifeCount = 5
    guessed =[]
   # word_display ="-"*(len(word))  bu da kullanılabilir   
    gameOver = False
    while not gameOver:
           # word_as_array = list(word)
            for letter in word:
                if letter.lower() in  guessed:
                    print(letter,end=" ")
                else:
                    print("_",end=" ")            
            print("")
            
            print(f"Clue (Bİr {category[:-3]})")
            guess = input(f"you have {lifeCount} life,Enter next guess:")
            guessed.append(guess.lower())
            
            if len(guess) == len(word) and guess.isalpha():
                if guess == word:
                    gameOver = True
                    break
            if guess.lower() not in word.lower() and guess.isalpha():
                lifeCount -=1
                if lifeCount == 0:
                    break
            gameOver = True
            for letter in word:
                if letter.lower() not in guessed:
                    gameOver = False
    if gameOver:
            print(word)
            print("Congratulations, you won!")
    else:
            print("Sorry mate, you lost! \n The word was %s" %(word))
def main():
    play()
    while True:
        if input("Do you want to play again ? (E/H)").upper() == "E":
            play()
        else:
            print("Thanks for playing!")
            break
main()

