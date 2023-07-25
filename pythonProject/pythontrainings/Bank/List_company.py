class Companylist:
    def __init__(self):
        return None
    def __list_company(self):
        print("\n 1.Infosys,\n 2.CTS,\n 3.Capgemini,\n 4.Wipro,\n 5.Accenture,\n 6.Robosoft")
        enter_choice = int(input("enter your choice:"))
        if enter_choice == 1:

            print("welcome to Infosys")
        elif enter_choice == 2:
            print("welcome to CTS")
        elif enter_choice == 3:
            print("welcome to Capgemini")
        elif enter_choice == 4:
            print("welcome to Wipro")
        elif enter_choice == 5:
            print("welcome to Accenture")
        elif enter_choice == 6:
            print("welcome to Robosoft")
