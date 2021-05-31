cars_stock={'nissan':['Pathfinder','Nissan','37OZ','GT-R'],'Honda':['Civic','Accord','CR-V']}
for cars in cars_stock.keys():
    print(cars)
print('*'*30)    
    
for car in cars_stock.values():
    print(car)

for i,j in cars_stock.items():
    print(f"{i} {j}")

