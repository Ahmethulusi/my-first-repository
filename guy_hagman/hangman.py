import random
from words import word_list
"""
def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_display ="-"*(len(word))
    guessed = False
    guessed_letters =[]
    guessed_words =[]
    tries = 6
    print("hadi başlayalım. %d hakkın var." %(tries))
    print(word_display)
    print("\n")
    
    while not guessed and tries >0:
        guess = input("Tahminde bulunun : ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("%s harfini daha önce denediniz." %(guess))
            elif guess not in word:
                tries -=1
                print("%s harfi kelimede yok.%d hakkın kaldı" %(guess,tries))
                guessed_letters.append(guess)
            else:
                print("%s harfi kelimede var." %(guess))
                guessed_letters.append(guess)
                word_as_array =list(word_display)
                indices =[i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_array[index] = guess
                word_display ="".join(word_as_array)
                if "_" not in word_display:
                    guessed = True
                    
        elif len(guess) ==  len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_display = word
            elif guess in guessed_words:
                print("%s kelimesini daha önce denediniz."%(guess))
            else:
                print("%s kelimesi doğru cevap değil. "%(guess))
                guessed_words.append(guess)
                tries -=1

        else:
            print("Geçersiz tahmin!")
        print(word_display)
        print("\n")
    if guessed:
        print("tebrikler, Bildiniz.")
    else:
        print("Maalesef olmadı. Doğru cevap : %s" %(word))

def main():
    word = get_word()
    play(word)
    
    while input("Tekrar oynamak ister misiniz ? (E/H)").upper() == "E":
        word = get_word()
        play(word)
    
main()
"""

word = random.choice(word_list).lower()

lifeCount = 5
guessed =[]

gameOver = False

while not gameOver:
    for letter in word:
        if letter.lower() in  guessed:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")
    
    guess = input(f"you have {lifeCount} life,Enter next guess: ")
    guessed.append(guess.lower())
    
    if len(guess) == len(word) and guess.isalpha():
        if guess == word:
            gameOver = True


    if guess.lower() not in word.lower():
        lifeCount -=1
        if lifeCount == 0:
            break
        
        
    gameOver = True
    for letter in word:
        if letter.lower() not in guessed:
            gameOver = False

if gameOver:
    print("Congratulations, you won!")
else:
    print("Sorry mate, you lost!")