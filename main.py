import products
import store


def start(store_instance):
    """
    Initialize a dictionary that has all the functions to preview a list of available products, the
    total amount of each product, and to place an order for the user, even to quit the app.
    and let them choose between the various selections by passing the store instance parameter for each function
    and running an iteration until the user enters the correct positive number between 1 and 4.
    """
    menu_options = {
        1: list_products,
        2: show_total_amount,
        3: make_order
    }

    while True:
        choice = input(
        """
        **** Best Buy Store Menu ****
             ___________________\n
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        
        Please choose a number: """).strip().lower()

        if not choice.isdigit():
            print("Invalid input. please enter a number between (1 and 4)")
            continue

        menu = int(choice)

        if menu in menu_options:
            menu_options[menu](store_instance)
        elif menu == 4:
            print("Thank you for shopping by us. Goodbye! 👋")
            break


def list_products(store_instance):
    """
    Previews a list of available products to the user by passing the store instance parameter
    and calling both methods get_all_products() and show() from the Store and Products classes.
    It starts from 1 for the first product and so on..
    """
    print("        ___________")
    for i, product in enumerate(store_instance.get_all_products(), start=1):
        print(f"{i}, {product.show()}")
    print("        ___________")


def show_total_amount(store_instance):
    """
    Previews the total amount for all products to the user by passing and calling
    the method get_total_quantity() from the Store class.
    """
    total = store_instance.get_total_quantity()
    print("        ___________")
    print(f"        Total of {total} items in store")
    print("        ___________")


def make_order(store_instance):
    """
    Initializes a variable that has each product's information and the store instance parameter
    to iterate over each product to show the name, price, and quantity to the user by strating from 1 and so on..
    Then initializes a shopping list which has all the information about the user's order.
    """
    print("        ___________")
    all_products = store_instance.get_all_products()
    for i, product in enumerate(all_products, start=1):
        print(f"{i}, {product.show()}")
    print("        ___________")

    shopping_list = []
    while True:
        choice = input("Please select a product number, or (leave it empty to go back): ").strip()

        # If there is an empty choice, it makes the user go back to the main menu.
        if not choice:
            break

        # If the choice is either a positive number or out of the product length range, it prints
        # a message to the user and starts over from the beginning.
        if not choice.isdigit() or (0 >= int(choice) <= len(all_products)):
            print("Invalid product number.")
            continue

        quantity = input("Please select the amount do you want or (leave it empty to go back): ").strip()

        # If there is no quantity number, it breaks outside and go back to the main menu.
        if not quantity:
            break

        # If the quantity is not a positive number, equal or less than 0 ,it starts over again.
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity.")
            continue

        # Adds each chosen product from the previous list and subtracts from each product 1
        shopping_list.append((all_products[int(choice) - 1], int(quantity)))
        print("Product added to the basket!\n")

    # If there is a shopping list, it previews the total order to the user by using the store instance parameter
    # and passing the order function from the Store class.
    if shopping_list:
        total = store_instance.order(shopping_list)
        print(f"***The order made, Total payment: {total} $")


def main():
    """
    Initialize first the product_list, which has all the information about each product name, price, and quantity.
    And the store variable instance, best_buy, by calling the Store class from the store file.
    Runs the app by calling the start function.
    """


    # setup the initial stock of inventory
    product_list = [products.Product("    MacBook Air M2", price=1450, quantity=100),
                    products.Product("    Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("    Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)



# Run the app if this file is executed directly
if __name__ == "__main__":
    main()