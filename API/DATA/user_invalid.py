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
