names = [ "michal" , "nela" , "ola", "przemek" ]
for i in range(len(names)):
    names[i] = names[i].capitalize()
for i in names:
    print(i)
print("____________________\n")


names2 = []
for i in names:
    if 'l' in i:
        names2.append(i)
for i in names2:
    print(i)
print("____________________\n")

names3=[]
for i in names:
    if i[-1]=='a':
        names3.append(i)
for i in names3:
    print(i)
print("____________________\n")

dlugosc=0
for i in names:
    dlugosc = dlugosc + len(i)
print(dlugosc)