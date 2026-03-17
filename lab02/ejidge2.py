l = (1,2,7,-2,3,0)
m1=l[0]
m2=l[0]
ln=len(l)
for i in range(ln):
    if m1<l[i]:
        m1=l[i]
for i in range(ln):
    if l[i]==m1:
        continue
    elif m2<l[i]:
        m2=l[i]
print(m1)
print(m2)