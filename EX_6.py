def darab(n):
    ls=['0','4','7']
    db=0
    for i in range(n):
        tmp=str(i)
        k=0
        for j in range(len(tmp)):
            if tmp[j] in ls:
                k+=1
        if k==len(tmp):
            db+=1
    return db

n=700
print(darab(n))
