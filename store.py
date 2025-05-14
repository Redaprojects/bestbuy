from typing import List, Tuple
import products


class Store:
    def __init__(self, lst_products: List[products.Product]):
        """
        Initializes the class instance by passing the class list of products from the products file.
        """
        self.lst_products = lst_products

    def add_product(self, product):
        """Adds new products to the list of products."""
        self.lst_products.append(product)

    def remove_product(self, product):
        """Checks if the product inside the list to remove it from it."""
        if product in self.lst_products:
            self.lst_products.remove(product)

    def get_total_quantity(self) -> int:
        """Counts each product inside the instance list, adds it and returns the total amount of products."""
        total = 0
        for product in self.lst_products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[products.Product]:
        """
        Initializes and returns the active products list after checking each product
        If it's available in the store, add it to the list, otherwise,
        throws an exception and shows it to the user.
        """
        active_products = []
        for product in self.lst_products:
            try:
                if product.is_active():
                    active_products.append(product)
            except Exception as e:
                print(e)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Initialize and return the total price variable after counting each product amount in the shopping list
        and adds each one to the list by calling the buy function from the product class.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    """
    Initialize two products (instance classes), a product list with their name, price, and quantity,
    for applying both classes (Product and Store) methods on them to preview the result to the user.
    """
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    list_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(list_products[0], 1), (list_products[1], 2)]))

if __name__ == "__main__":
    main()