# Variable :
A=[23,12,4,56,35,32,42,57,3]
L=[]
R=[]
p=int()
q=int()
r=int()
n1=int()
n2=int()

# Programme :
def FUSION (A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    def creer_tableau(L,R):
        for i in range(n1):
            L[i] = A[p+i-1]
        return L
        for j in range(n2):
            R[j] = A[q+j]
        return R
    L[n1+1] = float("inf")
    R[n2+1] = float("inf")
    i = 1
    j = 1
    for k in range(p,r):
        if L[i]=<R[j]:
