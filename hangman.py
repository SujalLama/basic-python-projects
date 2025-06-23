import random

words = [
    "apple",
    "banana",
    "cat",
    "dog",
    "elephant",
    "flower",
    "grape",
    "house",
    "ice",
    "jungle",
    "kite",
    "lemon",
    "monkey",
    "notebook",
    "orange",
    "pencil",
    "queen",
    "river",
    "sun",
    "tree",
    "umbrella",
    "violin",
    "water",
    "xylophone",
    "yacht",
    "zebra",
    "ant",
    "bird",
    "cloud",
    "door",
    "eagle",
    "fish",
    "garden",
    "hat",
    "island",
    "jacket",
    "kangaroo",
    "lamp",
    "mountain",
    "nest",
    "ocean",
    "panda",
    "quilt",
    "road",
    "snake",
    "tiger",
    "unicorn",
    "village",
    "whale",
    "x-ray",
    "yogurt",
    "zoo",
    "art",
    "book",
    "candle",
    "desk",
    "engine",
    "forest",
    "glass",
    "hammer",
    "idea",
    "jewel",
    "king",
    "lake",
    "music",
    "night",
    "owl",
    "pizza",
    "quiet",
    "rose",
    "star",
    "table",
    "universe",
    "vase",
    "window",
    "xenon",
    "yard",
    "zipper",
    "arrow",
    "bottle",
    "circle",
    "dance",
    "energy",
    "feather",
    "gift",
    "hill",
    "ink",
    "jungle",
    "key",
    "leaf",
    "mirror",
    "needle",
    "oxygen",
    "parrot",
    "queen",
    "ring",
    "ship",
    "ticket",
    "uniform",
    "valley",
]


def random_word():
    return random.choice(words)


def letter_check(words, guessLetter):
    indexes = [{i: c} for i, c in enumerate(words) if c == guessLetter]
    return indexes


def replace_chars(words, replacements):
    # Strings are immutable, so convert to list
    word_list = list(words)

    for replacement in replacements:
        for key, new_char in replacement.items():
            if 0 <= key < len(word_list):
                word_list[key] = new_char

    return "".join(word_list)


def checkWord(chosen_word):
    user_input_char = input("\nGuess a letter : ")
    replacements = letter_check(chosen_word, user_input_char)
    return replacements


def process_game(chosen_word, masked_word, attempt=0):
    attempts = attempt
    replacements = checkWord(chosen_word)
    if not replacements:
        if attempts >= 3:
            print("You tried for 3 times, You lost the game")
            return
        attempts += 1
        print(f"Failed attempts: {attempts}\n")
        process_game(chosen_word, masked_word, attempts)
    else:
        new_word = replace_chars(masked_word, replacements)
        masked_word = new_word
        if new_word == chosen_word:
            print(f"You guessed the word right: {chosen_word}")
            attempts = 0
            return
        print(f"The word so far: {new_word}")
        process_game(chosen_word, masked_word, attempts)


def give_random_clue(chosen_word, masked_word):
    random_ind = random.randint(0, len(chosen_word))
    chosen_char = list(chosen_word)[random_ind]
    return replace_chars(masked_word, [{random_ind: chosen_char}])


while True:
    chosen_word = random_word()
    masked_word = "_" * len(chosen_word)

    # give the clue for one random char
    masked_word = give_random_clue(chosen_word, masked_word)

    print("\nLet's begin hangman.\n")
    print(f"The word is of length {len(chosen_word)} : {masked_word} \n")
    process_game(chosen_word, masked_word)
