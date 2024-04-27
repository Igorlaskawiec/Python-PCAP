class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    def __str__(self):
            return f'Model: {self.model}, Color: {self.color}, Year: {self.year}'


def get_car_info():
    model = input("Enter the car model: ")
    color = input("Enter the car color: ")
    year = input("Enter the car year: ")
    return Car(model, color, year)

car_database = dict()

car_database['Toyota'] = Car('Toyota', 'Red', '2020')
car_database['Honda'] = Car('Honda', 'Blue', '2019')


def add_car():
    while True: 
        new_car = get_car_info()
        car_database[new_car.model] = new_car
        add_more = input("Do you want to add more cars? (yes/no): ")
        if add_more.lower() != 'yes':
            break

def remove_car():
    car_model = input("Enter the car model you want to remove: ")
    if car_model in car_database:
        del car_database[car_model]
    else:
        print(f'{car_model} not found in the database')

def print_car_database():
    for car_model, car_info in car_database.items():
        print(f'Car Info: {car_info}')
    print('------------------')


#MAIN FUNCTION
def main():
    while True:
        print("What you want to do?\n1. Add a car\n2. Remove a car\n3. Print the car dagittabase\n4. Exit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_car()
        elif choice == '2':
            remove_car()
        elif choice == '3':
            print_car_database()
        elif choice == '4':
            break


main()