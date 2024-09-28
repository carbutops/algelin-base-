
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

