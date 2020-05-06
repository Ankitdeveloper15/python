'''#! python3'''

import pyperclip, sys, webbrowser,re

'''if len(sys.argv)>1:
    address= ' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()'''
while True:

    
    address = input('Give addresses separated by Comma:\n')

    if ',' in address:
        break
    else:
        if input('Is it single address. Enter (Y) for yes or (N) for entering again> ').upper()=='Y':
            break
        else: continue
        

addressList = address.split(',')

for i in range(len(addressList)):
    webbrowser.open('https://www.google.com/maps/place/'+addressList[i])
    #print(i)
