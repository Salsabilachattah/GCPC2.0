str = input()
pal=str[0]
for i in range(len(str)):
    for j in range(i+1,len(str)):
        s = str[i:j+1]
        if s == s[::-1] and len(s) > len(pal):
            pal = s
print(pal)