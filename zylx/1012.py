def sum(n):
    el=[((pow(10,i)-1)/9)for i in range(1,n)]
    a=0
    for b in range(0,len(el)):
     a=a+el[b]
    sumn=print(a)
    return a
sum(10)