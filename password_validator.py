def password_characters(password: str):
    if 6 <= len(password) <= 10:
        return True
    return False


def password_alphanumeric(password:str):
    is_aplphanum = True

    for ch in password:
        if not (ch.isalpha() or ch.isnumeric()):
            is_aplphanum = False
            break

    return is_aplphanum


def password_digits_enough(password):
    digits = 0

    for ch in password:
        if ch.isdigit():
            digits += 1
    if digits >= 2:
        return True
    else:
        return False


def password_validation(password):
    is_valid = True

    if not password_characters(password):
        print('Password must be between 6 and 10 characters')
        is_valid = False
    if not password_alphanumeric(password):
        print('Password must consist only of letters and digits')
        is_valid = False
    if not password_digits_enough(password):
        print('Password must have at least 2 digits')
        is_valid = False
    if is_valid:
        print('Password is valid')


given = input()
password_validation(given)