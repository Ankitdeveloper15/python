# Various ways to write print

mLine = '''
This is
multiplin"e
line'''

third_way = "third way"

prompt='Enter input > '


print('This is another way to get input in print',input(prompt))

print('This is first way of print', prompt)

print('This is second way of print' + mLine)

print(f'This is {third_way} way of print')

print('This is {1} of {0} of print'.format(third_way,'2nd version'))

print('This is %s of %s' % ('2nd version',third_way))
