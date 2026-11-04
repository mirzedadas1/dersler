#composition

'''class Car:
    def start(self):
        print("Masin işə düşdü")


car = Car()
car.start()'''

'''class Engine :
    def start(self):
        print("Muherrik ise dusdu")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()

car = Car()
car.start()'''


class CPU:
    def process(self):
        print("cpu ise dusdu")

class Computer:
    def __init__(self):
        self.cpu = CPU()
    def run_program(self):
        self.cpu.process()

pc = Computer()
pc.run_program()
