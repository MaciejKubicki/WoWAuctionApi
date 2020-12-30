import json

people_string = '''
{
    "people":[
      {
        "name": "John",
        "phone": "615-555",
        "emails": ["jonmail","johnsecondmail"],
        "has_licanse": false
      },
      {
        "name": "Mn",
        "phone": "0000",
        "emails": null,
        "has_licanse": true
      }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data['people']))

for person in data['people']:
    print(type(person))
    print(person)

new_string = json.dumps(data, indent=2)
print(new_string)