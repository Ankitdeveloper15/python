#! python3
''' This is called shebang line.
this is to run program from command line'''

import pyperclip, sys

Passwords = {'hdfcbank': 'hdfcank2020',
             'yesbank':'yesank1984',
             'axisbank':'ankaxis@84'}

if len(sys.argv)<2:
    print('Please pass one argumant as account name')
    sys.exit()
    
account=sys.argv[1]

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Password for ' + account + ' is copied')
else:
    print(account + ' is not in password list')


