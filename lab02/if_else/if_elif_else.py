#1
a=1
if a==1:
    print("kbtu")
elif a==2:
    print("a==2")
else:
    print("sdu")
#2
b=10
c=15
if b>c:
    b+=c
elif b==c:
    b*=c
else:
    c+=b

#3
d="maqsat"
if 5==5:
    print(d)
elif 14!=5:
    print("joq")
else:
    print("not equal")

#4
e=121
if e%11==0:
    print("can divide by 11")
elif e%15==0:
    print("15")
else:
    print("can't divide by 11")

#5
f="qwerty"
g="wer"
if g in f:
    print(f[0])
elif f in g:
    print(g[-1])
else:
    print(f[-1])