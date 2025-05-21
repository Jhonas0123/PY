class Car:
    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El coche {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El coche {self.brand} {self.model} no esta disponible.")

    def check_availability(self):
        return self.is_available
     
    def get_price (self):
        return self.price
    
class  Costumer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []

    def buy_car(self, car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo siento, {car.brand} {car.model} no esta disponible.")

    def inquire_car(self, car):
        availability = "disponible" if car.check_availability() else "no esta disponible"   
        print(f"El coche {car.brand} {car.model} esta {availability} y cuesta {car.price}")    

class Dealership:
    def __init__(self):
        self.inventory = []
        self.costumers = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido agragado al inventario")

    def register_costumer(self, costumer):
        self.costumers.append(costumer)
        print(f"El cliente {costumer.name} ha sido registrado")

    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"{car.brand} {car.model} por {car.price}")

# Crear instancias de coches
car1 = Car("Toyota", "Corolla", "20000")
car2 = Car("Honda","Civic", "22,000")
car3 = Car("Ford","Mustang", "35,000")

# Crear instancia de cliente
costumer1 = Costumer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealer = Dealership()
dealer.add_car(car1)
dealer.add_car(car2)
dealer.add_car(car3)
dealer.register_costumer(costumer1)

#Mostrar coches disponibles
dealer.show_available_cars()

# cliente consulta un coche
costumer1.inquire_car(car1)
#cliente compra coche 
costumer1.buy_car(car1)
# Mostrar coches disponibles nuevamente
dealer.show_available_cars()
#cliente intenta comprar un coche ya vendido    
costumer1.buy_car(car1)