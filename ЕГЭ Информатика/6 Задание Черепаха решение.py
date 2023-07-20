# for x in '0123456789':
#   t = int('4C'+x + '4', 15)+ int(x + '62A', 13)
#   if t % 121 == 0:
#       print(t // 121)
#
# for x in '0123456789':
#     t  = int('28'+ x+ '2', 18)+ int('93'+ x + '5', 12)
#     if t % 133 == 0:
#         print(t // 133)
#
# for x in '0123456789ABCDEF':
#     t  = int('2'+x + '84',19)+ int('2B3'+ x, 16)
#     if t % 88 == 0:
#         print(t // 88)
#
#
# for x in '0123456789':
#     t = int('3'+ x + 'DA',14)+ int( '5'+ x + 'A6',12)
#     if t % 81 == 0:
#         print( t // 81)
#
# s  = '8' * 68
# while ('222' in s) or ('888'in s):
#     if ('222'in s):
#        s = s.replace('222','8',1)
#     else:
#        s = s.replace('888','2',1)
# print (s)

# s='8'*68
# while ('222' in s) or ('888' in s):
#     if ('222' in s):
#          s=s.replace ('222','8',1)
#     else:
#          s=s.replace ('888','2',1)
#
# print(s)


# s = 'АБЗИ'
# for i in s:
#     for j in s:
#         for k in s:
#             for l in s:
#                 s  = i+j+k+l
#                 if s.count('И') == 1 and s.count('З') == 1 and s.count('Б') == 1 and s.count('А') == 1:
#                    print (s)
#


from itertools import *
words = product('размах', repeat=6)
K = set()
for w in words:
    word = ''.join(w)
    print (word)
    if  (word.count('р') +word.count('з')+ word.count('м') + word.count('х')) >=3:
        K.add(word)
print(len(K))
