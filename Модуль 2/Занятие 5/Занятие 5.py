# a = 10
# b = 18
# c = 15
# d = 10
#
# if d < b and c < b:
#     print ("True")
# else:
#     print("False")
#
# my_str =  ''
#
# my_list = []
# my_dict = {}
# if my_str:
#      print("True")
# else:
#      print("False")
# print(id(my_str))

import requests   # Импортируем библиотеку requests
response = requests.get("https://swapi.dev/api/")   #Делаем API из  этого сайта
planets_url = response.json()['planets']  #Json -словарь  можно использовать .get или же квадратные скобки "[]"

response = requests.get(planets_url)
print(response.json())
planets_list = []
for planets in range(1, 6):   #Информация о первых 5 планетах
     detail_planet_url = f'{planets_url}/{planets}'  #Создаем путь для каждой планеты
     response = requests.get(detail_planet_url)   #Получаем информациию
     planets_list.append(response.json())
     data =response.json()
     data['diameter'] =int(data['diameter'])
     planets_list.append(data)
print(planets_list)








