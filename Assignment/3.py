# QUESTION:
# Warehouse System: 1.Add 2.Remove 3.Report 4.Forecast

# stock data
stock = {}

def add():
    name = input("item: ")
    stock[name] = stock.get(name, 0) + int(input("qty: "))
    print("added!")

def sub():
    name = input("item: ")
    if name in stock:
        stock[name] -= int(input("qty: "))
        print("removed!")
    else: print("not found!")

def view():
    for name, qty in stock.items():
        print(f"{name}: {qty}")

def tip():
    name = input("item: ")
    if name in stock:
        if stock[name] < 10: print("buy more!")
        else: print("stock ok!")

# Loop
while True:
    print("\n1.Add 2.Sub 3.View 4.Tip 5.Exit")
    c = input("choice: ")
    if c == '1': add()
    elif c == '2': sub()
    elif c == '3': view()
    elif c == '4': tip()
    elif c == '5': break
    else: print("invalid!")