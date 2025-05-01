class Product:
    def __init__(self, name, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not name or not isinstance(name, str):
            raise ValueError("Error: Please enter a valid product name")
        if price <= 0 or quantity <= 0:
            raise ValueError("Error: Please enter a valid price")

    def get_quantity(self) -> int:
        return self. quantity

    def set_quantity(self, quantity):
        if self.quantity < 0:
            raise ValueError("Quantity can't be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f" {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
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