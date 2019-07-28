Test automatique : l'écueil de la maintenance
#############################################
:date: 2018-01-19 08:28
:author: apallier
:category: opinion
:tags: automatisation, test logiciel
:slug: test-automatique-lecueil-de-la-maintenance


.. image:: {static}/images/2018-test-automatique-lecueil-de-la-maintenance.jpg
   :width: 200px
   :height: 150px
   :align: center
   :alt: Test automatique : l'écueil de la maintenance

La confusion n'est pas loin - et le terme est trompeur - entre
"*automatiser des tests*" et "*tester automatiquement un logiciel*". 
Or il s'agit bien du premier terme dont on parle lorsqu'on
dit "Test automatique". Cette différence tenue est pourtant fondamentale
car elle nous dit que les tests ne vont pas vraiment fonctionner tout
seuls. Il va falloir les écrire et les maintenir au même titre
d'ailleurs que  n'importe quel logiciel informatique...

Pourquoi ?
----------

Les tests automatiques vérifient un logiciel. Ce logiciel est sujet à
des modifications, si du moins le projet est "vivant". Ces changements
devront nécessairement se répercuter dans les tests et/ou dans
l'environnement de test. Or ces changements ont un coût. Ce coût englobe
le temps, les personnes et les compétences qu'il est nécessaire de
déployer pour que les tests automatiques fonctionnent tout au long de la
vie du projet.

Des tests automatiques non maintenus perdent très vites de leur valeur,
surtout si le logiciel qu'ils testent évolue vite. On peut même imaginer
arriver à un point de non retour où il n'est plus rentable de les
remettre à jour. L'investissement dans les tests auto ne sera jamais
rentabilisé, créant alors beaucoup de déception.

Mieux vaut prévenir...
----------------------

La négligence des aspects de maintenance est à mon avis l'une des
principales causes d'échec des projets d'automatisation. Après avoir
investi dans la mise en place d'un environnement de test, on se rend
compte que cela ne marche pas exactement "tout seul", il y a toujours
besoin de réaliser des ajustements. On est déçu et on abandonne.

On rêverait tous d'un logiciel qui s'auto-teste tout seul (pléonasme ?).
En attendant, à nous testeurs de rappeler aux décideurs que **l'enjeu de
la maintenance est crucial** afin qu'il n'y ait pas de déception et que
l'on puisse se lancer (ou non d'ailleurs) dans des projets
d'automatisation de tests en **connaissance de cause**, en sachant sans
feindre de l'ignorer quel est le vrai "prix" de l'automatisation.
