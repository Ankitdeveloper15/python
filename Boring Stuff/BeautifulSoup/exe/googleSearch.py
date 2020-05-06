#! pyhthon3

import sys,bs4,webbrowser,requests,re

search = input('What do you want to search ?> ')

res = requests.get('https://www.google.com/search?q='+search)

try:
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text,"lxml")

    results = soup.select('div[class="ZINbbc xpd O9g5cc uUPGi"]\
> div.kCrYT > a[href]')

    urlNo = min(5,len(results))
    
    for i in range(0,urlNo):
    
        try:
            link = results[i].get("href")
            pattern = re.compile(r'(http.*:[.\w/-]*)[%&]')
            url = pattern.findall(link)[0]

        except:
            url='https://www.google.com/search?q='+search
            
        webbrowser.open(url)

    
    
except Exception as ex:
    print(f'Exception message is: {ex}')
