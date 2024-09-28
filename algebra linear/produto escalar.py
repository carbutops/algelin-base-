
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




