from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class GooglePay():
    def pay(self, amount):
        print(f"{amount} paid via Google Pay")
        
class PhonePay():
    def pay(self, amount):
        print(f"{amount} paid via Phone Pay")
class Paytm(Payment):
    def pay(self, amount):
        print(f"{amount} paid via Paytm")

obj = PhonePay()
obj.pay(6000)
