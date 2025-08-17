import random
words = ["apple", "banana", "grape", "mango", "peach"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6
print("Welcome to Hangman!")
while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter:"). lower()
    if guess in word:
        for i, letter in enumerate(word):

            if letter == guess:
                guessed[i] = guess
    else:
        tries  -= 1
        print(f"wrong!  {tries} tries left.")
if "_" not in guessed:
      print("you win! The word was:",word)
else:
    print("you lose! The word was:",word)                      
         

