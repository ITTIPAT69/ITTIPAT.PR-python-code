""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model},Year: {self.year} "


class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.__number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model},Year: {self.year}, Number of doors: "

mtCar = Car("Toyota","Prius","2020", 4)
print(myCar.get_info())


