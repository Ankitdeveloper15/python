# Regular expression version for strip() function

# If no arguments passed to strip() then remove whitespaces from beginning and end.

# Otherwise characters specified as second argument in strip() will be removed from the string

import re

string_in = input("Enter the string")

char_rem  = input("Enter the character")

if char_rem=='':
        char_rem=' '

def regex_strip(string_in,char_rem):

        a = re.compile(r'^[%s]+|[%s]+$'%(char_rem,char_rem))
        #a = re.compile(r'%s'% char_rem)
     
    # sub(pattern,replace,string,max=0)
        match = a.findall(string_in)
        print(match)
        return a.sub('',string_in)

print (regex_strip(string_in,char_rem))


#print(string_in.strip(char_rem))
