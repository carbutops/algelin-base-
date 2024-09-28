v1=[1,2,3]
x=2
def produtoporumescalar(v1,x):
    vfinal = []
    for c in range(len(v1)):
        vfinal.append(v1[c] * x)
    return vfinal

print(produtoporumescalar(v1,x))