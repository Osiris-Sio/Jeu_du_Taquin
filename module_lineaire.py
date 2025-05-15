# -*- coding: utf-8 -*-

'''
-> Module de Structures Linéaires

Auteur : AMEDRO Louis
'''

class Maillon :
    '''
    Une classe pour un maillon.
    '''
    
    def __init__(self, valeur = None, suivant = None):
        '''
        Initialise un maillon avec les attributs :
            -> valeur (type inconnu), la valeur du maillon
            -> suivant (Maillon), pointe vers son Maillon suivant (None si le Maillon suivant est vide).
        : params
            valeur (type inconnu)
            suivant (Maillon)
        '''
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        '''
        Donne la classe de l'objet et sa valeur.
        '''
        return 'Maillon de valeur : ' + str(self.valeur)
    
    def acc_valeur(self):
        '''
        Accesseur de l'attribut valeur.
        : return (type inconnu), valeur
        '''
        return self.valeur
    
    def acc_suivant(self):
        '''
        Accesseur de l'attribut suivant.
        : return (Maillon)
        '''
        return self.suivant
    
    def mut_valeur(self, nouvelle_valeur):
        '''
        Modifie l'attribut valeur.
        : param nouvelle_valeur (type inconnu)
        '''
        self.valeur = nouvelle_valeur
        
    def mut_suivant(self, maillon):
        '''
        Modifie l'attribut suivant.
        : param maillon (Maillon)
        '''
        self.suivant = maillon
        
    def est_vide(self) :
        '''
        Renvoie True si le maillon est vide, False sinon
        '''
        return self.valeur == None #Renvoie la réponse de la condition (True/False)
    
    
    
    
