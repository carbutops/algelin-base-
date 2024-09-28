from math import sqrt

def norma(v):
    norma=0
    for c in range(len(v)):
        norma+=(v[c])**2
    norma=sqrt((norma))
    return norma

def pescalar(v1,v2):
    produto=0
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            produto+=v1[n]*v2[n]
            n+=1
    else:
        produto.append('deu tudo errado biridin')
    return produto

def subvet(v1,v2):
    vfinal=[]
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            vfinal.append(v1[n]-v2[n])
            n+=1
    return vfinal

def somavet(v1,v2):
    vfinal=[]
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            vfinal.append(v1[n]+v2[n])
            n+=1
    return vfinal

def produtoporumescalar(v1,x):
    vfinal = []
    for c in range(len(v1)):
        vfinal.append(v1[c] * x)
    return vfinal


p1=[1,2,3]
v1=[0,2,2]
p2=[2,1,3]
v2=[0,2,2]

def distanciaretasparal(p1,v1,p2,v2):
    b=(pescalar(subvet(p1,p2),v1)/pescalar(v2,v1))
    distancia=norma(subvet(p1,somavet(p2,produtoporumescalar(v2,b))))
    return distancia

print(distanciaretasparal(p1,v1,p2,v2))