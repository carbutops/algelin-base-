def divvetorescalar(v1,v2):
    produto = []
    if len(v1) == len(v2):
        n = 0
        for c in range(len(v1)):
            produto.append(v1[n] / v2[n])
            n += 1
    return produto