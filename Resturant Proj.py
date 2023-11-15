# 3 global variables
# cust_dict = {...}
# menu_dict = {...}
# taxes

# Welcome function
# welcome the customer
# Display the menu amd taxes

# Calculation function
# get the meal input
# check if the meal exists and budget is enough
# Calculate and display the budget

# key: customer name value: $ budget
cust_dict = {"Alice":50,
             "John":12,
}

# key: meal name :value: cost of the meal
menu_dict = {
    "burger":8,
    "pizza":14,
    "cake":5
}

taxes = 0.8

def welcome(customer,budget):
    print(f"welcome to our restaurant! {customer}, Budget : {budget}")
    print("-----------------------------------------------------")
    print("menu list:")
    for meal,cost in menu_dict.items():
        print(f"{meal} costs : {cost}")
    print(f"Taxes : {taxes}")


def calculation(customer,budget):
    meal = input("what would you like to have ? : ").lower()
    while meal not in menu_dict.keys():
        print(f"{meal} is not available, try again.")
        meal = input("what would you like to have ? : ")

    meal_price = menu_dict[meal]

    while meal_price + taxes  > budget :
        print(f"sorry no enough budget for {meal}")
        meal = input("what would you like to have ? : ").lower()
        meal_price = menu_dict[meal]

    left_budget = (budget - meal_price) - taxes
    print(f"your left budget is {left_budget}, Thank you for choosing us Dear {customer} :).")

for customer,budget in cust_dict.items():
    welcome(customer,budget)
    calculation(customer,budget)