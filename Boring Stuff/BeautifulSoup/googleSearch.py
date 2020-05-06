#! pyhthon3

import sys,bs4,webbrowser,requests,re

search = input('What do you want to search ?> ')

res = requests.get('https://www.google.com/search?q='+search)

try:
    res.raise_for_status
    #print(res.text[:100])
    soup = bs4.BeautifulSoup(res.text,"lxml")
    #print(soup.prettify())

    #results = soup.select('div[class="ZINbbc xpd O9g5cc uUPGi"]\
#> div.kCrYT > a div[class="BNeawe UPmit AP7Wnd"]')

    results = soup.select('div[class="ZINbbc xpd O9g5cc uUPGi"]\
> div.kCrYT > a[href]')

    urlNo = min(5,len(results))
    #print(urlNo)
    
    for i in range(0,urlNo):
    
        #print(f'No. of results: {len(result)}')
        #print(str(results[i]))
        try:
            link = results[i].get("href")
            pattern = re.compile(r'(http.*:[.\w/-]*)[%&]')
            url = pattern.findall(link)[0]
            #print(f'Link is: {link}')
            #print(f'URL is: {url}\n\n')
        except:
            url='https://www.google.com/search?q='+search
        #url = link.replace(f' {chr(8250)} ','/')
        #print(f'Url is: {url}')
        #print('ASCII value of (›) :',ord('›'))         # 8250: ASCII Value of (›)
        #print('Character for ASCII Value (8250) :',chr(8250)) 

        webbrowser.open(url)

    
    
except Exception as ex:
    print(f'Exception message is: {ex}')
