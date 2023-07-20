# def strcount(s): # O(N**2)
#     for sym in set(s):
#         counter=0
#         for sub_sum in s:
#             if sym== sub_sum:
#                 counter+=1
#                 print(sym,counter)
#
#
# strcount('abac')


def strcount(s):
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) +1

    for key,value, in dct.items():
        print(key,value)

        
strcount('aaabcd')
