from Models import Cars, Bikes

cars = {}
bikes = { "b1": None, "b2": None }

def function():
    for i in range(10):
        print(f"Hello, World {i}")

def function2():
    car1 = Cars.Garrage("Toyota", 20000)
    car2 = Cars.Garrage("Honda", 25000)

    # car1.printDetails()
    # car2.printDetails()
    cars["c1"] = car1
    cars["c2"] = car2
    
    bike1 = Bikes.Garrage("Yamaha", 15000)
    bike2 = Bikes.Garrage("Suzuki", 18000)

    bikes["b1"] = bike1
    bikes["b2"] = bike2

    # bike1.printDetails()
    # bike2.printDetails()

def printDetails():
    for car in cars.values():
        car.printDetails()
    
    print("\n")

    for key,bike in bikes.items():
        print(f"Bike key: {key} Details: {bike.name} costs {bike.price} dollars.")
        # bike.printDetails()



function()
function2()
printDetails()
