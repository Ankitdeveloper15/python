

import sys

##str_original = '—OQ‚)êšÙx²àåÓã²Œke7TU$¬GÁ„õÁõÓ^'
##bytes_encoded = str_original.encode(encoding='utf-8')
##print(type(bytes_encoded))
##
##str_decoded = bytes_encoded.decode()
##print(type(str_decoded))
##
##print('Encoded bytes =', bytes_encoded)
##print('Decoded String =', str_decoded)
##print('str_original equals str_decoded =', str_original == str_decoded)
##
###fileName = input('Give file name: > ')
###fileName = 'ex15text.txt'
fileName = 'ex15write.txt'

with open(fileName,'wb') as f:
##    print(f.read(10))
##    print(f.truncate(20))
##    print(f'Text of file is:\n{f.readline()}',end='')
##    print(f.tell())
##    print(f.seek(90,0))
##    print(f.tell())
    #print(f.readlines(),end='')
##    print('List(f): ',list(f))
##    for i in f:
##        print(i,end='')
##    while 1:
##        line=f.readline()
##        if not line: break
##        print(line,end='')
    
##    value = ['the answer',42]
    newFile = open('file.pdf','rb')
    data = newFile.read()
    print(data)

    f.write(data)
    newFile.close()
##    print(f.seek(0,0))
##    print(f.read())
