class Vehicle:
    def __init__(self, type, model, color, engine_cc, weight, speed):
        self.__type = type
        self.__model = model
        self.__color = color
        self.__engine_cc = engine_cc
        self.__weight = weight
        self.__speed = speed

    @property
    def type(self):
        return self.__type

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def engine_cc(self):
        return self.__engine_cc

    @property
    def weight(self):
        return self.__weight

    @property
    def speed(self):
        return self.__speed

    def display_specifications(self):
        print(f"Type: {self.__type}")
        print(f"Model: {self.__model}")
        print(f"Color: {self.__color}")
        print(f"Engine CC: {self.__engine_cc}")
        print(f"Weight: {self.__weight}")
        print(f"Speed: {self.__speed}")

class TwoWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed):
        super().__init__("Two-Wheeler", model, color, engine_cc, weight, speed)

class ThreeWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed):
        super().__init__("Three-Wheeler", model, color, engine_cc, weight, speed)

class FourWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed):
        super().__init__("Four-Wheeler", model, color, engine_cc, weight, speed)

def get_vehicle_list(vehicle_list):
    for vehicle in vehicle_list:
        print(vehicle.model)

def get_vehicle_specifications(vehicle_list, model):
    for vehicle in vehicle_list:
        if vehicle.model == model:
            vehicle.display_specifications()
            break
    else:
        print(f"No specifications found for model {model}")

vehicles = [TwoWheeler("Activa", "Red", 110, 120, 60),
            TwoWheeler("TVS", "Blue", 125, 110, 55),
            TwoWheeler("Royal Enfield", "Black", 350, 180, 80),
            ThreeWheeler("Auto Rickshaw", "Green", 150, 300, 40),
            FourWheeler("Sedan", "Silver", 1200, 1500, 120),
            FourWheeler("SUV", "Black", 1600, 1700, 130)]

print("List of all available vehicle models:")
get_vehicle_list(vehicles)

model = input("Enter the model of the vehicle to see its specifications: ")
get_vehicle_specifications(vehicles, model)

