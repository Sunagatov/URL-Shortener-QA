import pytest


# (first name, last name, email, password, country, age)
USER_VALID = [
    ('A', 'A', 'mail123mail@ma123il.ru', '12345Qw!', 'B', 13),
    ('Ilya', 'Ilya', 'ZoxBfhLiynUuhzFxTdrtqzsTIqbsA4er8yeemYakgmHpvyCW3cXYu2oFT43dt50Q@mail.ru', '1234567Qwerty$',
     'France', 28),
    pytest.param(('iilGQgcrJpGkWHDQIPpzjGowkxVXwcEADCckNUDqsTwPeeVQMw',
                  'iilGQgcrJpGkWHDQIPpzjGowkxVXwcEADCckNUDqsTwPeeVQMw',
                  'mail@vOwMHeEWodFHcVaInngAkixEWDdT.mmnvudSGWjeHIHbJPecEF4gwX62xS.fkXJv4I365ylcfn7T4kvnCd91G9uz8OdH5RrNc6TsW.4AyHZg1FLNSTjjz1YO6IVHqE2v7pQLeGxySv0.asKIyyKSNxXLQqYakc0MfXoXIX8TQNX5.CKugWYrbcjYgchqzerhPGUM1ItNfTXYRbO.oT8Bk1Qnk6gCXg52Uwh5Dg5svDdAd5AxrFWazB.5P',
                  '9BUYjF4hGiMGpbBGdoSwWVh2IuZ80K1EZwHepQWLedzwbsIzo%',
                  'OIcEYgBptFcrLVBOdebBzCfzBpFLxPnHaxwsMLCickFgFrIHTw', 120),
                 marks=pytest.mark.xfail(reason="Bug: https://shorty-url.atlassian.net/browse/SHORTY-79", run=True)),
    pytest.param(('Ilya-Petya', 'Ilya-Petya', 'mail_mail@mail.ru', '1234567Qwerty$', 'Russian Federation', 28),
                 marks=pytest.mark.xfail(reason="Bug: https://shorty-url.atlassian.net/browse/SHORTY-80", run=True)),
    ("Ilya'Petya", "Ilya'Petya", 'mail-mail@mail.ru', '1234567Qwerty$', 'France', 28),
    ("Ilya-Petya'Vova", "Ilya-Petya'Vova", 'mail+mail@mail.ru', '1234567Qwerty$', 'France', 28),
    ('Ilya', 'Ilya', 'mail@m1OlTXt9tJvS0mZGBVL36zlp3NWRA7O47SUGdyrjk2sAUCnAKEKUFljHCia9W8l.com',
     '1234567Qwerty$', 'France', 28),
    ('Ilya', 'Ilya', 'mail@mail-mail.ru', '1234567Qwerty$', 'France', 28)
]
