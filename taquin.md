# Le taquin

## Règles du jeu



Le taquin est un jeu de puzzle. Il est composé de 16 cases. Les quinze premières cases sont numérotées de 1 à 15. La dernière est vide. Lorsque les cases apparaissent dans l'ordre ci-dessous, le jeu est en position initiale.

```txt
+----+----+----+----+
|  1 |  2 |  3 |  4 |
+----+----+----+----+
|  5 |  6 |  7 |  8 |
+----+----+----+----+
|  9 | 10 | 11 | 12 |
+----+----+----+----+
| 13 | 14 | 15 |    |
+----+----+----+----+
```

A partir de cette position, on _mélange_ les cases pour obtenir, par exemple, le puzzle suivant :

```txt
+----+----+----+----+
| 15 |  4 | 12 |  5 |
+----+----+----+----+
| 10 |    |  3 |  6 |
+----+----+----+----+
|  9 | 14 |  8 | 13 |
+----+----+----+----+
|  2 |  1 |  7 | 11 |
+----+----+----+----+
```

On peut ensuite déplacer les cases numérotées se trouvant à droite, à gauche, au dessus ou en dessous de la case vide. Dans l'exemple ci-dessus, il est possible de déplacer les cases 4, 10, 3 et 14 en les glissant dans la case vide. Leur case initiale devient alors la case vide.



Par exemple, si on choisit de jouer la case 4, la grille devient :

```txt
+----+----+----+----+
| 15 |    | 12 |  5 |
+----+----+----+----+
| 10 |  4 |  3 |  6 |
+----+----+----+----+
|  9 | 14 |  8 | 13 |
+----+----+----+----+
|  2 |  1 |  7 | 11 |
+----+----+----+----+
```

L'objectif est de revenir à la position initiale.



### Initialisation de la classe `Taquin`

Créer un programme `module_taquin.py` dans lequel nous allons commencer par définir une classe pour le taquin. 

```python
# -*- coding: utf-8 -*-
'''
    la classe Taquin
    : Auteur 
'''
    
class Taquin():
    '''
    une classe pour le jeu du taquin
    '''
    def __init__(self):
        '''
        initialise l'objet
        '''
        
```

Il faut maintenant initialiser un attribut qu'on nommera `grille` et qui stockera les données du taquin, c'est à dire la grille de jeu. On représentera une case vide par l'entier 0 et les autres cases par la valeur entière qu'elles contiennent. On va utiliser pour cela une liste de 16 entiers.



Par exemple, dans la situation ci-dessous, l'attribut `grille` serait le tableau [15, 0, 12, 5, 10, 4, 3, 6, 9, 14, 8, 13, 2, 1, 7, 11] 

```txt
+----+----+----+----+
| 15 |    | 12 |  5 |
+----+----+----+----+
| 10 |  4 |  3 |  6 |
+----+----+----+----+
|  9 | 14 |  8 | 13 |
+----+----+----+----+
|  2 |  1 |  7 | 11 |
+----+----+----+----+
```



**Remarque importante :**

Dans tout le projet, il ne faudra pas confondre l'indice de la case et la valeur qu'elle contient.

Par exemple, si je reprends la grille placée juste au dessus et la liste qui lui correspond  :

* la case d'indice 2 contient la valeur 12.
* la case de valeur 7 aura pour indice 14.





> Complétez :
>
> ```python
> class Taquin():
>        '''
>        une classe pour le jeu du taquin
>        '''
>        def __init__(self):
>            '''
>            initialise l'objet
>            '''
>            self.grille = 
> ```
>
> 

## Accesseurs, mutateurs et prédicats

Comme d'habitude, on va séparer la structure du reste du code grâce à des accesseurs, des mutateurs et des prédicats. 





> Considérons les méthodes ci-dessous :
>
> ```python
>     def acc_valeur(self, indice):
>         '''
>         renvoie le contenu de la case d'indice précisé avec 0 <= indice <= 15
>         : param
>         : return
>         >>> t = Taquin()
>         >>> t.get_valeur(0)
>         1
>         >>> t.get_valeur(10)
>         11
>         >>> t.get_valeur(15)
>         0
>         '''
> 
> 
>     def mut_valeur(self, indice , valeur):
>         '''
>         modifie le contenu de la case d'indice précisé avec 0 <= indice <= 15 
>         en y plaçant la valeur précisée avec 0 <= valeur <= 15
>         : param
>         : param
>         : Pas de return, self est modifié par effet de bord
>         >>> t = Taquin()
>         >>> t.set_valeur(0, 1)
>         >>> t.get_valeur(0)
>         1
>         >>> t.set_valeur( , )
>         >>> t.get_valeur( )
>              
>         '''
> 
> 
>     def acc_indice(self, valeur):
>         '''
>         renvoie l'indice de la case de la grille qui contient la valeur précisée
>         avec 0 <= valeur <= 15
>         : param
>         : return 
>         >>> 
>         
>         >>>
>         
>         '''
> 
>     def est_vide(self, indice) :
>         '''
>         renvoie True si (0 <= indice <= 15 et la case d'indice précisé est vide)
>         et False sinon
>         : param 
>         : return
>         >>>
>         
>         >>>
>         
>         '''
>     
>     def est_gagne(self):
>         '''
>         renvoie True si la grille est en position initiale et False sinon
>         : return
>         >>>
>         
>         >>>
>         
>         '''
> 
> ```
>
> * Complétez les spécifications.
> * Chaque méthode doit avoir un jeu de 2 tests au minimum.
> * Complétez ensuite le code de chaque méthode sans mettre les assertions. Déboguez au fur et à mesure, méthode par méthode.



