class Vehicle:
    def __init__(self, color, maxSpeed) -> None:
        self.__color = color
        self.maxSpeed = maxSpeed

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color


class Car(Vehicle):
    def __init__(self, color, maxSpeed, numberOfGears, isConvertible) -> None:
        super().__init__(color, maxSpeed)
        self.numberOfGears = numberOfGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Car Color : ", self.getColor())
        print("Car Max Speed: ", self.maxSpeed)
        print("Car Number Of Gears: ", self.numberOfGears)
        print("Car isConvertible: ", self.isConvertible)


c1 = Car("Black", 500, 6, False)

c1.printCar()
