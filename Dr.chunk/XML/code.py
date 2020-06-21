import xml.etree.ElementTree as ET

data = '''
    <preson>
        <name>shimaa</name>
        <phone type="intl"> +972592105998 </phone>
        <email hide="yes" />
    </preson>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print("Attr: ", tree.find("email").get("hide"))
