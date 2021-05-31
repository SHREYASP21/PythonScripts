#shooping list
cart=['fruits','books','pens','bottles','chips']
print('-'*30)
print('cart')
print('-'*30)
for i in cart:
    print(i)
print('-'*30)
item=input("enter new items in the shopping list: ").title()
cart.append(item)
print('-'*30)
print("Updated shopping list")
print('-'*30)
for i in cart:
    print(i)
item2=input("enter the item that needs to be removed: ")
if item2 in cart:
    cart.remove(item2)
    print("updated shopping list after removing item")
    for i in cart:
        print(i)
else:
    print('-'*30)
    print("This item is not in the list")



