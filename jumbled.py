import random

def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def play_word_jumble():
    words = ['python', 'hangman', 'computer', 'keyboard', 'mouse', 'gamer', 'programming']
    word_to_guess = random.choice(words)
    jumbled_word = jumble_word(word_to_guess)

    print("Welcome to Word Jumble!")
    print("Unscramble the letters to form a word.")
    print("Jumbled word:", jumbled_word)

    attempts = 0

    while attempts < 3:
        guess = input("Your guess: ").lower()
        if guess == word_to_guess:
            print("Congratulations! You've guessed the word correctly:", word_to_guess)
            return
        else:
            attempts += 1
            if attempts < 3:
                print("Incorrect guess. Try again!")

    print("\nSorry! You've used all your attempts.")
    print("The correct word was:", word_to_guess)

play_word_jumble()

