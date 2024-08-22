import random
import string
import sys

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
SURNAMES = ["dos Santos", "da Silva", "Peixoto", "Oliveira", "Sales", "Pereira", "Ferreira", "Almeida", "Souza", "Costa", "Sauro"]

def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

def generate_name(length):
    word = generate_word(length)
    surname = random.choice(SURNAMES)
    return f"{word.capitalize()} {surname}"

if __name__ == "__main__":
    try:
        count = int(sys.argv[1])
    except:
        count = 5

    try:
        length = int(sys.argv[2])
    except:
        length = 6

    for i in range(count):
        print(generate_name(length))