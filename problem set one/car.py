class Car:
    def __init__(self, speed=0, distance=0):
        self.speed = speed
        self.distance = distance

    def __str__(self):
        return f"Car: Speed = {self.speed}, Distance = {self.distance}"

    def update(self, time):
        self.distance += time * self.speed

    @classmethod
    def from_speed(cls, spd):
        return cls(spd)


truck = Car.from_speed(20)
truck.update(10)
truck.update(40)
print(truck)