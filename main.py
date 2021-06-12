import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# using dict comprehension method
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}
# print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
