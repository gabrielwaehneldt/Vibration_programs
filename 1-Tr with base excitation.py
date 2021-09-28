#calcula a razão entre força transmitida e força de excitação quando
#se tem todas as informações

import numpy as np

#Dados do sistema
M=80 #massa do eixo
k=224000 #coeficiente da mola
psi=0.5911 #fator de amortecimento
wn=(k/M)**0.5 #frequencia natural
w=628.3 #frequencia de excitação

#Dados da oscilacao da base
Y=(0.2+0j)#amplitude complexa da oscilacao da base

print ("M="+str(M))
print ("wn="+str(wn))



numerador=(1+(w/wn)*psi*2j)
denominador=(1-((w/wn)**2)+2j*(w/wn)*psi)
TR=numerador/denominador #complexo
TR_modulo=abs(TR) #modulo

print ("Valor de TR(X/Y): "+str(TR_modulo))

