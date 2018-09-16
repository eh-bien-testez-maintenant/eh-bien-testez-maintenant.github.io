La stratégie de test de la "Terre ronde"
########################################

:date: 2018-09-16 18:00
:author: apallier
:category: revue
:tags: strategie, test logiciel
:slug: strategie-test-terre-ronde


.. image:: {filename}/images/2018-terre-globe.jpg
   :width: 400px
   :align: center
   :alt: La stratégie de la "Terre ronde"
   
.. Photo by Suzy Hazelwood from Pexels

James Bach vient de publier (le 08/09/2018) sur son blog `un article <http://www.satisfice.com/blog/archives/4947>`_  dans 
lequel il explique l'analogie qu'il fait entre le forme sphérique de la Terre et le Test logiciel.

Il a appelé ce modèle la **stratégie de test de la "Terre ronde"** et je vais tenter d'en expliquer les grandes lignes [#f1]_.

Qu'est-ce que la stratégie de test de la "Terre ronde" ?
--------------------------------------------------------

Un modèle pour expliquer le Test logiciel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avant de parler du modèle de la "Terre ronde", nous allons parler d'un autre modèle similaire,
bien connu des testeurs : la "**Pyramide du Test automatique**" [#f2]_

.. image:: http://www.mountaingoatsoftware.com/uploads/blog/Testpyramid.jpg
   :width: 200px
   :align: center
   :alt: Pyramide du Test automatique

Ce modèle part d'une pyramide - plutôt un triangle - découpée en couches ou strates horizontales successives. 
Chaque strate représente un niveau de test. 
L'analogie est faite entre la forme évasée du triangle et la proportion de tests automatiques à réaliser.
Dans les couches basses, il doit y avoir plus de tests que dans les hautes avec une diminution progressive, 
d'où la forme triangulaire.

Ce modèle permet d'expliquer un aspect du Test automatique par analogie avec une forme géométrique.

C'est ce que fait James Bach en utilisant l'analogie de la "Terre ronde". Il utilise la forme sphérique répartie
en couches concentriques de la Terre pour modéliser un aspect du Test logiciel :

.. image:: {filename}/images/2018-strategie-test-terre-ronde.png
   :width: 800px
   :align: center
   :target: {filename}/doc/strategie-test-terre-ronde.pdf
   :alt: La stratégie de la "Terre ronde"

Un modèle qui montre les enjeux du test à différents niveaux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'idée derrière le modèle de la "Terre ronde" est de penser les technologies comme les **couches terrestres concentriques**.
Chaque couche a un volume qui représente les possibilités, c'est-à-dire **l'espace des états possibles du produit à tester**.
Ce volume tend donc à augmenter de façon drastique à chaque couche. 
On imagine alors facilement les problématiques de test qui en découlent à chaque niveau.

En bas du modèle, au niveau du noyau terrestre, se trouvent les frameworks, les systèmes d'exploitation et les environnements de développement, en d'autres termes,
tout ce qu'on ne va pas tester. Les développements reposent sur cette "fondation solide" de suppositions. 
Ces suppositions sont généralement sûres, bien que quelques fois de la lave ou du gaz radon ou une source souterraine toxique, peuvent traverser cette fondation.

Si on monte d'un niveau, on arrive au code du produit que l'on peut tester de façon unitaire puisque nous en sommes les auteurs. 
Ces tests sont typiquement écrits par des développeurs de manière "souterraines" à un niveau relativement bas. 
Cependant, les utilisateurs eux vivent tout en haut, à la lumière. Les développeurs peuvent donc avoir des difficultés à adopter 
le point de vue des utilisateurs car ils sont "empêtrés" dans les détails de leur travail et biaisés par leur haut-niveau d'expertise.

En montant dans les couches, on arrive alors à l'endroit où interagissent les sous-systèmes. 
Ceux-ci peuvent typiquement être testés via une API ou en ligne de commande.
C'est à ce niveau que les outils de test excellent. 
On peut d'ailleurs s'imaginer les outils de test comme des sous-marins évoluant sous la tempête.

Enfin, la surface de la Terre, lieu où peuvent sévir des intempéries, il y a l'interface graphique (GUI).

Un modèle qui nous rappelle l'importance des données
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

James Bach donne une importance particulière aux données. 
Il les représente comme les flux d'énergies qui agissent au dessus de la surface (le soleil, le vent, l'eau)
et en dessous (eaux souterraines, magma, tremblements de terre). 
Lorsque l'on teste, les données sont partout, dans des bases, dans le cloud si on fait du micro-service.
Il y en a même dans le code. 
Enfin, les données sont bien sûr dans ce que les utilisateurs saisissent mais aussi dans la manière dont ils manipulent le produit.

Un modèle qui nous rappelle l'importance de la testabilité
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un produit "testable" est un produit qui peut être décomposé en parties testables séparément. 
On doit également pouvoir observer et contrôler son comportement.
Cela signifie que les testeurs doivent avoir accès à des parties plus "internes" du logiciel via une interface (comme une ligne de commande ou une API),
et à un système de journalisation (logging).


Conclusion
----------

Pour conclure son propos, James Bach finit par ces quelques remarques :

* La qualité apparente (à la surface) nécessite de la qualité sous-jacente (en souterrain)
* La qualité apparente réduit la dépendance à de coûteux tests de haut-niveau
* Les tests de bas-niveau, peu coûteux, réduisent la dépendance à de coûteux tests de haut-niveau
* Le risque augmente jusqu'à l'utilisateur

---------------

.. rubric:: Notes

.. [#f1] Cet article n'est pas une traduction mot pour mot de l'article de James Bach mais plutôt un résumé librement interprété, en français
       mais qui, je l'espère, reste assez fidèle à l'original. Merci à James Bach pour ce travail.

.. [#f2] Quelques références sur la "Pyramide du Test Automatique" :

   * https://watirmelon.blog/testing-pyramids/
   * https://martinfowler.com/bliki/TestPyramid.html
   * https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid

