class Yamcha:
   def __init__(self, age):
     self.__age = age

   def get_age(self):
     return self.__age

y1 = Yamcha(50)

print(y1.get_age())

