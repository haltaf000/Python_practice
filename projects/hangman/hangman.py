import random
import projects.hangman.word_list as word_list

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6


chosen_word = random.choice(word_list.word_list)

print(chosen_word)

place_holder = ""

for letter in range(len(chosen_word)):
    place_holder += "_"

print(place_holder)

all_correct = False
letter_list = []

while not all_correct:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    user_choice = input("Please guess a letter: ").lower()


    if user_choice in letter_list:
        print("You already guessed this letter!")

    display = ""

    for char in chosen_word:
        if char == user_choice:
            display += char
            letter_list.append(user_choice) 
        elif char in letter_list:
            display += char
        else:
            display += "_"

    if user_choice not in chosen_word:
        print(f"You guessed {user_choice}. that's not in the word. You lose a life!")
        lives -= 1

        if lives == 0:
            all_correct = True
            print(f"***********************YOU LOSE -> The correct word was {chosen_word}**********************")


    if "_" not in display:
        all_correct = True
        print('You Win!')

    print(display)
    print(stages[lives])
    