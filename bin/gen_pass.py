#!/usr/bin/env python3
import getpass

import pbkdf2

ITERATIONS = 0x10000

TABLE = [
    {
        'name': 'google',
        'nonce': '2013-10-09: nonce for google',
    },
    {
        'name': 'dropbox',
        'nonce': '2013-10-09: nonce for dropbox',
    },
    {
        'name': 'keepass',
        'nonce': '2013-10-09: nonce for keepass',
    },
]

def get_nonce():
    for i in range(len(TABLE)):
        print('({}) {}'.format(i, TABLE[i]['name']))
    selection = getpass.getpass('Selection:')
    selection = int(selection)
    return TABLE[selection]['nonce']

def main():
    nonce = get_nonce()
    password = getpass.getpass('Enter password:')
    result = pbkdf2.crypt('{}{}'.format(password, nonce),
                          salt='',
                          iterations=ITERATIONS)
    result = result.split('$')[4]
    print('{}'.format(result))

if __name__ == '__main__':
    main()
