import random

# -------------------------------
# HANGMAN GAME
# -------------------------------

# List of predefined words
words = ["python", "apple", "tiger", "school", "computer"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0

# Maximum incorrect guesses allowed
max_wrong_guesses = 6


print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player has won
    if "_" not in display:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        print("You Win! 🏆")
        break

    print("\nGuessed letters:", guessed_letters)
    print("Wrong guesses remaining:", max_wrong_guesses - wrong_guesses)

    # Take input from user
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    # Add guessed letter to list
    guessed_letters.append(guess)

    # Check correct or incorrect guess
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Game over condition
if wrong_guesses == max_wrong_guesses:
    print("\n" + "=" * 40)
    print("           GAME OVER!")
    print("=" * 40)
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman Game!")
