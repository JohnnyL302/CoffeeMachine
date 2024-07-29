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
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif drink != "espresso":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False



def calculate_money(quarters, dimes, nickels, pennies, drink):
    quarters = 0.25 * quarters
    dimes = 0.10 * dimes
    nickels = 0.05 * nickels
    pennies = 0.01 * pennies
    total = quarters + dimes + nickels + pennies
    if total < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif total > MENU[drink]["cost"]:
        total = round(total - MENU[drink]["cost"], 2)
        total = "{:.2f}".format(total)
        print(f"Here is your change: ${total}")
        make_drink(drink)
        return MENU[drink]["cost"]
    else:
        make_drink(drink)
        return MENU[drink]["cost"]


def make_drink(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink} ☕. Enjoy! ")


machine_on = True

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    elif user_input == "espresso" or "latte" or "cappuccino":
        if check_resources(user_input) == False:
            continue
        else:
            print("Please insert coins.")
            num_quarters = int(input("How many quarters?: ") )
            num_dimes = int(input("How many dimes?: "))
            num_nickels = int(input("How many nickels?: "))
            num_pennies = int(input("How many pennies?: "))
            can_Buy = calculate_money(num_quarters, num_dimes, num_nickels, num_pennies, user_input)
            profit += can_Buy















