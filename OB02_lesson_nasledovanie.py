class Bird():
    def __init__(self,name,voice,color):
        self.name = name
        self.voice = voice
        self.color = color
    
    def fly(self):
        print(f"{self.name} flying")
    
    def eat(self):
        print(f"{self.name} eating")
    
    def sing(self):
        print(f"{self.name} singing -{self.voice}")
    
    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - цвет")

class Pigeon(Bird):
    def __init__(self,name,voice,color, favorite_food):
        super().__init__(name,voice,color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} singing - soprano")
    
    def walk(self):
        print(f"{self.name}  ходит")

bird1 = Pigeon("Gosha", "bas", "red", "bread")
bird2 = Bird("Masha", "alt", "yellow")

bird1.sing()
bird1.info()
bird1.walk()


    

