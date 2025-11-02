from abc import ABC, abstractmethod
#  abstract base class abc inbuilt python module
#  i built a major class named ACCOunt and tha class is defined under ABC that means 
# i am building a template which tell the mandatory sub classes or functionality of a logic.


# ------------------ ABSTRACTION ------------------
class Account(ABC):  # parent
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        # self.balance=balance
        self.__balance = balance  # ENCAPSULATION — hidden attribute

    # Abstract methods (force subclasses to implement)
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    # Encapsulated getter (controlled access to private variable)
    def get_balance(self):
        # return self.balance
        return self.__balance

    # Protected balance update (used inside the class only)
    def _update_balance(self, new_balance):
        self.__balance = new_balance


# ------------------ INHERITANCE ------------------
class SavingsAccount(Account):  #child
    def __init__(self, acc_no, name, balance=0):
        super().__init__(acc_no, name, balance)
        self.interest_rate = 0.04

    # ------------------ POLYMORPHISM ------------------
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._update_balance(self.get_balance() - amount)
            print(f"✅ {self.name} withdrew ₹{amount} from Savings Account")
        else:
            print("❌ Insufficient funds in Savings Account!")

    def deposit(self, amount):
        self._update_balance(self.get_balance() + amount)
        print(f"✅ {self.name} deposited ₹{amount} in Savings Account")


class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance=0, overdraft_limit=5000):
        super().__init__(acc_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self._update_balance(self.get_balance() - amount)
            print(f"✅ {self.name} withdrew ₹{amount} from Current Account")
        else:
            print("❌ Overdraft limit exceeded!")

    def deposit(self, amount):
        self._update_balance(self.get_balance() + amount)
        print(f"✅ {self.name} deposited ₹{amount} in Current Account")


# ------------------ POLYMORPHISM IN ACTION ------------------
def show_account_summary(account):
    print(f"👤 Account Holder: {account.name}")
    print(f"💰 Account Balance: ₹{account.get_balance()}")
    # print(f"💰 Account Balance: ₹{account.balance}")
    print("-" * 40)


# ------------------ MAIN EXECUTION ------------------
if __name__ == "__main__":
    # CLASS / OBJECT CREATION
    s1 = SavingsAccount(acc_no=101, name="Ravi", balance=10000)
    c1 = CurrentAccount(acc_no=201, name="Ritik", balance=5000)

    # Polymorphic usage — same method names, different behaviors
    for acc in [s1, c1]:
        acc.deposit(2000)
        acc.withdraw(3000)
        show_account_summary(acc)
