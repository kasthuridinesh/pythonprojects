from pythontrainings.oops_concepts.vehicle_management import ThreeWheeler, TwoWheeler, FourWheeler

print("....... printing list of two wheeler............")
vehicle= TwoWheeler()
vehicle.display_all_vehicles()
vehicle.vehicle_specification('BAJAJ')

print("........printing list of Three wheeler ........")
vehicle= ThreeWheeler()
vehicle.display_all_vehicles()
vehicle.vehicle_specification('AUTO')

print("........printing list of four wheeler ........")
vehicle= FourWheeler()
vehicle.display_all_vehicles()
vehicle.vehicle_specification('BMW')





