#parent Class
class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

#child class
class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)

print("Vehcile name:", school_bus.name, "\nspeed:", school_bus.max_speed,"\nmileage:", school_bus.mileage)