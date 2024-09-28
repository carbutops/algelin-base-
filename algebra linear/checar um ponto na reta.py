pto=[3,4,5]
ptoreta=[1,2,3]

def divvetorescalar(v1,v2):
    produto = []
    if len(v1) == len(v2):
        n = 0
        for c in range(len(v1)):
            produto.append(v1[n] / v2[n])
            n += 1
    return produto

def subvet(v1,v2):
    vfinal=[]
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            vfinal.append(v1[n]-v2[n])
            n+=1
    return vfinal

def checarpontos(pto,ptoreta,vreta):
    vtrans=subvet(ptoreta,pto)
    checar=[]
    for c in range(len(vtrans)):
        checar=divvetorescalar(vreta,vtrans)
    n=0
    sera=false
    for c in range(len(checar)-1):
        if checar[n]==checar[n+1]:
            sera=true
    return sera

