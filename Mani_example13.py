#import rhinoscriptsyntax as rs
import json

#filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
#filename = rs.OpenFileName("Open JSON File", filter)


#if filename:
#    with open(filename, 'r') as f:
#        datastore = json.load(f)

##Use the new datastore datastructure
#print(datastore["office"]["parking"]["style"])

#json_file = open('test_json_file.json', 'r')

#json.loads(json_file)
#print(json_file['office']['parking']['style'])

#json_file.close


#data = []
with open('test_json_file.json') as f:
    data = json.load(f)

#print(type(data))

#print(data['office']['parking']['style']) ## This works

#for parking in data['office']['parking']:
#    print(parking['style'])
#print("Error is starting from here...")
#print('-'*50)

for medical in data['office']['medical']:
    print(medical['use']) ## This is not working



##for i in range(len(data['office']['medical']['use']).count()):
##print([data['office']['medical']['use']]) ## This is not working

#print("usage = ", uses)
#for db_item in data:
#    print(data['office']['medical']['use'][:])
    
