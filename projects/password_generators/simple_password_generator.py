import random
print('Welcome to the Password Generator!')


letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["!", "@", "#", "$", "%", "&", "*", "(",")"]

num_of_letters = int(input("How many letters would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))
num_of_symbols = int(input("How many symbols would you like? "))


password_choices = []


for i in range(num_of_letters):
    password_choices.append(random.choice(letters))

for i in range(num_of_numbers):
    password_choices.append(str(random.choice(numbers)))

for i in range(num_of_symbols):
    password_choices.append(random.choice(symbols))

random.shuffle(password_choices)

password = ""

for i in password_choices:
    password += i


print(password_choices)
print(password)