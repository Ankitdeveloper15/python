import requests

rsong = requests.get('http://api.pendusaab.com/download/128k-aeurl/Akela-Hai-Mr.-Khiladi.mp3')
rimage = requests.get('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg')
#print(r.content)

with open('image.jpg','wb') as f:
    f.write(rimage.content)

with open('Akela khiladi.mp3','wb') as f:
    f.write(rsong.content)
    
