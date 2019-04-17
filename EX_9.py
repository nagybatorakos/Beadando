import sys
import numpy as np

def matrixszorzas(m1,m2,mx):
    k=0
    while k<m1.shape[0]:
        p=0
        while p<m2.shape[1]:
            szor=0
            for i in range(m1.shape[1]):
                szor+=(m1[k][i])*(m2[i][p])
            mx[k][p]=szor
            p+=1
        k+=1
    return mx

try:
    n1=int(sys.argv[1])
    n2=int(sys.argv[2])
    n3=int(sys.argv[3])
    n4=int(sys.argv[4])
    if n2==n3:
        m1=np.random.randint(0,10,(n1,n2))
        m2=np.random.randint(0,10,(n3,n4))
        mx=np.zeros((n1,n4))

        print(matrixszorzas(m1,m2,mx))
    else:
        print("A két mátrix nem összeszorozható")
except ValueError:
    print("Hibás paraméterek")
