
strr = input().split()
tab = [0]*len(strr)
i = 0
for s in strr:
    if (s[len(s)-2].upper() == 'K') and (s[len(s)-1]== 'b') : 
            tab[i] = int(s[0:len(s)-2]) * 1024 
    elif (s[len(s)-2].upper() == 'K') and (s[len(s)-1]== 'B') : 
        tab[i] = (int(s[0:len(s)-2]) * 1024 )
    elif (s[len(s)-2].upper() == 'M') and (s[len(s)-1]== 'B') : 
        tab[i] = (int(s[0:len(s)-2]) * 1024 *1024)
    elif (s[len(s)-2].upper() == 'M') and (s[len(s)-1]== 'b') : 
        tab[i] =  (int(s[0:len(s)-2]) *1024*1024// 8 )  if (int(s[0:len(s)-2])*1024*1024 % 8 == 0) else int(s[0:len(s)-2])*1024*1024 / 8
    elif (s[len(s)-2].upper() == 'G') and (s[len(s)-1]== 'B') : 
        tab[i] = (int(s[0:len(s)-2]) * 1024 *1024*1024)
    elif (s[len(s)-2].upper() == 'G') and (s[len(s)-1]== 'b') : 
        tab[i] =  (int(s[0:len(s)-2]) *1024*1024*1024// 8 )  if (int(s[0:len(s)-2])*1024*1024 *1024% 8 == 0) else int(s[0:len(s)-2])*1024*1024*1024 / 8
    elif (s[len(s)-2].upper() == 'T') and (s[len(s)-1]== 'B') : 
        tab[i] = (int(s[0:len(s)-2]) * 1024 *1024*1024*1024)
    elif (s[len(s)-2].upper() == 'T') and (s[len(s)-1]== 'b') : 
        tab[i] =  (int(s[0:len(s)-2]) *1024*1024*1024*1024// 8 )  if (int(s[0:len(s)-2])*1024*1024 *1024*1024% 8 == 0) else int(s[0:len(s)-2])*1024*1024*1024*1024 / 8
    elif  (s[len(s)-1]== 'B') : 
        tab[i] = int(s[0:len(s)-1])
    elif  (s[len(s)-1]== 'b') : 
        tab[i] =  (int(s[0:len(s)-1])// 8 )  if (int(s[0:len(s)-1])% 8 == 0) else int(s[0:len(s)-1]) / 8
    i += 1
s = ''
# print(' '.join(map(str, tab)))
for i in range(len(tab)) : 
    s+=str(tab[i])+ ' '
print(s[:-1])








