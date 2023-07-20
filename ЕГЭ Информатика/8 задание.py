# a = 'БАЛКОН'
# c = 0  #Счетчик
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     s =i+j+k+l+m   #Составляем слово
#                     if 'Б' in s:  #Условие если в слове хотя бы есть одна буква Б
#                     if s.count('Б') >=2: # Считает, если в слове Больше или равно букв Б
#                         print (s)
#                         c +=1
# print(c)


# a = 'АБВГДЯ'
# a1 = 'АБВГД'
# c = 0
# for i in a:
#     for j in a1:
#         for k in a1:
#             for l in a:
#                 s =i+j+k+l #4-буквенное слово
#                 if s.count('Я') <=1:
#                     c +=1
#                 print (s)
# print(c)


# a = 'МАНОК'
# a1 = 'МАНК'
# c = 0
# for i in a1:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     s =i+j+k+l+m
#                     if  (not 'АО' in s) and (s.count('М') == 1) and (s.count('А') == 1) and (s.count('Н') == 1) and (s.count('О') == 1) and(s.count('К') == 1): # Каждая буква используется ровно один раз
#                         print(s)
#                         c += 1
#
# print (c)


a1 = '1357'
a2 =  '0246'

# c = 432
# for i in a1:
#     for j in a2:
#         for k  in a1:
#             for l  in a2:
#                 for m in a1:
#                     for n in a2:
#                         s =i+j+k+l+m+n
#                         if len(set(s)) == 6:   # Делает проверку, что все цифры разные
#                             print(s)
#                             c += 1
# print(c)

# a = 'ПИР'
# c=0
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     s = i+j+k+l+m
#                     if s.count('П') == 1:
#                         print(s)
#                         c +=1
# print(c)


a = 'МАНОК'
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i+j+k+l+m
                    if ()