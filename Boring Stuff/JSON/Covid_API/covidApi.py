import json,requests,csv

r = requests.get("https://covid19-api.weedmark.systems/api/v1/stats")
source = json.loads(r.text)
#source=r.json()
print(source)

##with open('covid.json') as f:
##    source = json.load(f)

data = source['data']['covid19Stats']
#print(json.dumps(data,indent=2))

#print(len(data))
count={}

for city in data:
    country = city['country']
    confirmed = city['confirmed']
    deaths = city['deaths']
    recovered = city['recovered']
    if recovered ==None:
        recovered=0
    
    count.setdefault(country,{}).setdefault('confirmed',0)
    count.setdefault(country,{}).setdefault('deaths',0)
    count.setdefault(country,{}).setdefault('recovered',0)
    count[country]['confirmed']=count[country]['confirmed']+confirmed
    count[country]['deaths']=count[country]['deaths']+deaths
    count[country]['recovered']=count[country]['recovered']+recovered

print(len(count))
#print(json.dumps(count,indent=2))

with open('covid_output.json','w') as fw:
    fw.write(json.dumps(count,indent=2))

##with open('covid_output.csv','w') as f:
##    csv_writer=csv.writer(f,delimiter='-')
##    csv_writer.writerow(json.dumps(count,indent=2))
