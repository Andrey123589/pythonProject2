class Item:  # Класс
    def __init__(self, name, price, weight): #self общее принятое соглашение, name, price, weight наши условия
        self.name =name
        self.price = price
        self.weight =weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price+other.price #МОжем легко сложить цены потому что у них одинаковый аттрибут(значение) - price
        elif isinstance(other, int):
            return self.price + other

    def __radd__(self, other):  #Правое cложение  item+1000 и 1000+ item для компа не одно и то же
        if isinstance(other, Item):
            return self.price+other.price #МОжем легко сложить цены потому что у них одинаковый аттрибут(значение) - price
        elif isinstance(other, int):
            return self.price + other

item1 =Item('Процессор',15000 , 0.2)   #Указывем имя, потом цену и вес
item2 =Item('Видеокарта',30000 , 0.9)    #Указывем имя, потом цену и вес
item3 = Item('Оперативка', 8000, 0.5)    #Указывем имя, потом цену и вес

# total_sum = item1.price + item2.price
total_sum =item1+item2+item3  #Складываем цены трех предметов
print(total_sum)