class ListeChainee() :
    '''
    Une classe pour implémenter une liste chainée.
    '''
    def __init__(self):
        '''
        Initialise une liste chainée vide avec comme attributs :
            -> tete (Maillon), le Maillon en tête de la liste (par défaut, la liste est vide).
            -> longueur (int), la longueur de la liste chainée.
        '''
        self.tete = None
        self.longueur = 0
    
    def __repr__(self):
        '''
        Donne la classe de l'objet et sa longueur.
        : return (str)
        '''
        return 'Class Liste_chainées de longueur ' + str(self.longueur)
    
    def __str__(self):
        '''
        Renvoie une chaine pour visualiser la liste.
        : return (str)
        
        >>> l = ListeChainee()
        >>> print(l)
        ()
        >>> l.ajouter(1)
        >>> print(l)
        (1, ())
        >>> l.ajouter(2)
        >>> print(l)
        (2, (1, ()))
        '''
        chaine = '(' #La chaine commence par ce caractère.
        maillon = self.tete #Le premier maillon c'est le maillon en tête de la liste chainée.
        while maillon != None : #Si le maillon n'est pas vide :
            chaine = chaine + str(maillon.acc_valeur()) + ', (' #Ajoute à la chaine la valeur du maillon et des caractères supplémentaire.
            maillon = maillon.acc_suivant() #Le maillon devient le suivant du maillon.
        chaine = chaine + ')' + (')' * (self.longueur)) #Quand tous les valeurs ont été ajoutées, on ferme toutes les parenthèses ouvertes.
        return chaine 
            
    def ajouter(self, valeur):
        '''
        Ajoute un maillon de valeur précisé en tête de liste.
        : param valeur (type inconnu)
        : pas de return
        
        >>> l = ListeChainee()
        >>> l.ajouter(2)
        >>> l.tete.acc_valeur()
        2
        >>> l.ajouter(3)
        >>> l.tete.acc_valeur()
        3
        >>> l.tete.acc_suivant().acc_valeur()
        2
        >>> l.longueur
        2
        '''
        nouveau_maillon = Maillon(valeur, self.tete) #Créer un maillon.
        self.tete = nouveau_maillon #Le nouveau maillon devient la tête de la liste chainée.
        self.longueur += 1 #La longueur de la liste chainée augmente de 1.

    def est_vide(self):
        '''
        Renvoie True si la liste est vide et False sinon.
        : return (boolean)
        
        >>> l = ListeChainee()
        >>> l.est_vide()
        True
        >>> l.ajouter(1)
        >>> l.est_vide()
        False
        '''
        return self.longueur == 0
    
    def __len__(self):
        '''
        Accesseur de l'attribut longueur.
        : return (int)
        
        >>> l = ListeChainee()
        >>> l.ajouter(2)
        >>> l.ajouter(5)
        >>> len(l)
        2
        '''
        return self.longueur
    
    def retirer(self):
        '''
        Enlève si possible la tête de la liste chainée.
        : pas de return, modifie l'attribut tete et longueur.
        
        >>> l = ListeChainee()
        >>> l.ajouter(1)
        >>> len(l)
        1
        >>> l.retirer()
        >>> len(l)
        0
        '''
        self.tete = self.tete.acc_suivant() #On prend le maillon suivant du maillon de tête pour le mettre en tête de la liste chainée.
        self.longueur -= 1 #Diminu la longueur de la liste chainée.
        
    def acceder(self, n):
        '''
        Renvoie le maillon d'indice n s'il existe.
        : param n (int), 0 <= n <= longueur
        : return (Maillon)
        
        >>> l = ListeChainee()
        >>> l.ajouter(4)
        >>> l.ajouter(3)
        >>> l.ajouter(2)
        >>> l.ajouter(1)
        >>> l.acceder(0).acc_valeur()
        1
        >>> l.acceder(2).acc_valeur()
        3
        '''
        #Précondition :
        assert isinstance(n, int) and 0 <= n <= self.longueur, 'n doit être un entier (int) entre 0 compris et la longueur de la liste compris !'
        #Code :
        maillon = self.tete #Le premier maillon est le maillon en tête de la liste chainée.
        for i in range (n) : #Pour chaque indice jusqu'à n :
            maillon = maillon.acc_suivant() #Change le maillon en son maillon suivant.
        return maillon #Renvoie le maillon d'indice n.
        
    def inserer(self, n, valeur):
        '''
        Insère la valeur à l'indice n de la liste chainée.
        : params
            n (int), 0 <= n <= longueur
            valeur (type inconnu)
        : pas de return, on modifie les maillons de la liste chainée.
            
        >>> l = ListeChainee()
        >>> l.ajouter(3)
        >>> l.ajouter(2)
        >>> l.ajouter(1)
        >>> l.inserer(1, 1.5)
        >>> print(l)
        (1, (1.5, (2, (3, ()))))
        '''
        #Précondition :
        assert isinstance(n, int) and 0 <= n <= self.longueur, 'n doit être un entier (int) entre 0 compris et la longueur de la liste compris !'
        #Code :
        if n == 0 : #Si n est 0 :
            self.ajouter(valeur) #On ajoute simplement la valeur avec la méthode ajouter de la classe.
        else : #Sinon :
            maillon_precedent = self.acceder(n - 1) #Le maillon précèdent c'est le maillon d'indice n - 1.
            nv_maillon = Maillon(valeur, maillon_precedent.acc_suivant()) #Définie le nouveau maillon avec sa valeur avec comme maillon suivant le suivant du maillon précèdent qui sera ajouté dans la liste chainée.
            maillon_precedent.mut_suivant(nv_maillon) #Change le suivant du maillon précèdent par le nouveau maillon.
            self.longueur += 1 #Augmente la longueur de la liste chainée.
            
    def supprimer(self, n):
        '''
        Enlève le maillon d'indice n passé en paramètre en modifiant l'attribut
        suivant du maillon qui le prècéde dans la liste chainée pour le relier directement au maillon qui le suit.
        : param n (int), 0 <= n <= longueur
        : pas de return, on modifie les maillons de la liste chainée.
        
        >>> l = ListeChainee()
        >>> l.ajouter(3)
        >>> l.ajouter(2)
        >>> l.ajouter(1)
        >>> l.supprimer(1)
        >>> print(l)
        (1, (3, ()))
        '''
        #Précondition :
        assert isinstance(n, int) and 0 <= n <= self.longueur, 'n doit être un entier (int) entre 0 compris et la longueur de la liste compris !'
        #Code :
        if n == 0 : #Si n est 0 :
            self.retirer() #On retire simplement le maillon de tête avec la méthode retirer de la classe.
        else : #Sinon :
            maillon_precedent = self.acceder(n - 1) #Le maillon précèdent c'est le maillon d'indice n - 1.
            maillon_precedent.mut_suivant(maillon_precedent.acc_suivant().acc_suivant()) #Le suivant du maillon précèdent devient le suivant du maillon suivant.
            self.longueur -= 1 #Diminu la longueur de la liste chainée.
            
    def __getitem__(self, n):
        '''
        Renvoie la valeur du maillon d'indice n passé en paramètre.
        : param n (int), 0 <= n <= longueur
        : return (type inconnu), la valeur du maillon d'indice n.
        
        >>> l = ListeChainee()
        >>> l.ajouter(4)
        >>> l.ajouter(3)
        >>> l.ajouter(2)
        >>> l.ajouter(1)
        >>> l[0]
        1
        >>> l[1]
        2
        >>> l[3] 
        4
        '''   
        #Précondition :
        assert isinstance(n, int) and 0 <= n <= self.longueur, 'n doit être un entier (int) entre 0 compris et la longueur de la liste compris !'
        #Code :
        return self.acceder(n).acc_valeur() #Renvoie la valeur maillon d'indice n.
    
    def __setitem__(self, n, valeur):
        '''
        Modifie la valeur du maillon d'indice n passé en paramètre.
        : params
            n (int), 0 <= n <= longueur
            valeur (type inconnu), la nouvelle valeur du maillon d'indice n.
        : pas de return, modifie la valeur du maillon d'indice n.
        
        >>> l = ListeChainee()
        >>> l.ajouter(4)
        >>> l.ajouter(3)
        >>> l.ajouter(2)
        >>> l.ajouter(1)
        >>> l[0]
        1
        >>> l[0] = 8
        >>> l[0] 
        8
        '''   
        #Précondition :
        assert isinstance(n, int) and 0 <= n <= self.longueur, 'n doit être un entier (int) entre 0 compris et la longueur de la liste compris !'
        #Code :
        return self.acceder(n).mut_valeur(valeur) #Modifie la valeur par la valeur passé en paramètre du maillon d'indice n.
    


