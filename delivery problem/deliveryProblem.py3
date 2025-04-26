
n = int(input())
t = input().split()
somme = 0 
q = int(input())
tab = [0]*n
for s in range(n) :
    somme +=int(t[s])
    tab[s] = somme
queries = [[]]*q
for i in range(q) :
    queries[i] = input().split()
for i in range(q) : 
    sum = 0 
    ss = queries[i]
    m = int(ss[2])
    print(min(somme + int(ss[0]),tab[m-1] + int(ss[1]) ))

