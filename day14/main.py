MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


resources = { "water": 3000, "milk": 200, "coffee": 100}

money: dict[str, float] = {    "PENNIES" : 0.01,    "NICKLES" : 0.05,    "DIMES" : 0.10,    "QUARTERS" : 0.25}

def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money}")


def check_resources_sufficient(drink):
    if drink == 'latte' or drink == 'cappuccino' or drink == 'espresso':
        if MENU[drink]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water.")
        elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough milk.")
        elif not drink == 'espresso' and MENU[drink]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
        else:
            resources['water'] -= MENU[drink]['ingredients']['water']
            resources['coffee'] -= MENU[drink]['ingredients']['coffee']
            if not drink == 'espresso':
                resources['milk'] -= MENU[drink]['ingredients']['milk']
            return True

    return False


total_money: float = 0

isOff = False

while not isOff:
    drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if drink == 'off':
        break
    elif drink == 'report':
        print_resources()
    elif drink == 'espresso':
        print("Espresso")
        if check_resources_sufficient('espresso'):
            print("enjoy")
        else:
            print("no resources")
    elif drink == 'latte':
        print("Latte")
        if check_resources_sufficient('latte'):
            print("enjoy")
        else:
            print("no resources")
    elif drink == 'cappuccino':
        print("Cappuccino")
        if check_resources_sufficient('cappuccino'):
            print("enjoy")
        else:
            print("no resources")

print("Good Bye")