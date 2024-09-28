from math import sqrt

def norma(v):
    norma=0
    for c in range(len(v)):
        norma+=(v[c])**2
    norma=sqrt((norma))
    return norma

def pvetorial(v1,v2):
    if len(v1)==len(v2)==3:
        produto=[]
        n1 = 1
        n2 = 2
        for c in range(len(v1)):
            produto.append(v1[n1]*v2[n2]-v1[n2]*v2[n1])
            if n1!=0:
                n1-=1
            else:
                n2-=1
        produto[1]=produto[1]*-1
    else:
        produto.append("da não filho")
    return produto

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

def pmisto(v1,v2,v3):
    vtransitivo=pvetorial(v1,v2)
    produto=pescalar(vtransitivo,v3)
    return produto

def subvet(v1,v2):
    vfinal=[]
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            vfinal.append(v1[n]-v2[n])
            n+=1
    return vfinal

pr=[1,1,1]
pp=[1,2,3]
vr=[2,3,4]
vp1=[2,2,3]
vp2=[0,3,4]

def distanciaretaeplano(pr,vr,pp,vp1,vp2):
    distancia=((pmisto(vp1,vp2,subvet(pp,pr)))/norma(pvetorial(vp1,vp2)))
    if distancia<0:
        distancia=distancia*-1
    return distancia
