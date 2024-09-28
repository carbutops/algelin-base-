from sympy import *

x,y,z,t = symbols('x y z t')

def abs(numero):
    if numero>=0:
        return numero
    else:
        return (-numero)

class ponto():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
def distancia_dois_pontos(ponto1,ponto2):
    distancia=((ponto1.x-ponto2.x)**2+(ponto1.y-ponto2.y)**2+(ponto1.z-ponto2.z)**2)**(1/2)
    return distancia
class vetor(ponto):
    def __init__(self ,x=0.0, y=0.0, z=0.0,nome='vetor'):
        self.nome = nome
        self.coordenadas = ponto(x, y, z)

    def __add__(v1, v2):
        if type(v1) == vetor and type(v2) == vetor:
            vsoma = vetor(x=(v1.coordenadas.x + v2.coordenadas.x), y=(v1.coordenadas.y + v2.coordenadas.y), z=(v1.coordenadas.z + v2.coordenadas.z))
        else:
            vsoma = (' Impossível fazer tal operação com tais dados.')
        return (vsoma)

    def __sub__(v1, v2):
        if type(v1) == vetor and type(v2) == vetor:
            vsub = vetor(x=v1.coordenadas.x - v2.coordenadas.x, y=v1.coordenadas.y - v2.coordenadas.y, z=v1.coordenadas.z - v2.coordenadas.z)  # subtracao de vetores
        else:
            vsub = (' Impossível fazer tal operação com tais dados.')
        return (vsub)

    def __rmul__(v1,cte):#produto por um escalar
        if type(v1)==vetor and type(cte)!=vetor:
          pv=vetor(x=v1.coordenadas.x*cte, y=v1.coordenadas.y*cte, z= v1.coordenadas.z*cte) # produto de constante a direita vezes vetor
        elif type(cte)==vector and type(v1)!= vector:
          pv=vector(x=v1*cte.coordenadas.x, y=v1*cte.coordenadas.y, z= v1*cte.coordenadas.z)
        return pv

    def __mul__(v1,v2):#produto escalar
        vescalar=(v1.coordenadas.x*v2.coordenadas.x+v1.coordenadas.y*v2.coordenadas.y+v1.coordenadas.z*v2.coordenadas.z) # subtracao de vetores
        return(vescalar)


    def __pow__(v1,v2):  # produto vetorial
        if type(v1)==vetor and type(v2)==vetor:
          vpv=vetor(v1.coordenadas.y*v2.coordenadas.z-v2.coordenadas.y*v1.coordenadas.z, -(v1.coordenadas.x*v2.coordenadas.z-v2.coordenadas.x*v1.coordenadas.z), (v1.coordenadas.x*v2.coordenadas.y-v2.coordenadas.x*v1.coordenadas.y))
        else:
          vpv=(' Impossível fazer tal operação com tais dados.')
        return(vpv)

    def __str__(self):
        return('( x = ' + str(self.coordenadas.x) + ', y = ' + str(self.coordenadas.y) + ', z = '+str(self.coordenadas.z) + ' )')

    def pmisto(v1,v2,v3):
        produto=(v1*v2)**v3
        return produto

    def norma(v1):
        norma=((v1.coordenadas.x)**2+(v1.coordenadas.y)**2+(v1.coordenadas.z)**2)**(1/2)
        return norma

    def projecao_ortogonal(v1, v2):
        proj=((v1*v2)/norma(v2))*v2
        return proj

    def diff(self,d):
        return vetor(diff(self.coordenadas.x,d),diff(self.coordenadas.y,d),diff(self.coordenadas.z,d))

    def integrate(self,d):
        return vetor(integrate(self.coordenadas.x,d),integrate(self.coordenadas.y,d),integrate(self.coordenadas.z,d))

    def subs(self,s,a):
        return vetor(subs(self.coordenadas.x,s,a),subs(self.coordenadas.y,s,a),subs(self.coordenadas.z,s,a))

def encontrarcos(v1, v2):
    v1n = norma(v1)
    v2n = norma(v2)
    cos = (v1*v2) / (v1n * v2n)
    return cos

def volumeparalelepipedo(v1, v2, v3):
    volume = pmisto(v1, v2, v3) // 1
    return volume

def volumepiramide(v1, v2, v3):
    volume = volumeparalelepipedo(v1, v2, v3) / 3
    return volume
def vetor_com_dois_pontos(pto1,pto2):
    vetorf=vetor(pto1.x-pto2.x, pto1.y-pto2.y, pto1.z-pto2.z)
    return vetorf
class reta(vetor):
    def __init__(self,nome='reta' ,x=0.0, y=0.0, z=0.0,vetor_reta=vetor(0,0,0)):
        self.nome = nome
        self.coordenadas_iniciais = ponto(x, y, z)
        self.vetor_reta=vetor_reta

def checar_ponto_na_reta(reta, ponto):
    vtrans = vetor(reta.x-pto.x,reta.y-pto.y,reta.z-pto.z)
    x=reta.vetor_reta.x/vtrans.x
    y=reta.vetor_reta.y/vtrans.y
    z=reta.vetor_reta.z/vtrans.z
    if x==y and y==z:
        sera=True
    else:
        sera=False
    return sera

def distancia_das_retas(reta1,reta2):
    def checar_reta_paralela(reta1,reta2):
        sera = false
        if norma(reta1.vetor_reta**reta2.vetor_reta) == 0:
            sera = true
        return sera
    def distancia_retas_paral(reta1,reta2):
        b = ((vetor_com_dois_pontos(reta1.coordenadas_iniciais,reta2.coordenadas_iniciais)*reta1.vetor_reta) / reta2.vetor_reta*reta1.vetor_reta)
        distancia=norma((vetor(reta1.coordenadas_iniciais))-vetor(reta2.coordenadas_iniciais)+(reta2.vetor_reta*b))
        return distancia

    def distancia_reta_nao_paral(reta1,reta2):
        distancia = pmisto(reta1.vetor_reta, reta2.vetor_reta, vetor_com_dois_pontos(reta1.coordenadas_iniciais,reta2.coordenadas_iniciais)) / norma(reta1.vetor_reta**reta2.vetor_reta)
        return distancia

    if checar_reta_paralela(reta1,reta2)==True:
        resposta=distancia_retas_paral(reta1, reta2)

    else:
        resposta=distancia_reta_nao_paral(reta1,reta2)

    return resposta

class plano(vetor):
    def __init__(self,nome='reta' ,x=0.0, y=0.0, z=0.0,vetor_diretor1=vetor(0,0,0),vetor_diretor2=vetor(0,0,0)):
        self.nome = nome
        self.coordenadas_iniciais = ponto(x, y, z)
        self.vetor_diretor1=vetor_diretor1
        self.vetor_diretor2=vetor_diretor2
        self.vetor_normal=vetor_diretor1**vetor_diretor2