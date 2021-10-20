clear
clc
close all

!Valeur de K (arbitraire)
K=0.5

!Fonction de transfert (intégrateur ici): H(p)=K/p^2
p=tf('p')
H=K/(p^2)

!Affichage des poles
pole(H)

!Graphe de la réponse indicielle H
figure(1)
step(H)
title('EPIC INDICIEL GRAPH')
xlabel('x MLG 420')
ylabel('y No Scope')

!Graphe de la réponse impulsionellle de H
figure(2)
impulse(H)
title('EPIC IMPULSONELLE GRAPH')
xlabel('x MLG 420')
ylabel('y No Scope')

!Affichage du diagramme de Bode de 
figure(3)
bode(H)