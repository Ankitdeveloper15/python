
birthdays = {'ankit':'13th Feb', 'akshat':'17th Sep'}

print(birthdays.keys())

while True:

    print('Enter name for getting birthdays: (Blank to quit)')
    name=str.lower(input())
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birdthday of ' + name)
    else:
        print('I don not have birthday for ' + name + ' , What is their birth\
    day')
        bday= input()
        birthdays[name]=bday
        print('Database Updated')

    
