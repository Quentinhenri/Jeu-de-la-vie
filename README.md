# Jeu de la vie  

## Description succinte du projet / Informations clés 

**Noms et prénoms des membres du projet :** Lucas Guillen, Quentin Henri 

**Nom du projet :** Jeu de la vie 

**Modules tiers utilisés :**
- Pygame 
- PyQt5 
- Os 
- Random 
- Json 
- Time 
- Threading
- Sys

**Objectif du projet :** 

    1. Comprendre le fonctionnement du jeu de la vie et s'approprier les fonctions conçues à l'avance. 

    2. Créer une animation à l'aide des fonctions préétablies et des règles du jeu de la vie. 

##

**Mission des membres impliqués dans le projet :**

*Quentin :* En charge de la recherche d'images / Codage des figures / Implémentation de la musique dans les différents fichiers.

*Lucas :* En charge du codage des figures / Résolution des différents bugs / Réalisation du rendu final en tenant compte du rythme de la musique.

***

## Description précise du programme / Difficultés rencontrées 

*Les fichiers présents sur GitHub représentent l'ensemble de notre travail. Pour une meilleure compréhension, nous avons décidé de classer les fichiers en deux catgéories :*

    1- Figures codées 
    2- Fonctions utiles

> Nota : Le dépôt contient un PowerPoint dans lequel nous avons identifié une vingtaine de couleur présentent dans Python. Il y a également un fichier texte avec le script initiale qui, étant trop complexe, a été redimensionné.  

## Détail précis des modifications des différents fichiers 

    1. jdlv_model.py : Aucun ajout. 
##
    2. jdlv_qrc.py : Aucun ajout.
##
    3. jdlv.qrc : Aucun ajout.
##
    4. jdlv_ui : Aucun ajout.
## 
    5. jdlv_rc.py : Aucun ajout.
##
    6. jdlv_other_functions.py : Aucun ajout. 
##
    7. jdlv_main.py : Aucun ajout. 
##
    8. jdlv_vue_fromUi.py : Aucun ajout.
##
    9. jdlv_my_tools.py : 
- Import des différents fichiers comprenant les images codées. 
- Ajout de 5 fonctions permenttant d'animer le projet sur la grille PyQt5. 

##
    10. jdlv_vue.py : Aucun ajout. 
##
    11. jdlv_data.py :
- Ajout des différentes couleurs nécessaires à la reproduction des figures présentées

##
    12. jdlv_outil.py : 

- Remplacement de la couleur "red" dans la fonction revive_case (case) par "grey"
    
- Ajout de la fonction play_music () ainsi que du module Pygame. Cette fonction permet d'initialiser la musique qui sera ensuite traitée dans le fichier jdlv_controleur.py 

##

    13. jdlv_controleur.py : 

- Ajout de la fonction play_music () dans la fonction action_pb_play_pause_clicked aisni que du module pygame (pygame.mixer.music.play) qui permet de jouer la musique quand on clique sur le bouton play. 

- Changement de la variable "apply_game_or_life_rules" par "scene_1" dans la fonction action_pb_play_pause_clicked. 

##
    14. plan_planisphere_individuel.py : Fichier avec les 14 fonctions correspondant aux 14 parties du monde. 
##
    15. plan_planisphere_global : Fichier avec la fonction permettant d'afficher le planisphere global. 
##
    16. plan_france_individuel : Fichier avec les 7 fonctions correspondant aux 7 parties de la France. 
##
    17. plan_france_global : Fichier avec la fonction permettant d'afficher la France en entier 
##
    18. plan_moto_position1 : Fichier avec la focntion correspondant à la moto avec la fumée collée au pot d'échappement 
##
    19. plan_moto_position2 : Fichier avec la focntion correspondant à la moto avec la fumée détachée du pot d'échappement
##
    20. plan_moto_position3 : Fichier avec la focntion correspondant à la moto sans fumée derrière le pot d'échappement
##
    21. plan_arc_de_triomphe : Fichier avec la fonction permettant d'afficher l'arc de triomphe 

## Détail précis des fonctions 

### Fonctions permettant de coder les images

grid = clean_grid (grid)
- Permet d'effacer la figure précédente et de commencer sur une grille vierge sans passer par la fonction clean_grid (grid) 

cases [i + 4] [j + 39] ['s'] = life_status
cases [i + 4] [j + 39] ['c'] = color
- Les deux lignes permettent de coder le pixel en fonction de ses coordonnées sur l'axe horizontal et vertical. Elles permettent également d'indiquer la couleur de la case. 

##

### Fonctions permettant de jouer la musique 

pygame.mixer.init()
- La ligne de code permet d'initialiser la musique 

pygame.mixer.music.load('videoplayback.ogg')
- La ligne de code permet de charger la musique à partir du fichier ogg. 

> Nota : Le fichier, tout d'abord téléchargé en MP3 a été converti en ogg pour être lu sur Spyder. Nous avons utilisé le fichier sous son format MP3 pour identifier les différents temps de la musique dans Audacity. 

##

### Fonctions permettant d'animer la grille 

elif compteur <= 1 :
- Si le compteur est inferieur à 1, c'est-à-dire si il y a eu qu'une seul grille d'initialisée précédemment, alors 

print ("COMPTEUR % 11  is  56")
- Permet de vérifier que l'animation de la grille fonctionne correctement. 

next_grid = \
           make_planisphere_plan1 (grid, 4, 4, "grey")
- Mention de l'élément qui va s'afficher dans la grille 

time.sleep (3.08)
- Durée avant la prochaine animation. 

##

### Difficultés rencontrées lors du projet : 

Le codage des différentes figures s'est avéré très chronophage. Nous avons redimensionné nos ambitions au cours de notre projet. Notre idée initiale étant trop complexe à réaliser, nous avons choisi de présenter nos différents monuments puis de mettre en place le jeu de la vie. 

*Auteurs :* Lucas Guillen et Quentin Henri 1-01 
