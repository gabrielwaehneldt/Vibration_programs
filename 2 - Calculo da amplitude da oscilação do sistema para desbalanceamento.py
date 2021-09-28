#Calcula X(amplitude do sistema) para desbalanceamento

import numpy as np

#Dados do sistema
M=49 #massa do eixo
k=3*10**6#coeficiente da mola
c=412
cc=(4*M*k)**0.5
psi=c/cc #fator de amortecimento
wn=(k/M)**0.5 #frequencia natural
w=wn #frequencia de excitação

#Dados do desbalanceamento
m=0.01
l=0.05
U=m*l

print ("M="+str(M))
print ("wn="+str(wn))



numerador=(1/k)*U*w**2
denominador=(1-((w/wn)**2)+2j*(w/wn)*psi)
X=numerador/denominador #complexo
X_modulo=abs(X) #modulo

print ("Valor de X: "+str(X_modulo))

