import re

text = '''
http//www.www.google.com 
http//www.facebook.com 
http//www.yahoo.org 
'''

text1 = 'Hello\tPython world'
#print(text1)
print('Printing Text:',text1)
#pattern = re.compile(input('Enter Pattern:'))

##while True:
##    pattern = re.compile(input('Enter Pattern:'))
##    text=input('Enter String to be searched:')
##    matches = pattern.finditer(text)
##    for match in matches:
##        
##        print(match.group(0))
##        print(match.group(1))
##    
##
##    if input('Enter Space to end')==' ':
##        break

#'^([^\r\n]+[\r\n]+)[^\r\n]+'
pattern = re.compile('Hello[\t]+')

matches = pattern.finditer(text1)
for match in matches:
    print(match)
    print(match.group())
