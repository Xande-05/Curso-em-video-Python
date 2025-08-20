from math import hypot
a= float (input ('Quanto mede o cateto adjacente? '))
o= float (input ('Quanto mede o cateto oposto? '))
h= math.hypot(a,o)
print ('A hipotenusa mede {:.2f}'.format(h))