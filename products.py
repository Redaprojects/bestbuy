class Product:
    """
    Represents a product class in the (Best buy) store which has several attributes:
    name (str), price (float), quantity (int) of the product and active (bool): whether the product is active or not.
    """

    def __init__(self, name:str, price:float, quantity:int):
        """
        Initialize a product instance. The name must be a string,
        the price is positive, and the quantity must be non-negative.
        It raises: ValueError: If name is empty or price/quantity is non-positive.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not name or not isinstance(name, str):
            raise ValueError("Error: Please enter a valid product name")
        if price <= 0 or quantity <= 0:
            raise ValueError("Error: Please enter a valid price")

    def get_quantity(self) -> int:

        """
        Returns (int) the current available quantity.
        """
        return self. quantity

    def set_quantity(self, quantity):
        """
        Updates the quantity of the product, deactivates the product if the quantity becomes 0.
        and it raises a ValueError if quantity is negative.
        """
        if self.quantity < 0:
            raise ValueError("Quantity can't be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        Checks if the product is currently active and returns True if active, otherwise False.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """
        Returns a string representation of the product and some information about it
        like: name, price, and quantity of the product.
        """
        return f" {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Processes the purchase of a specified quantity, if it's
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity available.")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    """
    Initialize products (Instance Classes) for Bose and Mac to apply the proper class's methods to them and run the app.
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == "__main__":
    main()