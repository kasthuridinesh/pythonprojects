class Vehicle:
    def __init__(self, type, model, color, cc, weight, speed):
        self.__type = type
        self.__model = model
        self.__color = color
        self.__cc = cc
        self.__weight = weight
        self.__speed = speed

    def get_type(self):
        print(self.__type)

    def get_model(self):
        print(self.__model)

    def get_color(self):
        print(self.__color)

    def get_cc(self):
         print(self.__cc)

    def get_weight(self):
        print(self.__weight)

    def get_speed(self):
        print(self.__speed)


class TwoWheeler(Vehicle):
    def __init__(self, model, color, cc, weight, speed):
        Vehicle.__init__(self, "Two-Wheeler", model, color, cc, weight, speed)
        return


class ThreeWheeler(Vehicle):
    def __init__(self, model, color, cc, weight, speed):
        Vehicle.__init__(self, "Three-Wheeler", model, color, cc, weight, speed)
        return


class FourWheeler(Vehicle):
    def __init__(self, model, color, cc, weight, speed):
        Vehicle.__init__(self, "Four-Wheeler", model, color, cc, weight, speed)
        return


class VehicleManagementSystem:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def get_all_vehicle_models_by_type(self, type):
        models = []
        for vehicle in self.__vehicles:
            if vehicle.get_type() == type:
                models.append(vehicle.get_model())
                print(models)
        return models

    def get_specifications_by_model(self, model):
        for vehicle in self.__vehicles:
            if vehicle.get_model() == model:
                return vehicle.__dict__


vehicle_management_system = VehicleManagementSystem()

vehicle_management_system.add_vehicle(TwoWheeler("Activa", "Red", 125, 110, 80))
vehicle_management_system.add_vehicle(TwoWheeler("TVS", "Black", 135, 115, 85))
vehicle_management_system.add_vehicle(TwoWheeler("Royal Enfield", "Silver", 145, 120, 90))

vehicle_management_system.add_vehicle(ThreeWheeler("Auto Rickshaw", "Yellow", 200, 400, 50))
vehicle_management_system.add_vehicle(ThreeWheeler("Tempo", "White", 220, 420, 60))

vehicle_management_system.add_vehicle(FourWheeler("Maruti Suzuki", "Red", 1200, 1500, 100))
vehicle_management_system.add_vehicle(FourWheeler("Hyundai", "Black", 1300, 1600, 110))

vehicle_management_system.get_specifications_by_model("Tempo")




# print("Two-Wheeler Models: ", vehicle_management_system.get_specifications_by_model(ThreeWheeler))
# Vehicle.get_model()