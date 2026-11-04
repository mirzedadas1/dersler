# encapsulation->public(self.name),  protected(_balance),private(__balance),name mangling(__balance->_BankAccount__balance)
#Getter ve setter metodlari
#annotation->@property,@setter
'''class Student:
    def __init__(self,name):
        self.name = name

student1 = Student("Mirza")

print(student1.name)''' # public


'''class Student:
    def __init__(self,name):
        self._name = name

student1 = Student("Mirza")



student1._name = "Nicat"
print(student1._name) # protected
'''


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        print("Hesab balansi:", self.__balance)

    def set_balance(self, balance):
        if balance < 0:
            print("Balans menfi ola bilmez")
        else:
            self.__balance = balance


account1 = BankAccount(1000)

print(account1.__balance) # private

'''class Student:
    def __init__(self,age):
        self.__age = age

    @property
    def get_age(self):
        print("Telebenin yasi:", self.__age)
    @get_age.setter
    def set_age(self, age):
        if not isinstance(age, int):
            print("Yas integer olmalidir")
        elif age <= 0:  
            raise ValueError("Yas menfi ola bilmez")
        self.__age = age


student1 = Student(20)

student1.set_age = 25
student1.get_age'''









'''Student adli bir class yaradin, name ve age adli atributlar olsun(private olsun),
getter ve setter metodlari ile bu atributlara elave edin, cagirin ve ekrana cixarin.'''


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("Telebenin adi:", self.__name)

    def set_name(self, name):
        self.__name = name