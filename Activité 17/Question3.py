def TypeParametre(text):
    return str(type(text))
def Presence3ChiffresMin(text):
    lst=['1','2','3','4','5','6','7','8','9']
    nb=0
    for i in lst:
        nb+=1
    if nb>=3:
        return True
    else:
        return False
def PresenceMaj(text):
    nb = 0
    for i in text :
        if (i.upper()==i):
            nb+=1
    if nb>0:
        return True
    else :
        return False
def Presence8CaractMin(text):
    if len(text) >=8:
        return "Oui"
    else :
        return "Non"

import unittest
class TestMdp(unittest.TestCase):
    def test_Presence3ChiffresMin(self):
        try:
            input("Mettez un mdp")
        except:
            print("La fonction pour vérifier les chiffre marche pas")
    def PresenceMaj(text):
        try:
            input("Mettez un mdp")
        except:
            print("La fonction pour vérifier les majuscule marche pas")
    def Presence8CaractMin(self):
        try:
            input("Mettez un mdp")
        except:
            print("La fonction pour vérifier la longueur du mdp marche pas")

if name=='main':
    unittest.main()
