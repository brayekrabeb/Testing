def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 9)
def verifier_victoire(plateau, joueur):
    for i in range(3):
        if all(plateau[i][j] == joueur for j in range(3)):
            return True
        if all(plateau[j][i] == joueur for j in range(3)):
            return True
    if all(plateau[i][i] == joueur for i in range(3)):
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False
def plateau_plein(plateau):
    return all(plateau[i][j] != " " for i in range(3) for j in range(3))
def mouvement_ia(plateau, joueur_ia, joueur_humain):
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = joueur_ia
                if verifier_victoire(plateau, joueur_ia):
                    return i, j
                plateau[i][j] = " "
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = joueur_humain
                if verifier_victoire(plateau, joueur_humain):
                    plateau[i][j] = " "
                    return i, j
                plateau[i][j] = " "
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                return i, j
def jouer_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_humain = "X"
    joueur_ia = "O"
    joueur_actuel = "X"

    print("Bienvenue dans le jeu Tic-Tac-Toe !")
    print("Vous êtes 'X' et l'ordinateur est 'O'.")
    afficher_plateau(plateau)

    while True:
        if joueur_actuel == joueur_humain:
            print(f"Tour du joueur {joueur_humain} :")
            try:
                ligne = int(input("Choisissez une ligne (0, 1, 2) : "))
                colonne = int(input("Choisissez une colonne (0, 1, 2) : "))
            except ValueError:
                print("Veuillez entrer des nombres valides !")
                continue
            if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2 or plateau[ligne][colonne] != " ":
                print("Mouvement invalide ! Essayez à nouveau.")
                continue
            plateau[ligne][colonne] = joueur_humain
        else:
            print("Tour de l'ordinateur :")
            ligne, colonne = mouvement_ia(plateau, joueur_ia, joueur_humain)
            plateau[ligne][colonne] = joueur_ia
        afficher_plateau(plateau)

        if verifier_victoire(plateau, joueur_actuel):
            if joueur_actuel == joueur_humain:
                print("Félicitations ! Vous avez gagné ! 🎉")
            else:
                print("L'ordinateur a gagné ! 😢")
            break


        if plateau_plein(plateau):
            print("Match nul ! Aucun gagnant.")
            break


        joueur_actuel = joueur_ia if joueur_actuel == joueur_humain else joueur_humain

jouer_tic_tac_toe()
