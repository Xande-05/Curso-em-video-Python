from math import radians, sin, cos, tan
a= float (input ('Digite o ângulo que você deseja em °: '))
an= radians(a)
s= sin(an)
c= cos(an)
t= tan(an)
print ('Respectivamente temos: Seno={:.2f}, Cosseno={:.2f} e Tangente={:.2f}'.format(s,c,t))