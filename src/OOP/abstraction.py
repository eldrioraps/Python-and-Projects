from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount): pass

# Concrete Layers
class StripeProcessor(PaymentProcessor):
    def make_payment(self, amount):
        print(f"Stripe API: Charged ${amount}")

class RazorpayProcessor(PaymentProcessor):
    def make_payment(self, amount):
        print(f"Razorpay API: Charged ₹{amount}")

# Client code (e.g. order module)
def process_checkout(payment_processor: PaymentProcessor, amount):
    payment_processor.make_payment(amount)

# Usage
process_checkout(StripeProcessor(), 120)
process_checkout(RazorpayProcessor(), 5000)



from abc import ABC, abstractmethod

class Loan(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class HomeLoan(Loan):
    def calculate_interest(self):
        return "Home Loan interest rate: 8%"

class CarLoan(Loan):
    def calculate_interest(self):
        return "Car Loan interest rate: 9%"

class PersonalLoan(Loan):
    def calculate_interest(self):
        return "Personal Loan interest rate: 11%"

# loans = [HomeLoan(), CarLoan(), PersonalLoan()]
# for loan in loans:
#     print(loan.calculate_interest())


from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailChannel(NotificationChannel):
    def send_notification(self, message):
        print(f"Sending Email: {message}")

class SMSChannel(NotificationChannel):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

class SlackChannel(NotificationChannel):
    def send_notification(self, message):
        print(f"Sending Slack message: {message}")

# Business logic layer (uses abstraction)
def alert_user(channel: NotificationChannel):
    channel.send_notification("Your ticket has been resolved!")

# alert_user(EmailChannel())
# alert_user(SMSChannel())
# alert_user(SlackChannel())
