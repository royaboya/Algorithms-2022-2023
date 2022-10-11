class Car:
    def __init__(self):
        self.speed = 0
        self.distance = 0

    def __str__(self):
        return f"Car: Speed = {self.speed}, Distance = {self.distance}"

    def update(self, time):
        self.distance += time * self.speed

    @classmethod
    def from_speed(cls, spd):
        new_car = cls()
        new_car.speed = spd
        return new_car


truck = Car.from_speed(20)
truck.update(10)
truck.update(40)
print(truck)