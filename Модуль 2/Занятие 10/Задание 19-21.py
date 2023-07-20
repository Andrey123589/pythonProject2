def WIN1 (S):
    if 2*S >=29 or S +1 >= 29:
        return True
    else:
        return False
def WIN2(S):
    if LOSS1(2*S) or LOSS1(S+1):
        return True
    else:
        return False

def LOSS1(S):
    if (not(WIN1(S))) and WIN1(2*S)  and WIN1(S+1):

for S in range(1, 29):
    if  WIN1(2*S) and WIN1(S+1):
        print(S)