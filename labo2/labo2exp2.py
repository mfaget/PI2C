# labo 2 
#exercice 2
#Écrivez un programme qui ouvre un fichier texte 
# et qui retrouve tous les nombres qui y apparaissent.
# Le programme produit en sortie un inventaire de ces nombres,
#  séparés par des virgules et avec lenuméro de ligne où ils apparaissent.
#  Voici un exemple d’exécution :

#& python3  labo2 -q2.py  monfichier.txt
# Line 3: 829,  -12, 88
# Line  12: 99
# Line  28:  +15
import re

filePath = r"C:\Users\matth\Desktop\ECAM\PI2C\labo2\textexp.txt"
f=open(filePath,'r',encoding="utf-8")
lignes=f.readlines()
print(lignes)

pattern = r'\d+'
p = re.compile(pattern)

result={}
i =1
for e in lignes:
    result[i]=p.findall(e)
    #print(p.findall(e))
    i+=1
for key in result:
    if result[key] != [] :
        print("key : ", key, " : ",result[key])

