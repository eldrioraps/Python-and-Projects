from abc import ABC, abstractmethod
from datetime import datetime

# Abstraction: Define a blueprint for products without implementation details
class Product(ABC):
    @abstractmethod
    def get_details(self):
        """Return product details for display."""
        pass

    @abstractmethod
    def calculate_price(self):
        """Calculate final price (e.g., after discounts)."""
        pass

# Encapsulation: Base product class with protected attributes and controlled access
class BaseProduct(Product):
    def __init__(self, product_id, name, base_price, stock):
        self._product_id = product_id  # Protected: Unique ID
        self._name = name
        self._base_price = base_price
        self._stock = stock  # Protected: Internal stock count

    @property
    def name(self):
        return self._name

    @property
    def base_price(self):
        return self._base_price

    @property
    def stock(self):
        return self._stock

    def reduce_stock(self, quantity):
        """Controlled stock modification."""
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        return False

# Inheritance: Electronics inherits from BaseProduct, adding specific attributes
class Electronics(BaseProduct):
    def __init__(self, product_id, name, base_price, stock, warranty_years):
        super().__init__(product_id, name, base_price, stock)
        self._warranty_years = warranty_years  # Specific to electronics

    def get_details(self):  # Polymorphism: Override for specific details
        return f"{self._name} (Electronics), Price: ${self._base_price}, Warranty: {self._warranty_years} years, Stock: {self._stock}"

    def calculate_price(self):  # Polymorphism: Apply electronics-specific discount
        discount = 0.1 if self._base_price > 500 else 0  # 10% off for expensive items
        return self._base_price * (1 - discount)

# Inheritance: Clothing inherits from BaseProduct
class Clothing(BaseProduct):
    def __init__(self, product_id, name, base_price, stock, size):
        super().__init__(product_id, name, base_price, stock)
        self._size = size

    def get_details(self):  # Polymorphism: Override for clothing details
        return f"{self._name} (Clothing), Price: ${self._base_price}, Size: {self._size}, Stock: {self._stock}"

    def calculate_price(self):  # Polymorphism: Apply seasonal discount
        return self._base_price * 0.8  # 20% seasonal discount

# Abstraction: Payment processor interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, user):
        """Process payment for given amount."""
        pass

# Polymorphism: Different payment methods
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount, user):
        return f"Processed ${amount:.2f} via Credit Card for {user}"

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount, user):
        return f"Processed ${amount:.2f} via PayPal for {user}"

# Encapsulation: User class to manage customer data securely
class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email  # Protected: Sensitive data
        self._cart = []  # List of (product, quantity) tuples

    @property
    def name(self):
        return self._name

    def add_to_cart(self, product, quantity):
        if product.reduce_stock(quantity):
            self._cart.append((product, quantity))
            return f"Added {quantity} {product.name} to cart"
        return "Insufficient stock"

    def checkout(self, payment_processor):
        total = sum(product.calculate_price() * qty for product, qty in self._cart)
        result = payment_processor.process_payment(total, self._name)
        self._cart = []  # Clear cart after successful payment
        return f"{result}, Total: ${total:.2f}"

# E-Commerce System: Orchestrates products, users, and payments
class ECommerceSystem:
    def __init__(self):
        self._products = []
        self._users = []

    def add_product(self, product):
        self._products.append(product)

    def add_user(self, user):
        self._users.append(user)

    def display_products(self):
        return "\n".join(product.get_details() for product in self._products)

# Demo: Simulate e-commerce workflow
if __name__ == "__main__":
    # Initialize system
    shop = ECommerceSystem()

    # Create products
    laptop = Electronics("E001", "Laptop", 1000, 5, 2)
    tshirt = Clothing("C001", "T-Shirt", 20, 100, "M")
    shop.add_product(laptop)
    shop.add_product(tshirt)

    # Create user
    user = User("U001", "Alice", "alice@example.com")

    # Display catalog
    print("Product Catalog:")
    print(shop.display_products())

    # User adds items to cart
    print("\nCart Actions:")
    print(user.add_to_cart(laptop, 1))
    print(user.add_to_cart(tshirt, 2))

    # Checkout with different payment methods
    print("\nCheckout:")
    print(user.checkout(CreditCardPayment()))  # Polymorphic payment
    print(user.checkout(PayPalPayment()))      # Empty cart, so $0