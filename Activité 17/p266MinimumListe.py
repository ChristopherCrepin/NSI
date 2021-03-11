def MinimumListe(lst):

    """
        cherche le nombre minimum de la liste
        longueur = Longueur de la liste nommée "lst"
        mini = Valeur de l'élément à la première position de la liste
        tant que i < longueur :
            si le premier i de la liste et lst est inférieur à mini :
                mini prend la valeur de cet valeur
            i augmente d'une valeur pour pouvoir tester toutes les valeurs de la liste
        on renvoie mini qui contient le nombre minimum de la liste
    """
    longueur = len(lst)
    mini = lst[0]
    i = 1
    while (i < longueur) :
        if lst[i] < mini :
            mini = lst[i]
        i = i+1
    return mini

"""
f=open("test.txt","r")
Il affiche "FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'".
Python nous indique ici qu'il ne trouve pas le fichier souhaiter.
"""

try :
    f=open("test.txt","r")
except :
    print("Python ne parvient pas à localiser le fichier")