import random
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 to 100")

num = random.randint(1, 100)

def number_guess():

    difficulty = input("Chose your difficulty: Type 'easy' or 'hard': ")

    lives = 0

    if difficulty == 'easy':
        lives = 10
        print("You have 10 lives to guess my number")
    else:
        lives = 5
        print("You have 5 lives to guess my number")

    play = True
    guesses = []


    while lives != 0 and play:
        guess = int(input("Chose a number between 1 through 100: "))

        if guess in guesses:
            print("You already tried that number, guess again")
            continue
        guesses.append(guess)

        if guess == num:
            print(f"You guessed my number {num}! CONGRATS!")
            play = False
            continue
        elif guess < num:
            print("Your guess is low!")
            lives -= 1
            print(f"You have {lives} lives remaining!")
        elif guess > num:
            print("Your guess is high!")
            lives -= 1
            print(f"You have {lives} lives remaining!")


        if lives == 0:
            print(f"Sorry, you are out of lives! My numbery was {num}")

number_guess()

