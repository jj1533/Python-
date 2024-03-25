stock={
    "Book":100,
    "Pencil":30,
    "Pen":70
}
price={
    "Book": "25",
    "Pencil": "5",
    "Pen": "10"
}
print("Available Items in the stock are \n")
for x,y in stock.items():
    print(x, y)
print("\n")
print("Price of each items \n")
for a,b in price.items():
    print(a, b)

item=input("Enter item to buy: ")

if item in stock:
    qty=int(input("Enter quantity: "))
    if qty<=stock[item]:
        ad=price[item]
        totalcost=qty*int(ad)
        stock[item]=stock[item]-int(qty)
        print("TOTAL BILL: ",totalcost)
    else:
        print("no stock")
else:
    print("no item found")


    

