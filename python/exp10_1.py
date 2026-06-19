class vechicle:
   def __init__(self,brand,model,hp,year):
      self.brand=brand
      self.model=model
      self.hp=hp
      self.year=year
   def display(self):
      print("Brand:",self.brand)
      print("Model:",self.model)
      print("HP:",self.hp)
      print("year of manufatoring:",self.year)
x1=vechicle("BMW","M5",360,2018)
x2=vechicle("Nissan","GTR",400,2012)
x1.display()
x2.display()
