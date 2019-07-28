Développement logiciel et Gouvernance
#####################################
:date: 2016-10-19 20:51
:author: apallier
:category: opinion
:tags: gouvernance, test logiciel
:slug: developpement-logiciel-et-gouvernance

|

    "Pour qu’on ne puisse abuser du pouvoir, il faut que, par la
    disposition des choses, le pouvoir arrête le pouvoir"
    
    -- Montesquieu, *De l'esprit des lois*

Cette citation de Montesquieu parle bien sûr de politique et de la
séparation de ses pouvoirs. Dans cet article, je vais décrire une
approche qui me permet de faire rapidement l'audit d'une entreprise sur
sa maturité en terme de test logiciel.
Il m'a paru intéressant de rapprocher cette citation du domaine du
développement logiciel. En essayant de déterminer quels sont les jeux de
pouvoir qu'il peut exister au sein d'une entreprise qui développe des
produits logiciels, on peut voir apparaître les forces et les lacunes
qui conduisent à des dérives et des biais dans la construction d'un
produit logiciel.

Les pouvoirs en présence
------------------------

Les trois pouvoirs politiques définis par Montesquieu [#f1]_ sont :

-  Le pouvoir **législatif**
-  Le pouvoir **exécutif**
-  Le pouvoir **judiciaire**

Maintenant, transposons cette vision dans le domaine de l'industrie
logicielle. On peut définir 3 pouvoirs qui gravitent autour d'un produit
logiciel :

-  Le pouvoir de **définir** le produit : législatif
-  Le pouvoir de **construire** le produit : exécutif
-  Le pouvoir de **contrôler** l'état du produit : judiciaire

Pour illustrer cette notion, on peut par exemple rapprocher ces
"pouvoirs" de différentes entités qu'il est commun de trouver dans
l'industrie du logiciel :

-  La MOA [#f2]_ : entité chargée de définir le produit et de formuler les besoins
   des clients et du marché, qui a le pouvoir de définir
-  La MOE [#f3]_ : entité de développement du logiciel, peut être appelée aussi "R&D"
   ou "équipes de développement", qui a le pouvoir de construire
-  La QA [#f4]_ : entité chargée de vérifier le bon fonctionnement du produit, qui a
   le pouvoir de contrôler l'état du produit


Jeu de pouvoir
--------------

L'idée consiste maintenant à évaluer les équilibres entre les pouvoirs
qu'il existe au sein d'une entreprise entre ces entités.

Il s'agit d'évaluer pour chacune d'elles, leurs effectifs, leurs rôles
hiérarchiques, les degrés d'indépendance, les processus qui les font
interagir, etc. On pourra alors avoir une idée des forces en présence
afin d'évaluer s'il n'y a pas une carence ou un excès de tel ou tel
pouvoir.

Exemples
~~~~~~~~

-  Prenons le cas d'une MOA qui définirait uniquement des exigences
   métiers ou des exigences fonctionnelles. Elle conduirait la MOE à ne
   s'attacher à résoudre que des problématiques d'ordre fonctionnel et à
   construire un produit qui fonctionne peut-être mais mal car ayant des
   lacunes dans le domaine non-fonctionnel (comme la performance,
   l'utilisabilité, la facilité de déploiement, etc).
   
-  Un autre exemple : Prenons le cas d'une société qui aurait une MOE de
   100 personnes et une QA de 5 personnes. La responsabilité de la QA
   étant sous celle de la MOE. On voit bien ici le déséquilibre entre le
   pouvoir de construction et le pouvoir de contrôle. Le risque ici est
   bien de livrer un produit qui est construit de façon non contrôlée et
   qui ne correspondra pas aux attentes en terme de fonctionnalités et
   de qualité.

-  Un troisième cas, qui de mon point de vue est sûrement le plus rare,
   la QA est constituée d'une équipe importante, ayant un fort degré
   d'indépendance par rapport à la MOA et la MOE. Son pouvoir de
   contrôle et de veto surdimensionné pourrait nuire au bon déroulement
   de la construction. La QA pourrait demander des exigences
   qualitatives difficiles à atteindre et qui ferait augmenter les coûts
   de développement.

Conclusion
----------

Cette réflexion m'est venue suite à un audit réalisé dans une entreprise
qui avait des problèmes de fiabilité sur ses logiciels. Je me suis
aperçu que selon la définition des pouvoirs que j'ai énoncé ici,
l'entité QA était réellement sous dimensionnée. Les personnes dédiées au
Test et à la Qualité représentent moins de 10% de l'effectif et donc
approximativement du budget, alors que le standard de l'industrie sont
deux à trois fois supérieurs à cela depuis plusieurs années [#f5]_. 
Il y avait donc clairement un déficit dans le contre-pouvoir du
contrôle de la Qualité, expliquant en partie les problèmes de fiabilité
rencontrés par cette entreprise.

J'espère que ce petit outil permettra à d'autres d'évaluer les lacunes
et les forces en présence dans une entreprise ou une équipe de
développement. C'est un exercice que j'ai trouvé intéressant à faire et
qui m'a permis de mieux comprendre le contexte d'une entreprise.

+----------------------------------------------------+
| |image0|                                           |
+----------------------------------------------------+
| Sketchnote "Développement logiciel et Gouvernance" |
+----------------------------------------------------+

---------------

.. rubric:: Notes

.. [#f1] https://fr.wikipedia.org/wiki/S%C3%A9paration\_des\_pouvoirs#Montesquieu\_:\_reprise\_de\_la\_philosophie\_de\_Locke
.. [#f2] MOA = Maîtrise d'ouvrage
.. [#f3] MOE = Maîtrise d'oeuvre
.. [#f4] QA = Quality Assurance ou Assurance Qualité
.. [#f5] Voir à ce sujet le "World Quality Report 2015-16" : en 2015, en moyenne 35% du budget IT est alloué à la Qualité et au Test : www.world-quality-report.com

.. |image0| image:: {static}/images/2016-SketchnoteDéveloppementLogicielEtGouvernance.jpg
   :width: 640px
   :height: 414px
   :target: {static}/images/2016-SketchnoteDéveloppementLogicielEtGouvernance.jpg
