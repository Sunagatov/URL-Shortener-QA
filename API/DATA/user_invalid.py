# (first name, last name, email, password, country, age)

USER_EMAIL_EMPTY = [
    ('Ilya', 'Ilyin', '', '123456Qwerty!', 'Russia', 28)
]

USER_EMAIL_INVALID = [
    # email without @
    ('Ilya', 'Ilyin', '12345gmail.com', '123456Qwerty!', 'Russia', 28),

    # domain-less email
    ('Ilya', 'Ilyin', '12345@', '123456Qwerty!', 'Russia', 28),

    # with spaces in the email
    ('Ilya', 'Ilyin', '12345 @gmail.com', '123456Qwerty!', 'Russia', 28),

    # email beginning with “.”
    ('Ilya', 'Ilyin', '.12345@gmail.com', '123456Qwerty!', 'Russia', 28),

    # email ending with “.”
    ('Ilya', 'Ilyin', '12345@gmail.com.', '123456Qwerty!', 'Russia', 28),

    # email with “..”
    ('Ilya', 'Ilyin', '12345@gmail..com.', '123456Qwerty!', 'Russia', 28),
]

USER_EMAIL_LONG = [
    ('Ilya', 'Ilyin', 'mail@vOwMHeEWodFHcVaInngAkixEWDdT.mmnvudSGWjeHIHbJPecEF4gwX62xS.fkXJv4I365ylcfn7T4kvnCd91G9uz8OdH5RrNc6TsW.4AyHZg1FLNSTjjz1YO6IVHqE2v7pQLeGxySv0.asKIyyKSNxXLQqYakc0MfXoXIX8TQNX5.CKugWYrbcjYgchqzerhPGUM1ItNfTXYRbO.oT8Bk1Qnk6gCXg52Uwhqweeewwwwww5Dg5svDdAd5AxrFWazB.5P', '123456Qwerty!', 'Russia', 28)
]

USER_PASSWORD_EMPTY = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', '', 'Russia', 28)
]

USER_PASSWORD_SHORT = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'Pass1!', 'Russia', 28)
]

USER_PASSWORD_WITHOUT_UPPERCASE = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'password123!', 'Russia', 28)
]

USER_PASSWORD_WITHOUT_LOWERCASE = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'PASSWORD123!', 'Russia', 28)
]

USER_PASSWORD_WITHOUT_DIGITS = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'Password!', 'Russia', 28)
]

USER_PASSWORD_WITHOUT_SPEC_CHAR = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'Password123', 'Russia', 28)
]

USER_PASSWORD_WITH_SPACES = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'Pas sword123!', 'Russia', 28)
]

USER_PASSWORD_LONG = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'm8xSe8HYiZ2eVxTYUYXQmpmqNkbicXsyatIQLtCQftC3jlMvUM!', 'Russia', 28)
]

USER_PASSWORD_INVALID = [
    ('Ilya', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28)
]

USER_FIRST_NAME_EMPTY = [
    ('', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28)
]

USER_FIRST_NAME_INVALID = [
    ('Alex12', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28),
    ('Mel@man!', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28),
    ('Anna Gloria', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28)
]

USER_FIRST_NAME_LONG = [
    ('AnnanAnnanAnnanAnnanAnnanAnnanAnnanAnnanAnnanAnnana', 'Ilyin', '12345mailtest@gmail.com', 'Пароль123!', 'Russia', 28)
]
