import unittest
class TestTicTacToe(unittest.TestCase):
    from Main import afficher_plateau, verifier_victoire, plateau_plein, mouvement_ia

    def test_verifier_victoire_ligne(self):
        plateau = [
            ["X", "X", "X"],
            ["O", " ", "O"],
            [" ", " ", " "]
        ]
        self.assertTrue(verifier_victoire(plateau, "X"))
        self.assertFalse(verifier_victoire(plateau, "O"))

    def test_verifier_victoire_colonne(self):
        plateau = [
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertTrue(verifier_victoire(plateau, "X"))
        self.assertFalse(verifier_victoire(plateau, "O"))

    def test_verifier_victoire_diagonale(self):
        plateau = [
            ["X", "O", " "],
            ["O", "X", " "],
            ["O", " ", "X"]
        ]
        self.assertTrue(verifier_victoire(plateau, "X"))
        self.assertFalse(verifier_victoire(plateau, "O"))

    def test_plateau_plein(self):
        plateau_rempli = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        plateau_non_rempli = [
            ["X", "O", "X"],
            ["O", " ", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(plateau_plein(plateau_rempli))
        self.assertFalse(plateau_plein(plateau_non_rempli))

    def test_mouvement_ia_gagne(self):
        plateau = [
            ["X", "O", " "],
            ["O", "O", " "],
            ["X", " ", " "]
        ]
        ligne, colonne = mouvement_ia(plateau, "O", "X")
        plateau[ligne][colonne] = "O"
        self.assertTrue(verifier_victoire(plateau, "O"))

    def test_mouvement_ia_bloque(self):
        plateau = [
            ["X", "X", " "],
            ["O", "O", " "],
            [" ", " ", " "]
        ]
        ligne, colonne = mouvement_ia(plateau, "O", "X")
        plateau[ligne][colonne] = "O"
        self.assertFalse(verifier_victoire(plateau, "X"))

    def test_mouvement_ia_premier_coup(self):
        plateau = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        ligne, colonne = mouvement_ia(plateau, "O", "X")
        self.assertTrue(0 <= ligne <= 2 and 0 <= colonne <= 2)
        self.assertEqual(plateau[ligne][colonne], " ")

if __name__ == "__main__":
    unittest.main()