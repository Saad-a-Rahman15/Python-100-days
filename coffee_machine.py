from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

working = True

while working:
    coffee_options = menu.get_items()
    coffee_choice = input(f'Which kind of coffee would you like?: {coffee_options}, or enter "off" to turn the coffee machine off, or enter "report" to see how many ingredients you have and to see the amount of money that you have. \n ')
    if coffee_choice == 'off':
        working = False
    elif coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)