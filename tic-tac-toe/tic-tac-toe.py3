
import sys
tab = [[2 for i in range(3)] for _ in range(3)]
line =''
bo = 1
s = ''
for line in sys.stdin : 
      s = line.split()
      tab[int(s[0])][int(s[1])] = bo
      bo = abs(1-bo)
if ( tab[int(s[0])][int(s[1])] == tab[int(s[0])][0] and tab[int(s[0])][int(s[1])] == tab[int(s[0])][1] and tab[int(s[0])][int(s[1])] == tab[int(s[0])][2]) or  ( tab[0][int(s[1])] == tab[int(s[0])][int(s[1])] and tab[1][int(s[1])] == tab[int(s[0])][int(s[1])] and tab[2][int(s[1])] == tab[int(s[0])][int(s[1])] ) or   (int(s[0])*int(s[1]) == 1 and ((tab[0][0]==tab[1][1] and tab[1][1]==tab[2][2])or ((tab[0][2]==tab[1][1] and tab[1][1]==tab[2][0])))) or   (( (s[0]=='0' and s[1] == '2')or (s[0]=='2' and s[1] == '0')) and (tab[0][2]==tab[1][1] and tab[1][1]==tab[2][0])) or   (( (s[0]=='0' and s[1] == '0')or (s[0]=='2' and s[1] == '2')) and (tab[0][0]==tab[1][1] and tab[1][1]==tab[2][2])) : 
     print(True)
else : 
      print(False)
