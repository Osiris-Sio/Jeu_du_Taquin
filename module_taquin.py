# -*- coding: utf-8 -*-

'''
-> Classe Taquin

Auteurs : AMEDRO Louis / CAPPONI DELY Arthur
'''

# Importation Module :
import random

class Taquin():
    
    def __init__(self):
        '''
        Initialise l'objet.
        '''
        self.grille = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    def __repr__(self):
        '''
        Renvoie une chaine qui décrit la classe grille.
        : return (str)
        '''
        return ('Une grille de Taquin')
    
    def __str__(self) :
        '''
        Renvoie une chaine de caractères pour représenter la grille.
        : return (str)
        '''
        separateur = '+----+----+----+----+\n'
        chaine = separateur
        i = 0
        for i in range(16) :
            chaine += '| '
            valeur = self.acc_valeur(i)
            if valeur == 0 :
                chaine += '   '
            elif 1 <= valeur <= 9 :
                chaine = chaine + ' ' + str(valeur) + ' '
            elif 10 <= valeur <= 15 :
                chaine = chaine + str(valeur) + ' '
            if i % 4 == 3 :
                chaine = chaine + '|\n' + separateur
        return chaine

    def acc_valeur(self, indice):
        '''
        Renvoie le contenu de la case d'indice précisé en paramètre.
        : param indice (int), 0 <= indice <= 15
        : return (int)
        
        >>> t = Taquin()
        >>> t.acc_valeur(0)
        1
        >>> t.acc_valeur(10)
        11
        >>> t.acc_valeur(15)
        0
        '''
        return self.grille[indice]
        
    def mut_valeur(self, indice , valeur):
        '''
        Modifie le contenu de la case d'indice précisé en paramètre en y plaçant la valeur précisée en paramètre.
        : params
            indice (int), 0 <= indice <= 15
            valeur (int), 0 <= valeur <= 15
        : Pas de return, self est modifié par effet de bord.
        
        >>> t = Taquin()
        >>> t.mut_valeur(0, 1)
        >>> t.acc_valeur(0)
        1
        >>> t.mut_valeur(6, 12)
        >>> t.acc_valeur(6)
        12
        '''
        self.grille[indice] = valeur

    def acc_indice(self, valeur):
        '''
        Renvoie l'indice de la case de la grille qui contient la valeur précisée en paramètre.
        : param valeur (int), 0 <= valeur <= 15
        : return (int)
        
        >>> t = Taquin()
        >>> t.acc_indice(10)
        9
        >>> t.acc_indice(0)
        15
        '''
        indice = 0
        while self.acc_valeur(indice) != valeur :
            indice += 1
        return indice
        
    def est_vide(self, indice) :
        '''
        Renvoie True si la case d'indice précisé en paramètre est vide et False sinon.
        : param indice (int), 0 <= indice <= 15
        : return (bool)
        
        >>> t = Taquin()
        >>> t.est_vide(15)
        True
        >>> t.est_vide(0)
        False
        '''
        return self.grille[indice] == 0
    
    def est_possible(self, valeur) :
        '''
        Renvoie True si la case contenant la valeur passé en paramètre
        est déplaçable et False sinon.
        : param valeur (int), 0 < valeur <= 15
        : return (bool)

        >>> t = Taquin()
        >>> t.est_possible(12)
        True
        >>> t.est_possible(1)
        False
        '''
        #Précondition :
        assert isinstance(valeur, int) and 0 < valeur <= 15, "Le paramètre doit être un entier et sur l'intervalle ]0;15]." 
        #Code :
        indice_valeur = self.acc_indice(valeur)
        indice_vide = self.acc_indice(0)
        return (indice_valeur == indice_vide - 4) or (indice_valeur == indice_vide + 4) or (indice_valeur == indice_vide - 1 and indice_valeur // 4== indice_vide // 4) or (indice_valeur == indice_vide + 1 and indice_valeur // 4== indice_vide // 4)
            
    def est_gagne(self):
        '''
        Renvoie True si la grille est en position initiale et False sinon.
        : return (bool)
        
        >>> t = Taquin()
        >>> t.est_gagne()
        True
        >>> t.mut_valeur(0, 5)
        >>> t.est_gagne()
        False
        '''
        return self.grille == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    def deplacer(self, valeur) :
        '''
        Deplace, si cela est possible, la case contenant la valeur précisée
        en paramètre (entre 1 et 15) dans la case vide. Si le déplacement n'est pas 
        possible, il ne se passe rien.
        : param valeur (int), 0 < valeur <= 15
        : pas de return mais self est mofifié par effet de bord
        '''
        #Précondition :
        assert isinstance(valeur, int) and 0 < valeur <= 15, "Le paramètre doit être un entier et sur l'intervalle ]0;15]."
        #Code :
        indice_valeur = self.acc_indice(valeur)
        if self.est_possible(valeur) :
            self.mut_valeur(self.acc_indice(0) , valeur)
            self.mut_valeur(indice_valeur , 0)
         
    def valeurs_deplacables(self):
        '''
        Renvoie une liste des valeurs des cases déplaçables.
        : return (list)
        
        >>> t = Taquin()
        >>> t.valeurs_deplacables()
        [12, 15]
        >>> t.deplacer(12)
        >>> t.valeurs_deplacables()
        [8, 11, 12]
        '''
        tab_valeurs_deplacables = []
        for valeur in self.grille :
            if valeur != 0 and self.est_possible(valeur) :
                tab_valeurs_deplacables.append(valeur)
        return tab_valeurs_deplacables
    
    def melanger(self, niveau) :
        '''
        Renvoie le Taquin melangée selon le niveau passé en paramètre (0 <= niveau <= 4).
        : param niveau (int), 0 <= niveau <= 4
        : pas de return mais self est mofifié par effet de bord
        '''
        #Précondition :
        assert isinstance(niveau, int) and 0 <= niveau <= 4, 'Le paramètre doit être un entier (int) positif ou nul compris entre 0 et 4.'
        #Code :
        coup_precedent = None
        dic_niveaux = { 0 : 5,
                        1 : 10,
                        2 : 30,
                        3 : 100,
                        4 : 200
                        }
        for i in range (dic_niveaux[niveau]) :
                valeur_deplacable = random.choice(self.valeurs_deplacables())
                while coup_precedent == valeur_deplacable :
                    valeur_deplacable = random.choice(self.valeurs_deplacables())
                coup_precedent = valeur_deplacable
                self.deplacer(valeur_deplacable)
                         
######################################################
# Doctest :
######################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)