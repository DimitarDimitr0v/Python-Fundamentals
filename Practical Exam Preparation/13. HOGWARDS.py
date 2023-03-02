spell = input()
command = input()

while not command == 'Abracadabra':
    cmd_info = command.split()

    if cmd_info[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)

    elif cmd_info[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)

    elif cmd_info[0] == 'Illusion':
        index = int(cmd_info[1])
        letter = cmd_info[2]
        if 0 <= index < len(spell):
            spell = list(spell)
            spell[index] = letter
            spell = str(''.join(spell))
            print('Done!')
        else:
            print('The spell was too weak.')

    elif cmd_info[0] == 'Divination':
        first_substring = cmd_info[1]
        second_substring = cmd_info[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif cmd_info[0] == 'Alteration':
        substring = cmd_info[1]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)

    else:
        print('The spell did not work!')

    command = input()
