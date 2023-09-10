class Automobile:
    def __init__(self, make, model, year, color, mileage):  # constructor function
        # underscores prevent unintentional access to these variables.
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__mileage = mileage

    def __str__(self):  # method for when the class is returned as a string
        return f"{self.__year} {self.__color} {self.__make} {self.__model} with {self.__mileage} miles"

    def update(self, attribute, value):  # updating values method
        if attribute == 'make':
            self.__make = value
        elif attribute == 'model':
            self.__model = value
        elif attribute == 'color':
            self.__color = value
        elif attribute == 'year':
            self.__year = int(value)
        elif attribute == 'mileage':
            self.__mileage = int(value)
        else:
            print(f"Attribute {attribute} not found.")


class Garage:
    def __init__(self):
        self.collection = []

    def output_to_file(self, filename="collection.txt"):
        print("Attempting to write to file...")  # Debugging print statement
        with open(filename, 'w') as file:
            for automobile in self.collection:
                file.write(str(automobile) + '\n')
        print(f"The inventory was exported to file: {filename}")

    def add_automobile(self, automobile):  # add to collection of automobiles
        self.collection.append(automobile)

    def remove_automobile(self, index):  # remove vehicle at a specific index
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


def main():
    my_garage = Garage()

    while True:
        print("Welcome to your garage! Choose an option:\n")
        print("1.) Add a vehicle.")
        print("2.) Remove a vehicle.")
        print("3.) Update a vehicle.")
        print("4.) List all vehicles and output to a file.")
        print("5.) Exit")

        choice = input("* ")

        if choice == '1':
            make = input("Enter the vehicle's make: ")
            model = input("Enter the vehicle's model: ")
            color = input("Enter the vehicle's color: ")
            year = int(input("Enter the vehicle's year: "))
            mileage = int(input("Enter the vehicle's mileage: "))
            automobile = Automobile(make, model, color, year, mileage)
            my_garage.add_automobile(automobile)
            print("Vehicle added.")

        elif choice == '2':
            index = int(input("Enter the index of the vehicle you would like to remove: "))
            my_garage.remove_automobile(index)

        elif choice == '3':
            index = int(input("Enter the index of the vehicle to update: "))
            attribute = input("Would you like to update the make, model, color, year, or mileage? (Pick one): ")
            value = input("Enter the new value: ")
            my_garage.update_automobile(index, attribute, value)
            print("Vehicle updated.")

        elif choice == '4':
            my_garage.output_to_file()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            "Invalid choice."


if __name__ == "__main__":
    main()
