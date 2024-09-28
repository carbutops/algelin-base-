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

def encontrarcos(v1,v2):
    v1n=norma(v1)
    v2n=norma(v2)
    cos=(pescalar(v1,v2)/(v1n*v2n))
    return cos
x=[1.398,1.398]
y=[-0.683,0.683]
print(encontrarcos(x,y))