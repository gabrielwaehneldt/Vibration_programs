#Calcula X(amplitude do sistema) para desbalanceamento

import numpy as np

#Dados do sistema
M=1520 #massa do eixo
k=2000000#coeficiente da mola
c=412
cc=(4*M*k)**0.5
psi=0.1242 #fator de amortecimento
wn=19.87 #frequencia natural
w=12.57 #frequencia de excitação

#Dados do desbalanceamento
m=0.01
l=0.05
U=m*l

print ("M="+str(M))
print ("wn="+str(wn))



numerador=(1/k)*(500)
denominador=(1-((w/wn)**2)+2j*(w/wn)*psi)
X=numerador/denominador #complexo
X_modulo=abs(X) #modulo

print ("Valor de X: "+str(X_modulo))

