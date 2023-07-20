# class Point:
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coords(self):
#         return (self.x, self.y)
# pt = Point() # Создаём экземпляр класса
# pt2 =Point()
# pt.set_coords(1, 2)
# pt2.set_coords(10, 20) # В pt добавляем значения x и y(1, 2)
# print(pt.__dict__) # Прочитаем, что есть в экземпляре pt
# print(pt2.__dict__)
# print(pt.get_coords())

class Zombie:
    hp = 5000
    speed = 6000

    def attack(self,damage, speed_attack):
        self.damage = damage
        self.speed_attack = speed_attack
pt = Zombie()
pt2 = Zombie()
pt2.attack(70, 34)
pt.attack(60, 20)
print(pt.__dict__)
print(pt2.__dict__)



