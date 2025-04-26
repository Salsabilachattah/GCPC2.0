n = int(input())
s = 1
nbr_outside = 5
if n == 0 : 
    s = 0
for i in range( n-1) : 
    s += nbr_outside 
    nbr_outside = nbr_outside + 5
print(s)