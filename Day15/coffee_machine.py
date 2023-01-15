import menu, os

clear = lambda: os.system('cls')

WATER = menu.resources['water']
MILK = menu.resources['milk']
COFFEE = menu.resources['coffee']
MONEY = 0

off = False

def check_resources(water, milk, coffee, drink_water, drink_milk, drink_coffee):
    if water >= drink_water and milk >= drink_milk and coffee >= drink_coffee:
        return True
    else:
        return False

def remove_resources(water, milk, coffee):
    global WATER, MILK, COFFEE

    WATER -= water
    MILK -= milk
    COFFEE -= coffee

def process_coins(cost):
    global MONEY

    MONEY += cost
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    change = total - cost
    return change

def process_drink(water, milk, coffee, user_choice):
    remove_resources(water, milk, coffee)
    change = round(process_coins(menu.MENU[user_choice]['cost']), 2)
    print(f"Here is ${change} in change.")
    print("Here is your espresso. Enjoy.")

while not off:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        print(f"Water: {WATER}ml")
        print(f"Milk: {MILK}ml")
        print(f"Coffee: {COFFEE}g")
        print(f"Money: ${MONEY}")
    elif user_choice == "off":
        off = True
        print("Coffee machine is turning off.")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        make_drink = check_resources(WATER, MILK, COFFEE, menu.MENU[user_choice]['ingredients']['water'], menu.MENU[user_choice]['ingredients']['milk'], menu.MENU[user_choice]['ingredients']['coffee'])

        if make_drink:
            process_drink(menu.MENU[user_choice]['ingredients']['water'], menu.MENU[user_choice]['ingredients']['milk'], menu.MENU[user_choice]['ingredients']['coffee'], user_choice)
        else:
            print("Not enough resources in coffee machine.")
    else:
        print("Unrecognized drink or command. Please try again.")