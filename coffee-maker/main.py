from __future__ import annotations

from data import INITIAL_RESOURCES
from data import MENU

resources = INITIAL_RESOURCES
profit = 0.0


def show_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def is_resources_sufficient(requested):
    for item in requested:
        if requested[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return round(total, 2)


def make_coffee(drink, requested):
    for item in requested:
        resources[item] -= requested[item]
    print(f"Here is your {drink}. Enjoy!”.")


def is_transaction_completed(payment, drink_cost):
    if payment > drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    elif payment == drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        show_report(profit)
    elif (
        user_input == "espresso" or user_input == "latte" or user_input == "cappuccino"
    ):
        if is_resources_sufficient(MENU[user_input]["ingredients"]):
            cost = MENU[user_input]["cost"]
            if is_transaction_completed(process_coins(), cost):
                profit += cost
                make_coffee(user_input, MENU[user_input]["ingredients"])
