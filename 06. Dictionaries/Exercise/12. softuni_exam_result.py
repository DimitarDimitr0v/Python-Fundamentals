command = input()

student_info = {}
submissions = {}

while not command == "exam finished":
    split = command.split("-")

    if "banned" in split[1]:
        username = split[0]
        for current_language, current_usernames in student_info.items():
            if username in current_usernames:
                del student_info[current_language][username]


    elif "banned" not in split:
        username = split[0]
        language = split[1]
        points = split[2]

        if language not in student_info:
            if username not in student_info:
                student_info[language] = {username: points}
                submissions[language] = 1

        elif language in student_info and username in student_info[language]:
            if points > student_info[language][username]:
                student_info[language][username] = points
                submissions[language] += 1
            else:
                submissions[language] += 1

        elif language in student_info and username not in student_info[language]:
            student_info[language][username] = points
            submissions[language] += 1


    command = input()


print(f"Results:")
for key, value in student_info.items():
    for name, point in value.items():
        print(f"{name} | {point}")

print(f"Submissions:")
for lang, count in submissions.items():
    print(f"{lang} - {count}")