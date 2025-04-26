str = input()
str1 = ''
str2 = ''
str3 = ''
str4 = ''
str5 = ''
str6 = ''
str7 = ''
str8 = ''

for i in range(len(str)) : 
    if str[i] in 'AEIOUY' :
          str1 += str[i]
    elif str[i] in 'dhlptx': 
          str2 += str[i]
    elif str[i] in 'BCFGJKMNQRSVWZ': 
          str3 += str[i]
    elif str[i] in 'DHLPTX': 
          str4 += str[i]
    elif str[i] in '0123456789': 
          str5 += str[i]
    elif str[i] in '!@#$%^&*()_+/][{}":;`<>?' or str[i]==ord("'")or str[i]==ord('\\'): 
          str6 += str[i]
    elif str[i] in 'aeiouy': 
          str7 += str[i]
    elif str[i] in 'bcfgjkmnqrsvwz': 
          str8 += str[i]


print(str1+str2+str3+str4+str5+str6+str7+str8)
