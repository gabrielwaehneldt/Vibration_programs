import numpy as np

#Calcula w ou c sendo conhecida a amplitude do desbalanceamento

p=7800 #massa especifica
r=0.05 #raio do desbalanceamento
L=0.8 #comprimento do eixo
x=0.0003 #amplitude do deslocamento
volume=3.1416*L*r**2 #volume do eixo
M=p*volume #massa do eixo
k=3*10**6 #coeficiente da mola
c=0 #coeficiente de amortecimento
wn=(k/M)**0.5 #frequencia natural
#w=wn #frequencia de excitação
m=0.01 #massa de desbalanceamento
U=m*r #caracteristicas fisicas do desbalanceamento
results=[]

print ("M="+str(M))
print ("wn="+str(wn))
print ("U="+str(U))

a=np.linspace(0,1000,100000)
for w in a: #mudar a variavel aqui !!!!!
    denominador=((-w**2)*M+1j*w*c+k)
    numerador=w**2*U
    try:
        X=numerador/denominador #complexo
    except:
        pass
    X_modulo=abs(X) #calcula modulo do num complexo
    if ((X_modulo-x)**2)**0.5<x/600.0: #mudar precisão da resposta aqui !!!!!
        results.append([X_modulo,w]) #mudar a variavel aqui !!!!!
print ("Possíveis valores da variavel: "+str(results))

