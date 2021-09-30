def tri_bulle(tab):
    #  écrire l'algorithme du tri à bulle comme décrit dans l'énoncé
    # défini la grandeur du tableau
    longueur = len(tab)
    # parcourir la liste en ordre décroissant
    for i in range(longueur,1,-1):
        for j in range (i-1):
            if tab[j+1] < tab[j]:
                memoire = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = memoire

    return tab

if __name__ == '__main__':
    val = [5,8,1,9,6,2,4,3,7,5]
    sorted_val = tri_bulle(val)
    print(val)
