class Car:
    def __init__(self, make, model):
        self.public_make = make
        self._protected_model = model
        self.__private_year = 2022

    def public_method(self):
        return f"Это публичный метод. Машина:{self.public_make} {self._protected_model}."
    def _protected_method(self):
        return "Это защищенный метод"
    def __private_method(self):
        return "Это приватный метод"
class ElectricCar(Car):
    def __init__(self, make, model, battary_size):
        super().__init__(make, model)
        self.battary_size = battary_size
    def get_details(self):
        details = f"{self.public_make} {self._protected_model}, батарея:{self.abttary_size} kw."
        return details
    
tesla = ElectricCar("tesla", "Model S", 100)
print(tesla.public_make)
print(tesla.public_method())

print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__private_year)