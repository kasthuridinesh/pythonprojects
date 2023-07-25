class Vehicle:
    def __init__(self, model_name, color, engine_cc, weight, speed):
        self.__model_name = model_name
        self.__color = color
        self.__engine_cc = engine_cc
        self.__weight = weight
        self.__speed = speed

    def get_model_name(self):
        return self.__model_name

    def get_specifications(self):
        return {
            'Model Name': self.__model_name,
            'Color': self.__color,
            'Engine CC': self.__engine_cc,
            'Weight': self.__weight,
            'Speed': self.__speed
        }


class TwoWheeler(Vehicle):
    def __init__(self, model_name, color, engine_cc, weight, speed):
        super().__init__(model_name, color, engine_cc, weight, speed)
        return


class ThreeWheeler(Vehicle):
    def __init__(self, model_name, color, engine_cc, weight, speed):
        super().__init__(model_name, color, engine_cc, weight, speed)
        return


class FourWheeler(Vehicle):
    def __init__(self, model_name, color, engine_cc, weight, speed):
        super().__init__(model_name, color, engine_cc, weight, speed)
        return


class VehicleManagementSystem:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def get_vehicle_models(self, vehicle_type=None):
        if vehicle_type is None:
            return [vehicle.get_model_name() for vehicle in self.__vehicles]
        else:
            return [vehicle.get_model_name() for vehicle in self.__vehicles if isinstance(vehicle, vehicle_type)]

    def get_vehicle_specifications(self, model_name):
        for vehicle in self.__vehicles:
            if vehicle.get_model_name() == model_name:
                return vehicle.get_specifications()
        return "Vehicle not found"


if __name__ == "__main__":
    vms = VehicleManagementSystem()

    activa = TwoWheeler("Activa", "Red", 109.19, 110, 80)
    tvs = TwoWheeler("TVS", "Black", 109.7, 105, 82)
    royal_enfield = TwoWheeler("Royal Enfield", "Blue", 346, 195, 130)

    auto = ThreeWheeler("Auto", "Yellow", 170, 450, 60)
    tempo = ThreeWheeler("Tempo", "White", 720, 1500, 40)

    swift = FourWheeler("Swift", "Silver", 1197, 890, 150)
    i10 = FourWheeler("i10", "Grey", 1197, 845, 145)

    print(vms.add_vehicle(activa))
obj= VehicleManagementSystem()
obj.get_vehicle_models()