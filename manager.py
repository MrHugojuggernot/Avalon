import numpy as np
# 0 : ID , 1 : Name
a = np.load("db.npy",None,True)
def add(nom):
    a = np.load("db.npy",None,True)
    ID=len(a)+1
    nom = str(nom)
    ods2 = np.array([[ID,nom]])
    a = np.vstack((a,ods2))
    np.save('db.npy', a)
    return a


def ln():
    a = np.load("db.npy",None,True)
    return len(a)

def delete(n):
    a = np.load("db.npy",None,True)
    a = np.delete(a,n,0)
    np.save('db.npy',a)
    return a

def show(n):
    a = np.load("db.npy",None,True)
    return a[n]
    
def zashow():
    a = np.load("db.npy",None,True)
    return a

def search(arg):
    a = np.load("db.npy",None,True)
    L=[]
    for i in range(len(a)):
        z=a[i][1].split()
        if arg in z and not(a[i][1] in L):
            L.append(a[i][1])
        if arg in a[i][1] and not(a[i][1] in L):
            L.append(a[i][1])
    return L

def zasearch(arg):
    a = np.load("db.npy",None,True)
    L=[]
    for i in range(len(a)):
        z=a[i][1].split()
        if arg in z and not(a[i][1] in L) and not(a[i][0] in L):
            L.append(a[i][0])
            L.append(a[i][1])
        if arg in a[i][1] and not(a[i][1] in L) and not(a[i][0] in L):
            L.append(a[i][0])
            L.append(a[i][1])
    LL=[]
    Lsama=[]
    for i in range(len(L)//2):
        LL.append(L.pop(0))
        LL.append(L.pop(0))
        Lsama.append(LL)
        LL=[]
    return Lsama
