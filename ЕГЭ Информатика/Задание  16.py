# def vozrast(year):
    # return year-2000  # return, то же самое, что знак равно
# print(vozrast(2050))

# def F(n):
#     if n == 0:
#         return 1
#     if  n == 1:
#         return 1
#     if n>1:
#         return F(n-1)*F(n-2)+1
# print(F(6))

# def F(n):
#     if n == 1:
#         return 1
#     if n%2 == 0:  #Определяем четное число или нет, если не равно нулю, то число не четное и идет дальше к else:
#         return n+2+F(n-1)
#     else:
#         return 2*F(n-2)
# print(F(24))

#def F(n):
  #  if n == 0:
      #  return 0
   # if n == 1:
      #  return 1
   # if n>1 and n%2== 0:
       #return 2+int(3* F(n-1) / 3)  #Целая часть числа это округление в меньшую сторону 15.8=15
   # if n >1 and n%2 != 0:  # != (не равно) n%2 != 0 значит число нечетное
     #   return  2*n +(F(n-1) +F(n-3) +2) //3  #Можно с помощью int или же при помощи //- целочисленное деление
#print(F(30))

# def F(n):
#     if n == 1:
#         return 2
#     if n>1:
#         return F(n-1)- G(n-1)
# def G(n):
#     if n == 1:
#         return 1
#     if n >=2:
#         return (F(n-1)) +G(n-1)
# print(F(5)/ G(5))
# import sys
# sys.setrecursionlimit(1000000)
# def F(n):
#     if n ==1:
#         return 1
#     if n>1:
#         return n*F(n-1)
# print(F(2023)/ F(2021))
import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n==1:
        return 1
    if n>1:
        return n*F(n-1)
print(F(2023)/F(2021))

