import re


def length_validator(username: str):
    if 3 <= len(username) <= 16:
        return True

    return False


def contains_validator(username: str):
    symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '.', '/', ':', ';', '<', '=', '>', '?', '@',
               '[', ']', '^', '`', '{', '|', '}', '~']

    for x in symbols:
        if x in username:
            return False

    return True


usernames = input().split(", ")
valid_usernames = []


for current_username in usernames:
    if length_validator(current_username):
        if contains_validator(current_username):
            valid_usernames.append(current_username)

for el in valid_usernames:
    print(el)
