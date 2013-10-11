#!/usr/bin/env python3
import pbkdf2


def genpass(password, *, nonce='', salt='', iterations=0x10000):
    '''
    >>> genpass('')
    '9G39QAZXnhIqc7y.3gF5fMbbG752/tve'
    >>> genpass('password', nonce='nonce', salt='salt', iterations=1)
    'ztWpkVwEFEmoWkX.7Vk6e5oFkVgFPTsh'

    '''
    result = pbkdf2.crypt('{}{}'.format(password, nonce),
                          salt=salt, iterations=iterations)
    return result.split('$')[4]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
