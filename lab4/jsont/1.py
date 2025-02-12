import json

with open("jsont\sample-data.json", "r") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface status")
print("="*100)
print("DN                                     Description               Speed    MTU")
print("-"*100)

for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "-"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:40} {descr:20} {speed:8} {mtu}")
