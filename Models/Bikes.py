class Garrage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printDetails(self):               
        print(f"{self.name} is a bike and it costs {self.price} dollars.")