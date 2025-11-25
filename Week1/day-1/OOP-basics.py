#exercise
## TODO: Create a Car class
# Properties: brand, model, year
# Methods: start_engine(), stop_engine(), get_info()
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
        
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} engine started!"
        return "Engine already running"
    
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} engine stoped!"
        return "Engine already off"
    
    def get_info(self):
        status = "running" if self.is_running else "off"
        return f"{self.year} {self.brand} {self.model} -Engine {status}"
    
my_car = Car("Toyota", "Avanza", 2020)
print(my_car.start_engine())
print(my_car.get_info())      
print(my_car.stop_engine())