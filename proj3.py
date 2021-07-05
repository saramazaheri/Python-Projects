class Cars:
    def __init__(self, type, cost, speed, company, color = ['white','blue','red','black','gray']):
        self.type = type
        self.cost = cost
        self.speed = speed
        self.company = company
        self.color = color
    def get_info(self):
        print(f"speed: {self.speed}")
        print(f"cost: {self.cost}$")
        print(f"type: {self.type}")
 
    def color_cheking(self):
        color_input = input('please enter your color :')
        if color_input in self.color:
            print('This color exist for this car.')
        else:
            print('This color does not exist. If you want this color however you must to pay 5000$ more to have this color.')
            add_color = input('Do you want this color? yes or no : ' )
            if add_color == 'yes':
                self.color.append(color_input)
                self.cost += 5000
            else:
                pass    
        
car1 = Cars('2 Series',42095,248,'BMW 2 Series')
car2 = Cars('CLA 250',37645,221,'Mercedes-Benz')
car3 = Cars('A3',36595,228,'Audi')
car4 = Cars('ILX',28645,201,'Acura')
car5 = Cars('C 300',44395,225,'Mercedes-Benz')

#car1.color_cheking() 
#car1.get_info()

#car2.color_cheking()
#car2.get_info()

#car3.color_cheking()
#car3.get_info()

#car4.color_cheking()
#car4.get_info()

#car5.color_cheking()
#car5.get_info()