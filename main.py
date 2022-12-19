import random

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


def enough_resource(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] <= resources[key]:
            return True
        else:
            print(f"Sorry, not enough {key} please restock")
            return False


def what_user_wants():
    user_want = input("What would you like? (espresso/latte/cappuccino/report/cost/off): ")
    return user_want

def pay(type_coffe):

    print("Please insert your coins:\n")

    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quater = 0.25
    amount_given = 0

    num_quat = int(input("how many quaters?: "))
    num_dime = int(input("how many dimes?: "))
    num_nic = int(input("how many nickels?: "))
    num_pen = int(input("how many pennies?: "))

    amount_given = (quater * num_quat) + (dime * num_dime) + (nickel * num_nic) + (penny * num_pen)

    if amount_given > MENU[type_coffe]["cost"]:
        change = 0
        change = amount_given - MENU[decision]["cost"]
        return change
    else:
        change = -1
        return change


run_machine = True

while run_machine == True:
    decision = what_user_wants()


    if decision == "report":
        print(resources)
        print(f"Money: ${profit}")

    elif decision == "off":
        print("Coffee machine is now turned off")
        run_machine = False

    elif decision == "cost":
        print("espresso:")
        print(MENU["espresso"]["cost"])
        print("latte:")
        print(MENU["latte"]["cost"])
        print("cappuccino:")
        print(MENU["cappuccino"]["cost"])

    else:
        proceed = enough_resource(MENU[decision]["ingredients"])
        if proceed == True:
            change = round(pay(decision), 2)
            profit += MENU[decision]["cost"]
            for key in MENU[decision]["ingredients"]:
                resources[key] -= MENU[decision]["ingredients"][key]


            if change > 0:
                print(f"Your change is ${change}")
                print(f"Enjoy your {decision} ☕")

            else:
                print("You did not put in enough money for your drink sorry :(\nYour money has been refunded")








