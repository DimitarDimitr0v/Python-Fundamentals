messenger = {}
capacity = int(input())
command = input()

while not command == 'Statistics':
    cmd_info = command.split('=')

    if cmd_info[0] == 'Add':
        username = cmd_info[1]
        sent_messages = int(cmd_info[2])
        received_messages = int(cmd_info[3])
        if username not in messenger.keys():
            messenger[username] = [0, 0]
            messenger[username][0] += sent_messages
            messenger[username][1] += received_messages
        command = input()

    elif cmd_info[0] == 'Message':
        sender = cmd_info[1]
        receiver = cmd_info[2]
        if sender in messenger.keys() and receiver in messenger.keys():
            messenger[sender][0] += 1
            if sum(messenger[sender]) >= capacity:
                print(f'{sender} reached the capacity!')
                messenger.pop(sender)
            messenger[receiver][1] += 1
            if sum(messenger[receiver]) >= capacity:
                print(f'{receiver} reached the capacity!')
                messenger.pop(receiver)
        command = input()

    elif cmd_info[0] == 'Empty':
        username = cmd_info[1]
        if username in messenger:
            messenger.pop(username)
        if username == 'All':
            messenger = {}
        command = input()

print(f'Users count: {len(messenger)}')

for (user, messages) in sorted(messenger.items(), key=lambda kvp: (-kvp[1][1], kvp[0])):
    print(f'{user} - {sum(messages)}')
