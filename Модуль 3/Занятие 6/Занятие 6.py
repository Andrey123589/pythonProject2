# class Year:
#     def __init__(self):
#         self.__days = 365
#     def get_days(self):
#         return self.__days
#
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise ValueError(f'Некорректное значние аотрибута: {days}')
#
# year = Year()
# print(year.get_days())
# year.set_days(366)
# print(year.get_days())
# year.set_days(367)


class Person:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return  self.__age #Геттер

    @age.setter  #Сеттер
    def age(self, age):
        if age < 0:
            raise ValueError("Вы кш==еше не родились")
        self.__age = age

person = Person("АВЫ", 16)
print(person.age) # 16
person.age = 15  #Меняем на 15
print(person.age) # 15
person.age = -15