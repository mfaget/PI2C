# labo 2 
#exercice 3
#3.Écrivez un programme qui décomposer une URL 
# en ses trois parties : le protocole,
#  le nom de domaine de la machine et le chemin d’accès de la ressource.
#  Faites deux versions de programme : 
# la première n’utilise que les méthodes de la classe str 
# et la seconde exploite les groupes capturants des expressions régulières.
#  Voici un exemple d’exécution :

#& python3  labo2 -q3.py http ://www.this.is/big/shit
# Protocol: http
# Domain: www.this.is
# Path: big/shit
import re 

pattern = r'^(?P<Protocol>[a-z]+)\:\//(?P<Domain>[a-z]{3}\.[a-z]+\.[a-z]{2})\/(?P<Path>[a-z]+\/[a-z]+)'

p = re.compile(pattern)

m = p.match('http://www.this.is/big/shit')

if m is not None :
    #print("m.groups :",m.groups())
    print("Protocol :",m.group('Protocol'))
    print("Domain :",m.group('Domain'))
    print("Path :",m.group('Path'))
    
    #i=1
    #while m.groups()!=None:
    #    print(" :",m.group(i))
    #    i+=1


