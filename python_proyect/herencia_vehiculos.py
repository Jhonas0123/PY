"""POO-Herencia"""

class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulacion
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. no esta dispobible")

    #abstraccion
    def check_available(self):
        return self.is_available
    
    #abstraccion
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la sub clase")
    


    # herencia

    # clase hija

class Car(Vehicle):
    #polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"el motor del coche {self.brand} esta en marcha"
        else:
            return f"el coche {self.brand} no esta dispobible"
    #polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"el motori del coche {self.brand} se ha detenido"
        else:
            return f"el coche {self.brand} no esta disponible"
        
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"la bicicleta {self.brand} esta en marcha"
        else:
            return f"la bicicleta {self.brand} no esta dispobible"
    def stop_engine(self):
        if self.is_available:
            return f"la bicicleta {self.brand} se ha detenido"
        else:
            return f"la bicicleta {self.brand} no esta disponible"
        
# herencia
class Truck(Vehicle):
    #polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta dispobible"
    #polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} se ha detenido"
        else:
            return f"lEl camion {self.brand} no esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"lo siento, {vehicle.brand} no esta disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print (f" el {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"el {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "Mt-07", 7000)
truck1 = Truck("Volvo", "fh16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#mostar vehiculos disponibles

dealership.show_available_vehicle()

#cliente consultar un vehiculo 
customer1.inquire_vehicle(car1)

#cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#mostar vehiculos disponibles
dealership.show_available_vehicle()

