# abstraction, @abstractmethod.


'''from abc  

class Payment(ABC):

    def show_mesage(self):
        print("odeme prosesi baslanildi ...")

    @abstractmethod
    def pay(self, amount):
        pass



class CardPayment(Payment):
    def pay(self, amount):
        print("kartla odeme edildi:", amount)

class   CashPayment(Payment):
    def pay(self, amount):
        print("nağd odeme edildi:", amount)

class OnlinePayment(Payment):
    def pay(self, amount):
        print("online odeme edildi:", amount)


class CryptoPayment(Payment):
    def pay(self, amount):
        print("kripto odeme edildi:", amount)
class M10 :
    def pay(self, amount):
        print("M10 odeme edildi:", amount)

card1 = CardPayment()
card1.pay(100)
cash1 = CashPayment()
cash1.pay(100)
online1 = OnlinePayment()
online1.pay(100)
crypto1 = CryptoPayment()
crypto1.pay(100)
m10 = M10()
m10.pay(100)
    

payments = [CardPayment(), CashPayment(), OnlinePayment(), CryptoPayment()]
for payment in payments:
    payment.show_mesage()
    payment.pay(100)'''
    
'''from abc import ABC, abstractmethod
class Heyvan(ABC):

    @abstractmethod
    def ses_ver(self):
        print("Heyvan ses verir")


class It(Heyvan):
    def yerimek(self):
        print("It yeriyir")
    def ses_ver(self):
        print("Hav Hav")


it = It()
it.ses_ver()
it.yerimek()'''












class Employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        print("Iscinin maasi:", self.__salary)

employee1 = Employee(1000)
print(employee1.get_salary())