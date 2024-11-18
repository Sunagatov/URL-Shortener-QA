EMAIL_INVALID = [
    # email without @
    '12345gmail.com',

    # domain-less email
    '12345@',

    # with spaces in the email
    '12345 @gmail.com',

    # email beginning with “.”
    '.12345@gmail.com',

    # email ending with “.”
    '12345@gmail.com.',

    # email with “..”
    '12345@gmail..com.',

    # email longer than 64 characters
    '152345123545123451234512345123451234512345123451234QWer@gmail.com',

    # email less than 7 characters
    'x@x.xx'
]
