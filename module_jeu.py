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
        elif not self.taquin.est_gagne() :
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.est_clique_jeu()
        else :
            if pyxel.btnr(pyxel.KEY_R) :
                self.__init__()
     
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
                x_indice = (indice % 4) * 40 + 10
                y_indice = (indice // 4) * 40 + 10
                if (
                    x_indice <= pyxel.mouse_x <= x_indice + 40 and
                    y_indice <= pyxel.mouse_y <= y_indice + 40
                ) and self.taquin.est_possible(valeur):
                    self.nombre_coups += 1
                    self.taquin.deplacer(valeur)

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
        elif not self.taquin.est_gagne() :
            self.afficher_grille()
        else :
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
            
    def afficher_grille(self):
        '''
        Affiche la grille de jeu.
        '''
        for indice in range(16) :
            x_indice = (indice % 4)* 40 + 10
            y_indice = (indice // 4)* 40 + 10
            valeur = self.taquin.acc_valeur(indice)
            
            pyxel.rect(x_indice, y_indice, 40, 40, 15)
            pyxel.rectb(x_indice, y_indice, 40, 40, 9)
            if 1 <= valeur <= 9 :
                pyxel.text(x_indice + 19, y_indice + 17, str(valeur), 0)
            elif 10 <= valeur <= 15 :
                pyxel.text(x_indice + 17, y_indice + 17, str(valeur), 0)
        
    def afficher_gagner(self):
        '''
        affiche l'écran de félicitation quand le taquin est résolu.
        '''
        pyxel.text(50, 75, 'Vous avez reussi en :\n\n       ' + str(self.nombre_coups) + ' coups !', random.randint(1, 15))
        pyxel.text(70, 150, 'Niveau : ' + str(self.niveau), random.randint(1, 15))
        pyxel.text(40, 160, 'Clique sur R pour recommencer', random.randint(1, 15))

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