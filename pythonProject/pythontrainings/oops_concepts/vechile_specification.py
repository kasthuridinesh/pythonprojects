class Vehicle:
    def __init__(self, model, type_of_vehicle):
        self.model = model
        self.type_of_vehicle = type_of_vehicle


class TwoWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed):
        super().__init__(model, type_of_vehicle="Two-wheeler")
        self.color = color
        self.engine_cc = engine_cc
        self.weight = weight
        self.speed = speed


class ThreeWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed, no_of_wheels):
        super().__init__(model, type_of_vehicle='Three Wheeler')
        self.color = color
        self.engine_cc = engine_cc
        self.weight = weight
        self.speed = speed
        self.no_of_wheels = no_of_wheels


class FourWheeler(Vehicle):
    def __init__(self, model, color, engine_cc, weight, speed, no_of_doors):
        super().__init__(model, type_of_vehicle='Four Wheeler')
        self.color = color
        self.engine_cc = engine_cc
        self.weight = weight
        self.speed = speed
        self.no_of_doors = no_of_doors


def show_vehicle_list(vehicles):
    for vehicle in vehicles:
        print(vehicle.model)


def show_vehicle_specifications(vehicles, model):
    for vehicle in vehicles:
        if vehicle.model == model:
            print(f'Model: {vehicle.model}')
            print(f'Type of Vehicle: {vehicle.type_of_vehicle}')
            print(f'Color: {vehicle.color}')
            print(f'Engine CC: {vehicle.engine_cc}')
            print(f'Weight: {vehicle.weight}')
            print(f'Speed: {vehicle.speed}')
            if hasattr(vehicle, 'no_of_wheels'):
                print(f'Number of Wheels: {vehicle.no_of_wheels}')
            if hasattr(vehicle, 'no_of_doors'):
                print(f'Number of Doors: {vehicle.no_of_doors}')


vehicles = [TwoWheeler('Jupiter', 'Red', 109, 110, 70),
            TwoWheeler('Activa', 'Black', 110, 120, 75),
            ThreeWheeler('Auto', 'Green', 200, 250, 60, 3),
            FourWheeler('Car', 'Red', 1500, 1700, 120, 4)]

print('List of Vehicles:')
show_vehicle_list(vehicles)

print('\nVehicle Specification:')
show_vehicle_specifications(vehicles, 'Activa')
