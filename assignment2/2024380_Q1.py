menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

def menu_card():
    print("Menu Card")
    print("---------")
    for i in range(len(menu)):
        print(i+1, menu[i][0], f'\u20B9{menu[i][1]}', sep = ". ")

menu_card()

def order(item,quant):
    return f'You have ordered {quant,menu[item-1][0]}'

def multi_order():

    total_price = 0
    total_items = 0


    item = (input("Enter the item number: "))
    if item == '':
        print("Thank you for your order!")
        return
    quant = int(input("Enter the quantity: "))
    while True:
        print(order(int(item),quant))
        total_price += menu[int(item)-1][1]*quant
        total_items += quant
        item = (input("Enter the item number: "))
        if item == '':
            print("Thank you for your order!, Your total price is \u20B9",total_price, "for", total_items, "items")
            return
        quant = int(input("Enter the quantity: "))

multi_order()

def test():
    assert order(1,2) == "You have ordered (2, 'Samosa')"
    assert order(2,3) == "You have ordered (3, 'Idli')"
test()