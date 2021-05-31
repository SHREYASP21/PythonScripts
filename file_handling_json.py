import json
# shoppinglist={'bread':'1 pack','eggs':'1 dozen'}
# with open("shopping.json",'w') as file:
#     json.dump(shoppinglist,file,indent=2)

import json
with open("shopping.json",'r') as file:
    a=json.load(file)
for i,j in a.items():
    print(f"{i} {j}")