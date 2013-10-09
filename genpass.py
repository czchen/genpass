#!/usr/bin/env python3
__all__ = ['gen_pass']


import pbkdf2


_ITERATIONS = 0x10000


def gen_pass(nonce, password):
    '''
    >>> gen_pass('', '')
    '9G39QAZXnhIqc7y.3gF5fMbbG752/tve'
    '''
    result = pbkdf2.crypt('{}{}'.format(password, nonce),
                          salt='', iterations=_ITERATIONS)
    return result.split('$')[4]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
