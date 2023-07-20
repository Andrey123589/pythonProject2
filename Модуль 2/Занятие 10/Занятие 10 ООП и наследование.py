# class A:
#     def info(self):
#         print("Это класс A")
#
#
# a =A()
# a.info()
#
#
# class B(A):
#     pass
#
#
# b = B()
# b.info()

class Pet:
   def __init__(self, has_tail, legs, name, animal):
       self.has_tail =has_tail
       self.legs = legs
       self.name = name
       self.animal = animal

   def __str__(self):
         #Возвращает строку
       # Выводим информацию о животном при помощи {self.name}. {self.legs} и.т.д
        # \ перед " нажимаем пробел и строка автоматически переносится с знаком \
       result =f"Питомец {self.name}. Это {self.animal}." \
          #      f" У него  {'есть хвост'  if self.has_tail  else 'хвоста нет' }. У него {self.legs} ног(и)"

      #  return result

   # def sound(self):
        #pass

#class Dog(Pet):
    #Остальная информация выводится по типу наследования, в данном случае меняется тольок name и animal,
    # другие данные получаются из class Pet
   # name = "Чарли"
   # animal = "Собака"
   # def sound(self):   #Дополнительная функция sound - звук
 #       return "ГАВ"
#print(Dog(), Dog().sound())  #Выводим собаку и его функцию, то есть звук

#class Frog(Pet):
  #  has_tail = False  # has_tail False, потому что у лягушки нет хвоста
  #  name = "Пепе"
  #  animal = "Лягушка"
  #  def sound(self):
  ##      return "КАВ"


#print(Frog(), Frog().sound())  # Frog().sound выводим функцию sound


#
# class People:
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# vanya = People ("vanya", 18)
# dima = People('dima', 17)
#
# print(vanya.name)















