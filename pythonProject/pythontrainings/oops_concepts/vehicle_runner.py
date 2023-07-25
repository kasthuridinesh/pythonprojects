from pythontrainings.oops_concepts.list_of_vehicle import ThreeWheeler, FourWheeler, TwoWheeler

print("...............Two Wheeler..................")
two_wheeler = TwoWheeler("Royal enfield", "Hunter", "blue", "350cc", "120kms/hr")
two_wheeler.display_details()

print("...............Three Wheeler..................")
three_wheelers_vehicle = ThreeWheeler("Mahendra", "Alpha plus", "Black", "120cc", "90kms/hr")
three_wheelers_vehicle.display_details()

print("...............Four Wheeler..................")
four_wheeler_vehicle = FourWheeler("Duster", "Alpha plus", "Grey", "420cc", "180kms/hr")
four_wheeler_vehicle.display_details()
