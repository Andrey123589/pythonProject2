goods = [
    {
        'name': 'Iphone',
        'brand': 'Apple',
        'price': 100,
    },
    {
        'name': 'Ipad',
        'brand': 'Apple',
        'price': 50,
    },
    {
        'name': 'Windows XP',
        'brand': 'Microsoft',
        'price': 150,

    }
]

# def on_price(item):
#     return item['price']

# print(sorted(goods, key=lambda item: item['price']))

#
# filtered_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
# print((filtered_list))




#
# numbers = ['1', '2', '3', '4', '5']
# print(numbers)
# result = list(map(int,numbers))
# print(result)



# names_list = ['Igor', 'Артем', 'Аня', 'Ксюша']
# surnames = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']
#
# persons = list(map(lambda name, surnames: f'{name} {surnames}', names_list,surnames))
#
# print(persons)



#
# names = ['Андрей', 'Паша', 'Кирилл', 'Вова']
# surnames = ['Иванов', 'Павлов', 'Алмазов']
#
# people = list(map(lambda namess, surnamess: f'{namess} {surnamess}', names,surnames))
#
# print(people)



#
# goods = [1, 2, 3, 4, 5, 6]
# for index, item in enumerate(goods):
#     print(index, item)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[-1]) # [] индекс определяет

# new_goods = []
#
# for index, item in enumerate(goods):
#     new_goods.append({index: item})

# print(new_goods)



#
# names = ['Андрей', 'Паша', 'Кирилл', 'Вова']
# surnames = ['Иванов', 'Павлов', 'Алмазов']
#
# for names, surnames in zip(names, surnames):
#     print(names,surnames)


print(__name__)













