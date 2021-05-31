menu_shop={'books':160,'pens':200,'papers':50,'bottles':120}
for i,j in menu_shop.items():
    print(f"{i:15} Rupees {j}")

bill=0
while True:
    order=input("Please enter your items:").lower()
    if order in menu_shop:
        qty=int(input("How many items do you want to purchase:"))
        bill += menu_shop[order]*qty
        print(bill)
    else:
        print("this item is currently not available")
    a=input("do you want to  purchase more itmes?")
    if a=='yes':
        continue
    else:
        break

