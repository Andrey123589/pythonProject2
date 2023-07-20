#Все это в 6 строчек
# my_list= []
#
# for i in range(1000):
#     my_list.append(i)
#
# print(my_list)

# Теперь же в 1 строчку
# my_list= [i for i in range(1000)]  #**2 Квадратами чисел; Ответ 0,1,4,9,16,25,36
# print(my_list)



# Выводит те числа, которые делятся на 5; Ответ: 0,5,10,15...
# for i in range(1000):
#     if i % 5 == 0:  Делит число на 5
#         my_list.append(i)
# print(my_list)
# my_list = []

# Теперь в одну строчку
# my_list = [i if i % 5  == 0 else i * 5 for i in range(1000) if i % 3 ==0]
# print(my_list)

#my_dict= {i:len(i) for i in ['первый', 'второй', 'АНдрейкрасвачик'] if  len(i) !=6}  #Длина списка не должна равняться 6
#print((my_dict))   # !=-не равняется

# my_list_1 = [1,2]   # Первое айди
# my_list_2 =[1,2]    # ВТорой айди
# a = 10
# b = 10
#
# print(my_list_1 is my_list_2)  # is это сравнение двух объектов
# print(a is b)
# print(id(my_list_2), id(my_list_1))
# print(id(a), id(b))


# my_tuple = (3, 5, 4)  #tuple-кортеж, его нельзя изменять
# print(my_tuple)
# print(type(my_tuple))
# element  = my_tuple[2]
# print(element)
#
# my_dict = {
#     ('cacsks'): '+743222674636'
# }
# print(my_dict)

# print(sorted(my_tuple))  # sorted сортировка чисел по возрастанию


# my_list =[1, 2, 3]
# print(tuple(my_list)) #Превращаем список в кортеш   list()   or tuple

my_tuple = (i for i in range(0,1000))
print(type(my_tuple))