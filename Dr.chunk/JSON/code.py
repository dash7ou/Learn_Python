import json

data = '''{
    "name": "mohammed",
    "phone": {
        "type": "int",
        "number": "0595555"
    },
    "email":{
        "hide": "yes"
    }
}
'''

info = json.loads(data)
print("Name: ", info["name"])
