class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f'{self.brand} {self.model} engine started')
        
    def stop_engine(self):
        print(f'{self.brand} {self.model} engine stopping...')