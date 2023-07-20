# f = open('test.txt', 'w', encoding='UTF-8')
# f.write("Скоро лето")
# f.close()

from contextlib import contextmanager
# with open('test.txt', 'w', encoding='UTF-8') as f:
#     f.write('СКоро лето, а сейчас лето')
#     print(f.closed)
# print(f.closed)


my_list = [1, 2]

@contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        print('БЫла ошибка')



with exc_handler(IndexError):
    my_list[4]