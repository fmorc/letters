
with open('./Input/Letters/starting_letter.txt') as letter:
    template = letter.read()

with open('./Input/Names/invited_names.txt') as invited:
    invited_names = invited.readlines()
    for name in invited_names:
        with open(f'./Output/ReadyToSend/letter_{name}.txt', 'w') as new_file:
            new_file.write(template.replace('[name]', name.split('\n')[0]))
            print(f'created new file: letter_{name}')
