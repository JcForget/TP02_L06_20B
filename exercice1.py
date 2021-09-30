def combine_dic(dic_1, dic_2):
    # Compléter la fonction afin de combiner dic_1 et dic_2
    #     en gardant la valeur max en cas de clef commune
    copie_de_dic2 = dic_2
    réponse = {}

    for clé in dic_1.keys():
        # si la clef est dans les deux dictionnaires
        if clé in dic_2:
            # une liste avec les deux valeurs
            valeur = [dic_1.get(clé),dic_2.get(clé)]
            # ajoute la plus grande valeur et la clé à la réponse
            réponse.update({clé:max(valeur)})
            # supprime le doublon de la deuxième matrice
            copie_de_dic2.pop(clé)
        # si la clef est seulement dans le dictionnaire 1
        else:
            # Ajoute la clef dans la réponse
            réponse.update({clé:dic_1.get(clé)})
    # finalement, ajoute les clefs restantes du deuxième dictionnaire.
    réponse.update(copie_de_dic2)





    return réponse

if __name__ == '__main__':
    # Combinaison de dictionnaire
    dic_1 = {'a': 5, 'b': 2, 'c': 9}
    dic_2 = {'a': 1, 'b': 8, 'd': 17}

    dic_3 = combine_dic(dic_1,dic_2)
    print(dic_3)