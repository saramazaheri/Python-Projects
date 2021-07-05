from proj3 import Cars

class HybridCars(Cars):
    def __init__(self, type, cost, speed, company, hybridType, color = ['wite','blue','red','black','gray']):
        super().__init__(type, cost, speed, company, color)
        self.hybridType = hybridType
        
    def get_info(self):
        print(f"type: {self.type}")
        print(f"cost: {self.cost}$")
        print(f"speed: {self.speed}")
        print(f"company: {self.company}")
        print(f"hybridType: {self.hybridType}")

car1 = HybridCars('2 Series',42095,248,'BMW 2 Series',2)

#car1.color_cheking() 
#car1.get_info()