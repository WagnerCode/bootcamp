import time
from random import randint
import os



def log(funk):
    def inner1(*args, **kwargs):
        file = open(r"/home/user/Desktop/bootcamp/bootcamp/module02/Ex02/machine.log", "a")
        begin = time.time()

        funk(*args, **kwargs)

        end = time.time()
        if funk.__name__ == "add_water":
            s = f"(cmaxime)Running: {funk.__name__}\t\t[ exec-time = {(end - begin) * 10**3}] \n"
        else:
            s = f"(cmaxime)Running: {funk.__name__}\t[ exec-time = {(end - begin) * 10 ** 3}] \n"
        file.write(s)

        file.close()

    return inner1

#... your definition of log decorator...
class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)