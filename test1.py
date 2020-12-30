import json

def open_file(file_name):
    """open file + load Json"""

    opened_file = open(file_name, "r", encoding="utf-8")
    data = json.load(opened_file)
    return data

x = open_file('connected-realm.json')

"""
for result in x['results']:
    print(result['key'])
"""

"""
for result in x['results']:
    print(result['key'],result['data']['id'])
"""


