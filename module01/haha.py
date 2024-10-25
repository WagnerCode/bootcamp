


class Car:
    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель заупущен"
        return "Двигатель уже был запущен"

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен"
        return "Двигатель уже был остановлен"

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен"
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива"
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} km. Fuel: {self.reserve} l."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption

def range_reserve(car):
    return car.get_reserve() / car.get_consumption() * 100

print(type(Car(color="black", consumption=10, tank_volume=55)))
car_1 = Car(color="black", consumption=10, tank_volume=55)

print(isinstance(car_1, Car))

for item in car_1.__dict__:
    if item == 'consumption':
       if isinstance(car_1.__dict__[item], int):
        print(True)

print(len(car_1.__dict__))


