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
roots_range=[]
print ("M="+str(M))
print ("wn="+str(wn))
print ("U="+str(U))
x_1=0
x_2=0

rang0=-100000 
rang1=100000 #procura raizes no intervalo entre rang1 e rang2
pre=100000 #precisão em que procura pelas raizes


a=np.linspace(rang0,rang1,pre)
for w in a: #mudar a variavel aqui !!!!!!!!!!!!!!!!!
    denominador=((-w**2)*M+1j*w*c+k)
    numerador=w**2*U
    try:
        X=numerador/denominador #complexo
    except:
        pass
    X_modulo=abs(X) #calcula modulo do num complexo
    x_2=x_1
    x_1=X_modulo
    var=w #mudar a variavel aqui !!!!!!!!!!!!!!!!
    if x_1<x:
        if x_2>x:
            roots_range.append([var-((rang1-rang0)/pre),var]) 
    if x_1>x:
        if x_2<x:
            roots_range.append([var-((rang1-rang0)/pre),var]) 

for i in range(len(roots_range)):
    b=np.linspace(roots_range[i][0],roots_range[i][1],1000)
    X_modulo_melhor=1
    var_melhor=0
    for w in b: #mudar a variavel aqui !!!!!!!!!!!!!!!
        #print (w)
        denominador=((-w**2)*M+1j*w*c+k)
        numerador=w**2*U
        X=numerador/denominador #complexo
        X_modulo=abs(X) #calcula modulo do num complexo
        if ((X_modulo-x)**2)**0.5<((X_modulo_melhor-x)**2)**0.5:
            X_modulo_melhor=X_modulo
            var_melhor=w # mudar variavel aqui !!!!!!!!!!!!
    results.append([X_modulo_melhor,var_melhor])
print ("Possíveis valores da variavel: "+str(results))

