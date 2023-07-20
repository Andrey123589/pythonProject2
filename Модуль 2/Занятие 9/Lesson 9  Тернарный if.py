#age = 17
#В 4 строки
#if age>= 18:
   # is_allow = "Можно"
#else:
  #  is_allow= "Нельзя"

# #print(is_allow)
# # В одну строку
# criminal_record = False
# is_allow = "Можно"if age >= 18  or criminal_record else "Нельзя"
#
# print(is_allow)

#a= 1000
#b= 1500
#c=a or b   # Если в первом уже True, то на вторую он даже не смотрит; Ответ будет 1000
#print(c)

age = 18

is_allow = True if age >= 18 else False

print(is_allow)