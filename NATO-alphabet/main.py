import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
output = [phonetic_dict[letter] for letter in input("Enter a word: ").upper()]
print(output)
