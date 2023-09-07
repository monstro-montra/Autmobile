class Automobile:
    def __init__(self, make, model, year, color, mileage): # constructor function
        # underscores prevent unintentional access to these variables.
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__mileage = mileage
    
    def __str__(self): # method for when the class is returned as a string
        return f"{self.__year} {self.__color} {self.__make} {self.__model} with {self.__mileage} miles"
    
    def __update__(self, attribute, value): # updating values method
        if attribute == 'make':
            self.__make = value
        elif attribute == 'model':
            self.__model = value
        elif attribute == 'color':
            self.__model = value
        elif attribute == 'year':
            self.__year = int(value)
        elif attribute == 'mileage':
            self.__mileage int(value)
        else:
            print(f"Attribute {attribute} not found.")

class Garage():
    def __init__(self):
        self.collection = []

    def output_to_file(self, filename="collection.txt"):
        with open(filename, 'w') as file:
            for automobile in self.collection:
                file.write(str(automobile) + '\n')
            print("The inventory was exported to a file named: ")
    
    def add_automobile(self, automobile):
        self.inventory.append(automobile)
    
    def remove_automobile(self, index):
        try:
            del self.collection[index]
            print("Vehicle removed successfully!")
        except IndexError:
            print("Invalid index.")
    
    def update_automobile(self, index, attribute, value):
        try:
            vehicle = self.collection[index]
            vehicle.update(attribute, value)
        except:
            print("Invalid Index.")
    

    def update_automobile(self, index, attribute, value):
        try:
            automobile = self.collection[index]
            automobile.update(attribute, value)
        except IndexError:
            print("Invalid index.")

def main():


if __name__ == "__main__":
    main()



    
