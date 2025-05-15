# -*- coding: utf-8 -*-

'''
-> Classe Taquin

Auteurs : AMEDRO Louis / CAPPONI DELY Arthur
'''

# Module à Importer :
import random, module_lineaire

class Taquin():
    
    def __init__(self):
        '''
        Initialise la grille du jeu du Taquin.
        '''
        self.grille = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.pile = module_lineaire.Pile()

    def __repr__(self):
        '''
        Renvoie une chaine qui décrit la classe Taquin.
        : return (str)
        '''
        return ('Une grille de Taquin')
    
    def __str__(self) :
        '''
        Renvoie une chaine de caractères pour représenter la grille.
        : return (str)
        '''
        separateur = '+----+----+----+----+\n' #Ajoute le sép.
        chaine = separateur #La chaine commence par le sép.
        for i in range(16) :
            chaine += '| '
            valeur = self.acc_valeur(i)
            #Conditions de valeur dans la grille :
            if valeur == 0 :
                chaine += '   '
            elif 1 <= valeur <= 9 :
                chaine = chaine + ' ' + str(valeur) + ' '
            elif 10 <= valeur <= 15 :
                chaine = chaine + str(valeur) + ' '
            #Condition de chaque ligne :
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

    def deplacer(self, valeur, qui_joue = True) :
        '''
        Auteur : Amedro Louis
        Deplace, si cela est possible, la case contenant la valeur précisée
        en paramètre (entre 1 et 15) dans la case vide. Si le déplacement n'est pas 
        possible, il ne se passe rien.
        : params 
            valeur (int), 0 < valeur <= 15
            qui_joue (boolean), True si c'est l'utilisateur ou l'attribut melanger, False si c'est l'ordinateur (pour résoudre le taquin)
        : pas de return mais self est mofifié par effet de bord
        '''
        #Précondition :
        assert isinstance(valeur, int) and 0 < valeur <= 15, "valeur doit être un entier et sur l'intervalle ]0;15]."
        assert isinstance(qui_joue, bool), "qui_joue doit être un boolean, True si c'est l'utilisateur ou l'attribut melanger (par défaut), False si c'est l'ordinateur (pour résoudre le taquin)."
        #Code :
        indice_valeur = self.acc_indice(valeur)
        if self.est_possible(valeur) : #Si la valeur peut bouger :
            self.mut_valeur(self.acc_indice(0) , valeur) #Mettre la valeur à la place de la valeur 0 (à l'indice 0)
            self.mut_valeur(indice_valeur , 0) #Mettre le 0 à l'indice de la valeur
            if qui_joue : #Si c'est l'utilisateur/melanger qui joue, alors :   
                self.pile.empiler(valeur) #On mémorise les coups joués.
    
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
    
    def optimiser_pile(self):
        '''
        Auteur : Amedro Louis
        Modifie par effet de bord le contenu de l'attribut pile afin d'éliminer les séries de deux coups identiques consécutifs
        dans la pile avant de le résoudre pour ne pas jouer deux fois de suite le même. Cette méthode n'est appelée qu'une seule fois.
        : pas de return, effet de bord sur pile
        
        >>> taquin = Taquin()
        >>> taquin.pile.empiler(1)
        >>> taquin.pile.empiler(1)
        >>> taquin.pile.empiler(2)
        >>> taquin.pile.empiler(3)
        >>> taquin.pile.empiler(3)
        >>> taquin.pile.empiler(3)
        >>> taquin.pile.empiler(4)
        >>> print(taquin.pile)
        4
        3
        3
        3
        2
        1
        1
        _
        >>> taquin.optimiser_pile()
        >>> print(taquin.pile)
        4
        3
        2
        _
        >>> taquin.pile.empiler(8)
        >>> taquin.pile.empiler(8)
        >>> taquin.pile.empiler(4)
        >>> print(taquin.pile)
        4
        8
        8
        4
        3
        2
        _
        >>> taquin.optimiser_pile()
        >>> print(taquin.pile)
        3
        2
        _
        '''
        stock = module_lineaire.Pile()
        for _ in range(2) : #Double vérification pour ne pas obtenir d'autre doublon(s) après la première optimisation.
            base_doublon = False #Permet de se rappeler si la base de la pile (les deux dernières valeur à dépiler) n'est pas un doublon.
            valeur_precedente = self.pile.depiler() #On dépile le sommet de la pile (valeur_precedente)
            while not self.pile.est_vide() : #Tant que la pile n'est pas vide :
                if not self.pile.est_vide() : #Si la pile n'est pas vide :
                    valeur = self.pile.depiler() #On dépile le sommet de la pile (valeur)
                    if valeur_precedente != valeur : #Si les deux valeurs ne sont pas les mêmes :
                        stock.empiler(valeur_precedente) #On empile valeur_precedente dans la pile stock
                        valeur_precedente = valeur #La valeur_precedente devient la valeur
                    else : #Sinon (si les deux valeurs sont les mêmes)
                        if not self.pile.est_vide() : #Si la pile n'est pas vide :
                            valeur_precedente = self.pile.depiler() #On dépile le sommet de la pile (valeur_precedente)
                        else : #Sinon (si la pile est vide) :
                            base_doublon = True #Se rappeler qu'il ne faut pas mettre la valeur_precedente dans le stock.
                else : #Sinon (si la pile est vide) :
                    stock.empiler(valeur_precedente) #On empile valeur_precedente dans la pile stock
            if not base_doublon : #Si la base de la pile n'est pas un doublon :
                stock.empiler(valeur_precedente) #On empile la valeur_precedente
            while not stock.est_vide() : #Tant que la pile stock n'est pas vide :
                self.pile.empiler(stock.depiler()) #On empile les valeurs dépilées de la pile stock dans la pile (self.pile)

    def resoudre(self) :
        '''
        Auteur : Amedro Louis
        Une méthode qui permet de résoudre la taquin si l'utilisateur le demande au cour de la partie.
        Joue les coups précedent de l'utilisateur puis résoud le taquin grâce à l'attribut pile qui empiler tous les coups depuis le début du jeux (également les coups de la méthode mélanger).
        : pas de return, modifie l'attribut pile  
        '''
        if not self.pile.est_vide() :
            self.deplacer(self.pile.depiler(), False)
              
######################################################
# Doctest :
######################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)