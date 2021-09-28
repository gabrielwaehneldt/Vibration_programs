import numpy as np

#Calcula (C;psi) quando se tem conhecida a razão entre x dinamico e estático

p=7800 #massa especifica
r=0.05 #raio do desbalanceamento
L=0.8 #comprimento do eixo
xf_xs=1.5 #razão entre x dinamico e estático
volume=3.1416*L*r**2 #volume do eixo
M=3000 #massa do eixo
k=8.225*10**8 #coeficiente da mola
c=0 #coeficiente de amortecimento
cc=(4*k*M)**0.5
wn=(k/M)**0.5 #frequencia natural
w=wn #frequencia de excitação
m=0.01 #massa de desbalanceamento
U=m*r #caracteristicas fisicas do desbalanceamento
psi=0
results=[]

print ("M="+str(M))
print ("wn="+str(wn))
print ("U="+str(U))

a=np.linspace(0,1,10000)
for psi in a: #mudar a variavel aqui
    denominador=((-(w/wn)**2)+2j*(w/wn)*psi+1)
    numerador=1
    Xf_Xs=0
    try:
       Xf_Xs=numerador/denominador #complexo
    except:
        pass
    Xf_Xs_modulo=abs(Xf_Xs) #modulo
    if ((Xf_Xs_modulo-xf_xs)**2)**0.5<xf_xs/5000.0: #mudar criterio aqui
        results.append([Xf_Xs_modulo,psi]) #mudar a variavel aqui
print ("Possíveis valores da variavel: "+str(results))

