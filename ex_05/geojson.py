import urllib.request
import urllib.error
import urllib.parse
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
key = "Enter_Your_KEY"

while True:
    address = input("Enter your location: ")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': key})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    location = js['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    print({
        'lat': lat,
        'lng': lng
    })

    location = js['results'][0]['formatted_address']
    print(location)
