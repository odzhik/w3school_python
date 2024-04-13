import json


with open(r"C:\Users\Olzhas\Desktop\workspace\PP2 labs\lab4\sample-data.json", 'r') as f:
    data = f.read()
    obj = json.loads(data)



print("Interface Status")
print("=" * 80)
print("{:<44} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
  
interfaces = obj.get('imdata',[{}])
for i in interfaces:
    l1PhysIf = i.get('l1PhysIf', {})
    attributes = l1PhysIf.get('attributes', {})
    
    
dn = attributes.get('dn','')
descr = attributes.get('descr', '')
speed = attributes.get('speed', '')
mtu = attributes.get('mtu', '')
    
print("{:<44} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))