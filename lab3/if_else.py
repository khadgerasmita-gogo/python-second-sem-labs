inventory = {'screws':150,'bolts':8,'washers':0,'nuts':45}

check={key: ("In Stock" if value>=10  else "Reorder") for (key,value) in inventory.items()}
print(check)