Dorénavant, il est obligatoire de ce servir de ces méthodes uniquement pour accéder à la grille ou la modifier. 



## Affichages

On souhaite que les affichages soient les suivants :
```python
>>> t = Taquin()
>>> t
une grille de Taquin
>>> print(t)
+----+----+----+----+
|  1 |  2 |  3 |  4 |
+----+----+----+----+
|  5 |  6 |  7 |  8 |
+----+----+----+----+
|  9 | 10 | 11 | 12 |
+----+----+----+----+
| 13 | 14 | 15 |    |
+----+----+----+----+

```


> Complétez la méthode `__str__` ci-dessous afin de représenter la grille de la façon présentée en haut de ce projet ainsi que la méthode `__repr__` afin de décrire la classe `Taquin`.
>
> ```python
>        def __str__(self) :
>            '''
>            renvoie une chaine de caractères pour représenter la grille.
>            : return (str)
>            '''
>            chaine = ''
> 
> 
>        def __repr__(self):
>            '''
>            renvoie une chaine qui décrit la classe grille.
>            : return (str)
>            '''
>            return 
> ```
>
> * `__str__` n'est pas une méthode facile à écrire. On pourra se servir du fait que la case d'indice `n` a pour coordonnées (`n % 4`, `n //  4`) ou, inversement, que la case de coordonnées `(x, y)` a pour indice `x + y * 4`.
> * Pas besoin de doctests ici.

  

 Testez dans la console !




## Déplacer les cases

Pour jouer, on a besoin de savoir si une case est déplaçable ou non.

  

> Complétez la méthode ci-dessous :
>
> ```python
> 	def est_possible(self, valeur) :
>         '''
>         renvoie True si la case contenant la valeur (entre 0 et 15)
>         passée en paramète est déplaçable et False sinon
>         : param valeur (int) avec 0 < valeur <= 15
>         : return (boolean)
>         >>> t = Taquin()
>         >>> t.est_possible(12)
>         True
>         >>>
> 
>         >>>
>         False
>         '''
> ```
>
> On n'oubliera pas les assertions.
>
> _Remarque :_ utiliser `est_vide` serait judicieux.



Il ne reste plus qu'à pouvoir déplacer une case donnée, lorsque cela est possible.

> Complétez le code ci-dessous :
>
> ```python
> 	def deplacer(self, valeur) :
>         '''
>         deplace, si cela est possible, la case contenant la valeur précisée
>         en paramètre (entre 1 et 15) dans la case vide. Si le déplacement n'est pas 
>         possible, il ne se passe rien.
>         : param
>         : pas de return mais self est mofifié par effet de bord
>         '''
> ```
>
> On n'oubliera ni la Docstring ni un jeu de tests bien choisi ni les assertions.



## Mélanger le jeu



En échangeant aléatoirement 2 cases du jeu, on risque de tomber sur un puzzle insolvable. Pour remédier à ce problème, on va mélanger la grille en jouant au hasard un certain nombre de coups. De cette façon, il suffirait de jouer ces coups à l'envers pour gagner : il y a forcément une solution au puzzle.



Plus on joue de coups, plus le taquin sera difficile à résoudre  :

* 5 coups  : ce sera le niveau 0
* 10 coups : ce sera le niveau 1
* 30 coups : ce sera le niveau 2
* 100 coups : ce sera le niveau 3
* 200 coups : ce sera le niveau 4



Pour commencer, on aura besoin de savoir quelles cases sont déplaçables.

>Complétez la méthode ci-dessous :
>
>```python
>    def valeurs_deplacables(self):
>             '''
>             renvoie une liste des valeurs des cases déplaçables
>             : return (list)
>             >>> t = Taquin()
>             >>> t.valeurs_deplacables()
>             [12, 15]
>             >>> t.deplacer(12)
>             >>> t.valeurs_deplacables()
>             [8, 11, 12]
>             '''
>```
>
>Regardez bien les Doctests proposés pour comprendre cette méthode.



Maintenant qu'on peut à tout moment connaître les valeurs déplaçables, il suffit, un grand nombre de fois de suite selon le niveau souhaité, d'en choisir une au hasard et de la déplacer. On aura donc besoin du module `random` et de la méthode `random.choice(une_liste)` qui renvoie au hasard un élément de la liste passée en paramètre.



> Définissez , documentez, testez puis codez la méthode `melanger(self, niveau)` qui mélange le puzzle selon le `niveau` passé en paramètre qui est un entier compris entre 0 et 4 inclus.
>
> N'oubliez pas les assertions.



Testez :

```python
>>> t = Taquin()
>>> t.melanger(0)
>>> print(t)
???
>>> t.melanger(4)
>>> print(t)
???
```

 

### Jouons au Taquin !

Créez un programme nommé `taquin.py`. Nous allons y programmer le jeu du taquin en nous servant de notre module.

Le principe du jeu est simple :

* le joueur le démarre en décidant d'un niveau entre 0 et 4.
* Le puzzle se mélange selon le niveau choisi.
* Tant que la grille n'est pas en revenue position initiale :
    * on affiche le taquin.
    * on demande la valeur de la case que le joueur souhaite déplacer (on pourra utiliser un `input`).
    * on déplace la case choisie.
* A l'issu de la boucle, on affiche une dernière fois la grille victorieuse et on félicite le joueur en précisant le nombre de coups qu'il a utilisé.



> Une seule fonction demandant le paramètre `niveau` est nécessaire.
>
> Définissez là et codez là.



_Remarque :_

Prochainement nous proposerons une résolution automatique du taquin... mais il nous manque des connaissances pour l'instant.



___________

Par Mieszczak Christophe Licence CC BY SA
