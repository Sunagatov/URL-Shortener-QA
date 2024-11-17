PASSWORD_INVALID = [
    # less 8 characters
    'Pass1!',

    # longer 50 characters
    'Password12345Password12345!Password12345Password123',

    # without uppercase
    'password123!',

    # without lowercase
    'PASSWORD123!',

    # without digits
    'Password!',

    # with spaces
    'Pas sword123!',

    # with invalid characters
    'Пароль123!'
]
