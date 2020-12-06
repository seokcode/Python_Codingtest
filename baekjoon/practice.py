
a = list()
for i in range(10):
    a.append(int(input()))
dif = 99

for i in range(10):
    if ( a[i] > 33):
        t = a[i]-33

    else:
        t = 33 - a[i]

    if (t<= dif):
        dif = t
        r = f"dif is {dif}, value if {a[i]}"

print(r)