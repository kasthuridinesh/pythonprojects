class Vehicle:
    def __init__(self, type_of_vehicle, model):
        self.type_of_vehicle = type_of_vehicle
        self.model = model

    def display_vehicle_type(self):
        print("Type of vehicle:", self.type_of_vehicle)

    def display_model(self):
        print("Model:", self.model)


class TwoWheeler(Vehicle):
    def __init__(self, type_of_vehicle, model, color, engine, speed):
        Vehicle.__init__(self, type_of_vehicle, model)
        self.color = color
        self.engine = engine
        self.speed = speed

    def display_details(self):
        self.display_vehicle_type()
        self.display_model()
        print("Color:", self.color)
        print("Engine CC:", self.engine)

        print("Speed:", self.speed)


class ThreeWheeler(Vehicle):
    def __init__(self, type_of_vehicle, model, color, engine, speed):
        Vehicle.__init__(self, type_of_vehicle, model)
        self.color = color
        self.engine = engine

        self.speed = speed

    def display_details(self):
        self.display_vehicle_type()
        self.display_model()
        print("Color:", self.color)
        print("Engine :", self.engine)
        print("Speed:", self.speed)


class FourWheeler(Vehicle):
    def __init__(self, type_of_vehicle, model, color, engine, speed):
        Vehicle.__init__(self, type_of_vehicle, model)
        self.color = color
        self.engine = engine

        self.speed = speed

    def display_details(self):
        self.display_vehicle_type()
        self.display_model()
        print("Color:", self.color)
        print("Engine CC:", self.engine)

        print("Speed:", self.speed)


def display_all_vehicle_models(vehicles):
    for vehicle in vehicles:
        vehicle.display_details()
        print()


if __name__ == "__main__":
    two_wheelers = [TwoWheeler("Two-Wheeler", "Activa", "Red", 109.19, 345),
                    TwoWheeler("Two-Wheeler", "TVS", "Blue", 109.19, 5485),
                    TwoWheeler("Two-Wheeler", "Royal enfield", "Blue", 9889, 7)
                    ]
if __name__ == "__main__":
    three_wheelers = [ThreeWheeler("Three-Wheeler", "Mahindra", "Red", 109.19, 345),
                      ThreeWheeler("Three-Wheeler", "tuk-tuk", "Blue", 109.19, 5485),
                      ThreeWheeler("Three-Wheeler", "pulser", "green", 9889, 7)
                      ]
if __name__ == "__main__":
    four_wheelers = [FourWheeler("Four-Wheeler", "Mahindra", "Red", 109.19, 345)]

