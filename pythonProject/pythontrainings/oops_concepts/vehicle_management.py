from pythontrainings.oops_concepts import variable_constants


class Vehicle:
    """
            This method is constructor for Vehicle class file
            """

    def __init__(self):
        self.__brand = None

    def vehicle_specification(self, brand):
        """
        This method returns the vehicle specification for given brand
        of the vehicle
        """
        print(f'The specification of given vehicle brand is {brand}')

    def display_all_vehicles(self):
        """
        This method displays all the vehicles
        """
        print(f'The vehicle list {vehicles}')


class TwoWheeler(Vehicle):
    def __init__(self):
        """
        This method is constructor for TwoWheeler class file, and it overrides Vehicle class file
        """
        super().__init__()
        self.__brand = None

    def vehicle_specification(self, brand):

        self.__brand = brand
        for vehicle in vehicles:
            if vehicle[variable_constants.BRAND] == self.__brand and \
                    vehicle[variable_constants.TYPE] == variable_constants.TWO_WHEELER:
                print(f'The specification of given brand is {vehicle}')

    def display_all_vehicles(self):

        for vehicle in vehicles:
            if vehicle[variable_constants.TYPE] == variable_constants.TWO_WHEELER:
                print(vehicle)


class BiCycle(TwoWheeler):
    def __init__(self):
        """
        This method is constructor for BiCycle class file, and it overrides TwoWheeler class file
        """
        super().__init__()
        self.__brand = None

    def vehicle_specification(self, brand):
        """
        This method returns the vehicle specification for given brand
        of the vehicle
        """
        self.__brand = brand
        for vehicle in vehicles:
            if vehicle[variable_constants.BRAND] == self.__brand and \
                    vehicle[variable_constants.TYPE] == variable_constants.TWO_WHEELER \
                    and vehicle['engine present'] == 'No':
                print(f'The specification of given brand is {vehicle}')

    def display_all_vehicles(self):
        """
        This method displays all the vehicles
        """
        for vehicle in vehicles:
            if vehicle[variable_constants.TYPE] == variable_constants.TWO_WHEELER \
                    and vehicle['engine present'] == 'No':
                print(vehicle)


class ThreeWheeler(Vehicle):
    def __init__(self):
        """
        This method is constructor for ThreeWheeler class file, and it overrides Vehicle class file
        """
        super().__init__()
        self.__brand = None

    def vehicle_specification(self, brand):
        """
        This method returns the vehicle specification for given brand
        :param brand: of the vehicle
        """
        self.__brand = brand
        for vehicle in vehicles:
            if vehicle[variable_constants.BRAND] == self.__brand and \
                    vehicle[variable_constants.TYPE] == variable_constants.THREE_WHEELER:
                print(f'The specification of given brand is {vehicle}')

    def display_all_vehicles(self):
        """
        This method displays all the vehicles
        """
        for vehicle in vehicles:
            if vehicle[variable_constants.TYPE] == variable_constants.THREE_WHEELER:
                print(vehicle)


class FourWheeler(Vehicle):
    def __init__(self):
        """
        This method is constructor for FourWheeler class file, and it overrides Vehicle class file
        """
        super().__init__()
        self.__brand = None

    def vehicle_specification(self, brand):
        """
        This method returns the vehicle specification for given brand
        of the vehicle
        """
        self.__brand = brand
        for vehicle in vehicles:
            if vehicle[variable_constants.BRAND] == self.__brand and \
                    vehicle[variable_constants.TYPE] == variable_constants.FOUR_WHEELER:
                print(f'The specification of given brand is {vehicle}')

    def display_all_vehicles(self):
        """
        This method displays all the vehicles in list
        """
        for vehicle in vehicles:
            if vehicle[variable_constants.TYPE] == variable_constants.FOUR_WHEELER:
                print(vehicle)


vehicles = [
    {'brand': 'AUDI', 'type_of_vehicle': 'Four Wheeler', 'fuel': 'Diesel', 'mileage': '19896',
     'registration_year': '2017', 'transmission': 'Handbediende versnellingsbak', 'price': 17800,
     'engine present': 'Yes'},
    {'brand': 'BMW', 'type_of_vehicle': 'Four Wheeler', 'fuel': 'Diesel', 'mileage': '87354',
     'registration_year': '2013', 'transmission': 'Handbediende versnellingsbak', 'price': 52000,
     'engine present': 'Yes'},
    {'brand': 'SKODA', 'type_of_vehicle': 'Four Wheeler', 'fuel': 'Diesel', 'mileage': '90613',
     'registration_year': '2012', 'transmission': 'Handbediende versnellingsbak', 'price': 11000,
     'engine present': 'Yes'},
    {'brand': 'YAMAHA', 'type_of_vehicle': 'Two Wheeler', 'fuel': 'Diesel', 'mileage': '47402',
     'registration_year': '2016', 'transmission': 'Sequentiele bak', 'price': 93000,
     'engine present': 'Yes'},
    {'brand': 'ACTIVA', 'type_of_vehicle': 'Two Wheeler', 'fuel': 'Essence', 'mileage': '28588',
     'registration_year': '2017', 'transmission': 'Handbediende versnellingsbak', 'price': 87000,
     'engine present': 'Yes'},
    {'brand': 'HERO HONDA', 'type_of_vehicle': 'Two Wheeler', 'fuel': 'Diesel', 'mileage': '66053',
     'registration_year': '2014', 'transmission': 'Handbediende versnellingsbak', 'price': 62000,
     'engine present': 'Yes'},
    {'brand': 'BAJAJ', 'type_of_vehicle': 'Three Wheeler', 'fuel': 'Diesel', 'mileage': '47402',
     'registration_year': '2016', 'transmission': 'Sequentiele bak', 'price': 93000,
     'engine present': 'Yes'},
    {'brand': 'AUTO', 'type_of_vehicle': 'Three Wheeler', 'fuel': 'Essence', 'mileage': '28588',
     'registration_year': '2017', 'transmission': 'Handbediende versnellingsbak', 'price': 87000,
     'engine present': 'Yes'},
    {'brand': 'TVS', 'type_of_vehicle': 'Three Wheeler', 'fuel': 'Diesel', 'mileage': '66053',
     'registration_year': '2014', 'transmission': 'Handbediende versnellingsbak', 'price': 62000,
     'engine present': 'Yes'},
    {'brand': 'Hero', 'type_of_vehicle': 'Two Wheeler', 'fuel': 'NA', 'mileage': 'NA',
     'registration_year': '2014', 'transmission': 'Handbediende versnellingsbak', 'price': 62000,
     'engine present': 'No'}
]
