import json

jsonString = ''' {
"name":"ankit",
"surname":"gupta",
"Age":36,
"Education":["BE","ICWA","Valuer"]
}'''

pythonJson = json.loads(jsonString)
data = pythonJson['Education']

jsonString_New = json.dumps(data,indent=2)
print(jsonString_New)



##with open('states.json') as rf:
##    pythonData = json.load(rf)
##
##for state in pythonData['states']:
##    del state['area_codes']
##    #print(state)
##
###print(pythonData)
##
##with open('new_States.json','w') as wf:
##        
##    json.dump(pythonData,wf,indent=1)
        
