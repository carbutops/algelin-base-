def subvet(v1,v2):
    vfinal=[]
    if len(v1)==len(v2):
        n=0
        for c in range(len(v1)):
            vfinal.append(v1[n]-v2[n])
            n+=1
    return vfinal

from math import sqrt

def norma(v):
    norma=0
    for c in range(len(v)):
        norma+=(v[c])**2
    norma=sqrt((norma))
    return norma

def eqreta(pto1,pto2):
    vetorctereta=subvet(pto1,pto2)
    ptoinicial=[]
    if norma(pto1)>norma(pto2):
        ptoinicial=pto2
    elif norma(pto1)<norma(pto2):
        ptoinicial=pto1
    else:
        ptoinicial=pto1
    return ptoinicial,vetorctereta
