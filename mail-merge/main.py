NAME_PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as draft:
    draft_letter = draft.read()

with open("Input/Names/invited_names.txt") as names_file:
    invited_names = names_file.read().split("\n")

for name in invited_names:
    with open(f"Output/ReadyToSend/letter_for_{name.title()}.txt", mode="w") as output:
        output.write(draft_letter.replace(NAME_PLACEHOLDER, f"{name.title()}"))
