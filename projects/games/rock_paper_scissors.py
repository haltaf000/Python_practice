import random

computer_choice = random.randint(0, 2)
user_choice = int(input("Pick 0 for rock, 1 for paper, 2 for scissors: "))

while user_choice < 0 or user_choice > 2:
    user_choice = int(input("Pick 0 for rock, 1 for paper, 2 for scissors: "))

rock_paper_scissors = ['Rock', 'Paper', 'Scissors']

print(f"You chose {rock_paper_scissors[user_choice]}.")
print(f"Computer chose {rock_paper_scissors[computer_choice]}.")

if computer_choice == 0 and user_choice == 1:
    print(f"Computer Wins! {rock_paper_scissors[computer_choice]} beats {rock_paper_scissors[user_choice]}")
elif computer_choice == 0 and user_choice == 2:
    print(f"Computer Wins! {rock_paper_scissors[computer_choice]} beats {rock_paper_scissors[user_choice]}")
elif computer_choice == 2 and user_choice == 1:
    print(f"Computer Wins! {rock_paper_scissors[computer_choice]} beats {rock_paper_scissors[user_choice]}")
elif computer_choice == user_choice:
    print("It's a tie!")
else:
    print(f"You Win! {rock_paper_scissors[user_choice]} beats {rock_paper_scissors[computer_choice]}")