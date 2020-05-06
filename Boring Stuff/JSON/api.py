import json,requests,csv

#payload ={'country':'India'}
#r = requests.get("https://covid19-api.weedmark.systems/api/v1/stats", params=payload)

url ="https://restcountries-v1.p.rapidapi.com/all"
headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "fbc33d6e3dmsh8874840b1c0f958p182f66jsn5bb2f38f931a"
    }

payload = {"query":"Pune"}

r = requests.get(url,headers=headers)
source = json.loads(r.text)
#source=r.json()

#jsonData = json.dumps(source,indent=2)
##for country in source:
##    if country['name']=='India':
##        print(json.dumps(country,indent=2))


count={}
info=[]

for country in source:
    countryName = country['name']
    population = country['population']
    isdCode = country['callingCodes']

##    print(isdCode)
##    print(population)
##    print(countryName+'\n')

    
    count['name'] = countryName
    count['population'] = population
    count['ISDCode'] = isdCode
    info.append(count.copy())
    
    
print(len(info))
print(json.dumps(info,indent=2))

##with open('covid_output.json','w') as fw:
##    fw.write(json.dumps(count,indent=2))

##with open('covid_output.csv','w') as f:
##    csv_writer=csv.writer(f,delimiter='-')
##    csv_writer.writerow(json.dumps(count,indent=2))