class Pile() :
    '''
    Une classe pour implémenter une pile.
    '''
    def __init__(self):
        '''
        Initialise une pile vide avec l'attribut sommet (Maillon)
        qui est le sommet de la pile (par défaut, il n'y a pas de sommet).
        : pas de return, on initialise.
        '''
        self.sommet = None

    def est_vide(self):
        '''
        Renvoie True si la pile est vide et False sinon.
        : return (boolean)
        
        >>> p = Pile()
        >>> p.est_vide()
        True
        >>> p.empiler(1)
        >>> p.est_vide()
        False
        '''
        return self.sommet == None

    def empiler(self, valeur):
        '''
        Ajoute la valeur passé en paramètre au sommet de la pile.
        : param valeur (type inconnu)
        : pas de return
        '''
        self.sommet = Maillon(valeur, self.sommet)

    def depiler(self):
        '''
        Enlève si possible la valeur au sommet de pile et la renvoie ou déclenche un message d'erreur si la pile est vide.
        : return (type inconnu)
        
        >>> p = Pile()
        >>> p.empiler(1)
        >>> p.empiler(2)
        >>> p.empiler('a')
        >>> p.depiler()
        'a'
        >>> p.depiler()
        2
        '''
        #Précondition :
        assert not self.est_vide(),'La pile est vide !'
        #Code :
        valeur = self.sommet.acc_valeur()
        self.sommet = self.sommet.acc_suivant()
        return valeur

    def __str__(self):
        '''
        Renvoie une chaine pour visualiser la pile.
        : return (str)
        
        >>> l = Pile()
        >>> l.empiler(1)
        >>> print(l)
        1
        _
        >>> l.empiler(2)
        >>> print(l)
        2
        1
        _
        '''
        chaine = ''
        maillon = self.sommet
        while maillon != None :
            chaine = chaine + str(maillon.acc_valeur()) + '\n'
            maillon = maillon.acc_suivant()
        chaine += '_'
        return chaine

    def __repr__(self):
        '''
        Renvoie une chaine pour décrire la classe.
        '''
        return 'Classe Pile' 
    
    
    
    
class File:
    '''
    Une classe pour les Files.
    '''
    
    def __init__(self):
        '''
        Contruit une file vide de longueur 0 possédant une tête et une queue.
        '''
        self.tete = None # premier maillon de la queue
        self.queue = None # dernier maillon de la queue

    
    def est_vide(self):
        '''
        Renvoie True si la file est vide et False sinon.
        : return (boolean)
        
        >>> f = File()
        >>> f.est_vide()
        True
        '''
        return self.tete == None
    
    def enfiler(self, valeur):
        '''
        Ajoute un élement à la file. On en distinguera 3 :
         - le cas où la file est vide.
         - le cas où la file n'est pas vide.
        : param valeur (type inconnu), la valeur a ajouter
        
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.est_vide()
        False
        '''
        maillon = Maillon(valeur, None)
        if self.est_vide() :
            self.tete = maillon
            self.queue = maillon
        else :
            self.queue.mut_suivant(maillon)
            self.queue = maillon
            
    def defiler(self):
        '''
        Renvoie la valeur en tête de file et la retire de la file si la file n'est pas vide. déclenche un message d'erreur sinon.
        : return (type inconnu)
        
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.defiler()
        1
        >>> f.defiler()
        2
        >>> f.est_vide()
        True
        '''
        #Précondition :
        assert not self.est_vide(), 'La file est vide !'
        #Code :
        valeur = self.tete.acc_valeur()  
        self.tete = self.tete.acc_suivant()
        return valeur
    
    def __str__(self):
        '''
        renvoie la chaine permettant d'afficher la file
        : return (str)
        >>> f = File()
        >>> f.enfiler(3)
        >>> f.enfiler(2)
        >>> f.enfiler('a')
        >>> print(f)
        (3, (2, (a, ())))
        '''
        chaine = '(' #La chaine commence par ce caractère.
        nbre_paranthese = 1
        maillon = self.tete #Le premier maillon c'est le maillon en tête de la file.
        while maillon != None : #Si le maillon n'est pas vide :
            chaine = chaine + str(maillon.acc_valeur()) + ', (' #Ajoute à la chaine la valeur du maillon et des caractères supplémentaire.
            maillon = maillon.acc_suivant() #Le maillon devient le suivant du maillon.
            nbre_paranthese += 1
        chaine += ')' * nbre_paranthese #Quand tous les valeurs ont été ajoutées, on ferme toutes les parenthèses ouvertes.
        return chaine
    
    def __repr__(self):
        '''
        renvoie une représentation de la file
        : return (str)
        '''
        return 'Classe File'
            
            





######################################################
# Doctest :
######################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)