import random


def get_random():
    random_num = random.randint(1, 11)
    return random_num


while True:
    user_input = input("Please guess the number between 1 to 10 \n")
    random_num = get_random()
    if random_num == int(user_input):
        print(f"You guessed the right number. The number is {random_num}\n")
    else:
        print(f"You guessed the wrong number. The number is {random_num}\n")
