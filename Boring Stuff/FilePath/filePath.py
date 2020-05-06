# Mad libs 

# Reading text files and let user add their own text anywhere the word adjective,noun,verb or adverb appears

import os

word = ['adjective','adverb','noun','verb']
fileName = 'write.doc'
print(os.path.basename(os.path.abspath('..')))
print(os.path.dirname(os.path.abspath('..')))
print(os.path.split(os.path.abspath('..')))   ## This will give tuple of dirname and basename
print(os.path.abspath('..').split(os.path.sep)) ## This will give list of all components of path
#print(fileName.endswith('.doc'))               ## separated by file separator

##list = ['adjective','ankit','noun','verb']
##for i in list:
##        print(f'i in list is {i} and index of i is {list.index(i)}.')
##        if i in word:
##                list[list.index(i)]=input(f'Enter the {i}> ')
##        else: pass
##print(list)


### Listing all the '.txt' files present in current working directories
##for filename in os.listdir('.'):
##        key =  []
##        if filename.endswith('.txt'):
##                f = open(filename,'r')
##                #print(filename)
##                # Print the content of text files for easyness
##                for line in f:
##                        #text = f.readline()
##                        textList = line.strip('\n').rsplit(' ')
##                        print(textList)
##
### Loop through read object for searching the word and appending it with user input
##                        for i in textList:
##                                #print('Value of i: ',i)
##                                if i in word:
##                                      textList[textList.index(i)]=(input("Enter the {0}:".format(i)))
##                                else: pass
##                                      #key.append(i)
##                        key = key+textList
##
##        print('Final Key: ',' '.join(key))
##
##### Writing all the words to the file and saving it
####file_object1 = open(filename,'w')
####file_object1.write(''.join(key))
####file_object1.close()



