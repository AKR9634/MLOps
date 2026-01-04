class vehicle:

    def __init__(self, name = "General vehicle"):
        self.name = name

    def drive():
        pass


class bike(vehicle):

    def __init__(self, name = "B"):
        super().__init__(name)

    def drive(self):
        print(f"Hey that's a {self.name} bike!!! \n")

class car(vehicle):

    def __init__(self, name = "C"):
        super().__init__(name)

    def drive(self):
        print(f"Hey that's a {self.name} car!!! \n")
        

b = bike("Blaze Cruiser")

c = car("Aston Martin Valhalla")

b.drive()
c.drive()
nb.drive()
