import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    try:
        output = [phonetic_dict[letter] for letter in input("Enter a word: ").upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)
