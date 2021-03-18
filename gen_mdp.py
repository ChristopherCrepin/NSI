# Importation des bibliothèques
from random import choice, randint

# Mise en place des variables
NbrCarac=int(input("Quel est le nombre de caract max"))

'''
min_user = input('True or False :').lower().strip()
if min_user == 'true':
    boolValue = True
    print("ok")
elif min_user == "false" :
    boolValue = False
    print("don't ok")
else :
    print('error')

maj_user = input('True or False :').lower().strip()
if maj_user == 'true':
    boolValue = True
elif maj_user == "false" :
    boolValue = False
else :
    print('error')

chif_user = input('True or False :').lower().strip()
if chif_user == 'true':
    boolValue = True
elif chif_user == "false" :
    boolValue1 = False
else :
    print('error')

cs_user = input('True or False :').lower().strip()
if cs_user == 'true':
    boolValue = True
elif cs_user == "false" :
    boolValue = False
else :
    print('error')
'''

alphabet_min = [ chr(i) for i in range(97,123) ]
alphabet_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

# Initialisation du mdp avec règles
def pwd(n , min = True, maj = False, chif = False, cs = False):
    alphabets = dict()
    key = 0

    if min:
        alphabets[key] = alphabet_min
        key += 1
    if maj:
        alphabets[key] = alphabet_maj
        key += 1
    if chif:
        alphabets[key] = chiffres
        key += 1
    if cs:
        alphabets[key] = caracteres_speciaux
        key += 1

    mdp = ''
    for i in range(n):
            s = randint(0,key-1)
            mdp += choice( alphabets[s] )
    return(mdp)

print(pwd(NbrCarac))
