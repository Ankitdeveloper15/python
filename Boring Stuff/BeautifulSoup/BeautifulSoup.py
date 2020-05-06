
import requests,bs4

#res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
#r = requests.get('https://moneycontrol.com')
#type(res)
#res.requests.codes.ok
#len(res.text)
#print(res.text[:250])
try:
    #r.raise_for_status()
    
    html_file = open('./simple.txt','r')
##    for chunk in r.iter_content(100000):
##        requestFile.write(chunk)

    with open('./Beautifuldata.txt','w') as dataFile:pass  # to clear contents of file before appending
    
    soup=bs4.BeautifulSoup(html_file,'html.parser')
    #print(soup.prettify())
    
    #for elem in soup.select('div.article'):
    for elem in soup.select('div[class="article"]'):
    #for elem in soup.find_all('div', class_='article'):
    #elems = soup.find('.article')
        
        print(elem.attrs)
        print(f'{type(elem)}\n')
        print(f'{str(elem)}\n')
        
        heading = elem.find('h2').text
        summary = elem.find('p').getText()
        
        print(f'Printing Heading: {heading}\nPrinting Summary: \
{summary}\n\n')

        with open('./Beautifuldata.txt','a') as dataFile:
            dataFile.writelines(f'{heading}\t')
            dataFile.writelines(f'{summary}\n')
    #status=[]
    #for elem in elems:
        #print(elem.getText())
        #print(elem.attrs)
        #print(str(elem))
        #status.append(elem.getText().isspace())
        #print(status)
        #input('Continue > ')
        #print(str(elem))
##        if elem.getText().isspace:
##            pass
##            print(str(elem))
##            print(elem.getText())
##        else:
##            print('Text of element without space',elem.getText())


    ##print(status)
    html_file.close()
except Exception as exc:
    print('There was a problem: %s' % (exc))
