from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
again = True
while again:
    order_name = input("What would you like? (espresso/latte/cappuccino/): ")
    if order_name == "off":
        print("Machine off")
        again = False
    if order_name == "report":
        coffee.report()
        money.report()
    if order_name in menu.get_items():
        drink = menu.find_drink(order_name)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)