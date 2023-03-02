def password_length_check(password: str):
    if 6 <= len(password) <= 10:
        return True
    else:
        print(f"Password must be between 6 and 10 characters")
        return False


def password_alphanumeric_check(password: str):
    if password.isalnum():
        return True
    else:
        print(f"Password must consist only of letters and digits")
        return False


def password_digit_check(password: str):
    digits = 0
    for el in password:
        if el.isdigit():
            digits += 1

    if digits >= 2:
        return True
    else:
        print(f"Password must have at least 2 digits")
        return False


password_input = input()

length_correct = password_length_check(password_input)
symbol_correct = password_alphanumeric_check(password_input)
digit_correct = password_digit_check(password_input)

if length_correct and symbol_correct and digit_correct:
    print(f"Password is valid")


