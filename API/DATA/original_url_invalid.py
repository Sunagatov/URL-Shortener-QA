import pytest

ORIGINAL_URL_INVALID = [
    ('http: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.EP',
     'URL is too long'),
    ('',
     'URL must not be empty or blank'),
    (' ',
     'URL must not be empty or blank'),
    ('https://ic. ed-la. tte.uk/',
     'URL must not contain spaces'),
    ('http://.com',
     'URL must have a valid host'),
    pytest.param('https://',
                 'URL must have a valid host',
                 marks=pytest.mark.xfail(reason='Bug (https://shorty-url.atlassian.net/browse/SHORTY-23) '
                                                'is not fixed')),
    ('ftp://example.com/file',
     'URL must use HTTP or HTTPS protocol')
]
