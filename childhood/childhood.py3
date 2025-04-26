n = int(input())
t = {}
for i in range(n) :
    inn = input().split()
    t[int(inn[0])] = int(inn[1])
    inn = []
ret = 'NO'
for i in t :
    y = i +t[i]
    
    if (y in t) and (y + t[y]) == i : 
        ret = 'YES'
        break
print(ret)
    
