# labo 2 
#exercice 1
#Écrivez un programme qui demande à l’utilisateur 
# d’encoder une chaine de caractères et qui vérifie
#  si cette dernière satisfait exactement le motif suivant :
#a) Un numéro de téléphone de la forme +xx xxx xx xx xx où les x sont tous des chiffres
import re
print("Question a :")

patterna = r'\+[0-9]{2}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}\ [0-9]{2}'
pa = re.compile(patterna)
print("Answer a :")
print(pa.match('+32 753 52 48 12'))
print(pa.match('+32 753.52.48.12'))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#(b)Un nombre entier, qui commence éventuellement 
# avec un signe+ou−devant, et sansespaces aucun.
print("Question b")
patternb = r'\+?[0-9]{2}|\-?[0-9]{2}'
pb = re.compile(patternb)

print("Answer b")
print(pb.match('+32'))
print(pb.match('-32'))
print(pb.match('32'))
print(pb.match('+ 32'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#(c)Une plaque d’immatriculation 
# qui peut prendre l’un des deux formes XLLLDDD ou XDDDLLL,
# où L est une lettre et D est un chiffre, et X est un chiffre optionnel (entre1et9).
print("Question c")
patternc = r'[0-9]?[A-Z]{3}[0-9]{3}|[0-9]?[0-9]{3}[A-Z]{3}'
pc = re.compile(patternc)

print("Answer c")
print(pc.match('1ARB123'))
print(pc.match('ARB123'))
print(pc.match('123ARB'))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# (d)Le nom d’un volume sous windows qui est,
#  pour rappel, de la formeC:\(une lettre majusculesuivie de deux-points et backslash).
print("Question d")
patternd = r'^[A-Z]\:\\(?:[a-zA-Z]+)'
pd = re.compile(patternd)

print("Answer d")
print(pd.match('C:\hello'))
print(pd.match('Chello'))
print(pd.match('C:\e'))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



