#!/usr/bin/env python3
import pbkdf2


def gen_pass(password, *, nonce='', salt='', iterations=0x10000):
    '''
    >>> gen_pass('')
    '9G39QAZXnhIqc7y.3gF5fMbbG752/tve'
    '''
    result = pbkdf2.crypt('{}{}'.format(password, nonce),
                          salt=salt, iterations=iterations)
    return result.split('$')[4]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
