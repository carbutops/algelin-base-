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

def volumepp(v1,v2,v3):
    volume=pmisto(v1,v2,v3)//1
    return volume

def volumepiramide(v1,v2,v3):
    volume=volumepp/3
    return volume