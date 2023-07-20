print ('w x y z ')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (z and w <= y) and (x or y or w ) == True:
                    print (w,x,y,z)



def f(n):
    if n >= 20:
        return n
    if n < 20:
        return  f(n+1)+ f(n+2)
print(f(5)// f(15))


s = '0123456789ABCDEF'
