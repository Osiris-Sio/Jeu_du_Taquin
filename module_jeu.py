# -*- coding: utf-8 -*-
'''
Module pour la classe Jeu

Auteur : AMEDRO Louis
'''
######################################################
### Importation Modules :
######################################################

import pyxel, random, module_taquin, module_jeu

######################################################
### Classe Jeu :
######################################################

class Jeu() :
    
    def __init__(self) :
        '''
        Initialise le jeu du Taquin.
        '''
        self.taquin = module_taquin.Taquin()
        self.niveau = None
        self.menu = True
        self.nombre_coups = 0
        self.question_resoudre = False
        self.resoudre = False
        
    ######################################################
    ### Fonction Calculs :
    ######################################################

    def calculer(self) :
        '''
        Ici on effectue tous les calculs nécessaires au jeu.
        '''
        #Menu :
        if self.menu :
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                self.est_clique_menu()
                if self.niveau != None :
                    self.taquin.melanger(self.niveau)
                    self.menu = False
        #Jeu :
        else :
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                if not self.taquin.est_gagne() and not self.question_resoudre and not self.resoudre: #Sans fenêtres d'ouvertes.
                    self.est_clique_jeu()
                    self.est_clique_resoudre()
                elif not self.taquin.est_gagne() and self.question_resoudre and not self.resoudre: #Pour la fenêtre de la question (pour résoudre ?).
                    self.est_clique_question()
                elif not self.taquin.est_gagne() and not self.question_resoudre and self.resoudre: #Si l'utilisateur a abandonné (ne peut rien modifier, juste continuer).
                    self.est_clique_continuer()
                elif self.taquin.est_gagne(): #Si le jeu est gagné, bouton retour au menu.
                    self.est_clique_fin()  

    def est_clique_menu(self):
        '''
        Si une case de niveau est cliqué dans le menu, alors change le niveau du jeu.
        : return (int)
        '''
        for indice in range(5) :
            x_indice = indice * 20 + 40
            y_indice = 145
            if (
                x_indice <= pyxel.mouse_x <= x_indice + 20 and
                y_indice <= pyxel.mouse_y <= y_indice + 20
            ):
                self.niveau = indice
                
    def est_clique_jeu(self):
        '''
        Si une case déplaçable est touché, alors on la déplace.
        '''
        for indice in range(16) :
            valeur = self.taquin.acc_valeur(indice)
            if valeur != 0 : 
                x_indice = (indice % 4) * 35 + 20
                y_indice = (indice // 4) * 35 + 15
                if (
                    x_indice <= pyxel.mouse_x <= x_indice + 35 and
                    y_indice <= pyxel.mouse_y <= y_indice + 35
                ) and self.taquin.est_possible(valeur):
                    self.nombre_coups += 1
                    self.taquin.deplacer(valeur)
                    
    def est_clique_resoudre(self):
        '''
        Si la bouton résoudre est touché, lance la procédure pour demander à l'utilisateur s'il est toujours d'accord.
        '''
        if (
            70 <= pyxel.mouse_x <= 70 + 39 and
            160 <= pyxel.mouse_y <= 160 + 15
        ):
            self.question_resoudre = True
            
    def est_clique_question(self):
        '''
        Si le bouton oui/non est touché, lance la procédure résoudre le taquin.
        '''
        #Bouton Oui :
        if (
            40 <= pyxel.mouse_x <= 40 + 25 and
            100 <= pyxel.mouse_y <= 100 + 15
        ):
            self.resoudre = True
            self.question_resoudre = False
            self.taquin.optimiser_pile()
        #Bonton Non :
        elif (
            110 <= pyxel.mouse_x <= 110 + 25 and
            100 <= pyxel.mouse_y <= 100 + 15
        ):
            self.question_resoudre = False
            
    def est_clique_continuer(self):
        '''
        Si le bouton continuer est touché, déplace une case de la grille pour le résoudre.
        '''
        if (
            70 <= pyxel.mouse_x <= 70 + 39 and
            160 <= pyxel.mouse_y <= 160 + 15
        ):
            self.taquin.resoudre()
            
    def est_clique_fin(self) :
        '''
        Si le bouton menu est touché (quand le jeu est fini), retour au menu. 
        '''
        if (
            70 <= pyxel.mouse_x <= 70 + 39 and
            160 <= pyxel.mouse_y <= 160 + 15
        ):
            self.__init__()
        
    ######################################################
    ### Fonctions Affichage :
    ######################################################

    def afficher(self):
        '''
        Ici on dessine tous les objets du jeu.
        '''
        pyxel.cls(0)
        #Menu :
        if self.menu :
            self.afficher_menu()
        #Jeu
        else :
            self.afficher_jeu()
            if self.question_resoudre :
                self.afficher_question()
            elif self.taquin.est_gagne() and not self.resoudre:
                self.afficher_gagner()
            
    def afficher_menu(self):
        '''
        Affiche le menu du jeu.
        '''
        pyxel.text(70, 60, 'Jeu du\n\n  Taquin !', random.randint(1, 15))
        pyxel.text(16, 120, '- Clique sur un niveau de difficulte -', random.randint(1, 15))
        
        for indice in range(5) :
            x_indice = indice* 20 + 40
            y_indice = 145
        
            pyxel.rect(x_indice, y_indice, 20, 20, 15)
            pyxel.rectb(x_indice, y_indice, 20, 20, 9)
            pyxel.text(x_indice + 9, y_indice + 7, str(indice), 0)
            
    def afficher_jeu(self):
        '''
        Affiche le jeu (la grille et le bouton résoudre).
        '''
        # Grille du Taquin :
        for indice in range(16) :
            x_indice = (indice % 4)* 35 + 20
            y_indice = (indice // 4)* 35 + 15
            valeur = self.taquin.acc_valeur(indice)
        
            pyxel.rect(x_indice, y_indice, 35, 35, 15)
            pyxel.rectb(x_indice, y_indice, 35, 35, 9)
            if 1 <= valeur <= 9 :
                pyxel.text(x_indice + 17, y_indice + 15, str(valeur), 0)
            elif 10 <= valeur <= 15 :
                pyxel.text(x_indice + 15, y_indice + 15, str(valeur), 0)
                
        # Bouton Résoudre/Continuer/Résolu :
        if not self.resoudre and not self.taquin.est_gagne() :
            pyxel.rect(70, 160, 39, 15, 8)
            pyxel.rectb(70, 160, 39, 15, 7)
            pyxel.text(74, 165, 'Resoudre', 7)
        elif self.resoudre and not self.taquin.est_gagne():
            pyxel.rect(70, 160, 39, 15, 11)
            pyxel.rectb(70, 160, 39, 15, 7)
            pyxel.text(72, 165, 'Continuer', 7)
        else :
            pyxel.rect(70, 160, 39, 15, 6)
            pyxel.rectb(70, 160, 39, 15, 7)
            pyxel.text(74, 165, 'Resolu !', 7)
        
    def afficher_question(self):
        '''
        Affiche la fenêtre pour savoir si l'utilisateur est toujours d'accord pour que le taquin soit résolu.
        '''
        pyxel.rect(0, 0, 180, 180, 0)
        pyxel.text(23, 75, 'Veux-tu que le taquin soit resolu ?', 7)
        # Bouton Oui :
        pyxel.rect(40, 100, 25, 15, 11)
        pyxel.rectb(40, 100, 25, 15, 7)
        pyxel.text(47, 105, 'Oui', 7)
        # Bouton Non :
        pyxel.rect(110, 100, 25, 15, 8)
        pyxel.rectb(110, 100, 25, 15, 7)
        pyxel.text(117, 105, 'Non', 7)
        
    def afficher_gagner(self):
        '''
        Affiche l'écran de félicitation quand le taquin est résolu.
        '''
        pyxel.rect(0, 0, 180, 180, 0)
        pyxel.text(50, 75, 'Vous avez reussi en :\n\n       ' + str(self.nombre_coups) + ' coups !', random.randint(1, 15))
        pyxel.text(70, 130, 'Niveau : ' + str(self.niveau), random.randint(1, 15))
        # Bouton Menu :
        pyxel.rect(70, 160, 39, 15, 6)
        pyxel.rectb(70, 160, 39, 15, 7)
        pyxel.text(82, 165, 'Menu', 7)

    ######################################################
    ### Initialisation du Jeu et de la fenêtre :
    ######################################################
        
    def jouer(self):
        '''
        Initialise la fenêtre et lance le jeu avec un taux de 30 rafraîchissements/calculs par seconde.
        '''
        pyxel.init(180, 180, 'Jeu du Taquin !')
        pyxel.mouse(True)
        pyxel.run(self.calculer, self.afficher)