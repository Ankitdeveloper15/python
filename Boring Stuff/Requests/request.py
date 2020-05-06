
import requests,bs4

##payload = {'page':2,'count': 25}
res = requests.get('http://httpbin.org/delay/2', auth=('ankit','pune'), timeout=3)

#dataPayload = {'username':'ankit','password':'testing'}
##res = requests.post('https://httpbin.org/post', data=dataPayload,params=payload)

#r = requests.get('https://moneycontrol.com')
#type(res)
#res.requests.codes.ok
#len(res.text)
#print(res.text[:250])

##print(res.headers)
##print(res.ok)
##print(res.encoding)

print(res.text)
#print(res.url)
