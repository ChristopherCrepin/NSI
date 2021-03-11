def TypeParametre(text):
    return str(type(text))

def Presence3ChiffresMin(text):
    lst = ['0','1','2','3','4','5','6','7','8','9']
    nb = 0
    for i in text:
        if i in lst:
            nb = nb +1
    if nb >= 3:
        return True
    else:
        return False

def PresenceMaj(text):
    nb = 0
    for i in text:
        if (i.upper() == i):
            nb = nb +1
    if nb > 0:
        return True
    else:
        return False

def NbCaractSpeciaux(text):
    lst = ['#','@','|','~','§']
    nb = 0
    for i in text:
        if i in lst:
            nb = nb +1
    return nb

def Presence8CaractMin(text):
    if len(text) >= 8:
        return "Oui"
    else:
        return "Non"

