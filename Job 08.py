def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Type ou saison non reconnu")

# Appel de la fonction avec différents paramètres pour tester
afficher_produits("fruits", "hiver")
afficher_produits("fruits", "été")
afficher_produits("légume", "hiver")
afficher_produits("legume", "été")
