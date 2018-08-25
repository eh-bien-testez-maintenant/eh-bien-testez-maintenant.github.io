Les environnements de test logiciel
###################################
:date: 2017-11-01 21:37
:author: apallier
:category: opinion
:tags: environnement de test, test logiciel
:slug: les-environnements-de-test-logiciel

.. image:: {filename}/images/2017-les-environnements-de-test-logiciel.jpg
   :width: 200px
   :height: 133px
   :align: center
   :alt: Couverture du livre

Le déploiement d'environnement de test est une activité importante du
test logiciel. En effet, il peut devenir un point critique s'il est
complexe à mettre en place [#f1]_. C'est une lapalissade : "plus le
temps de mise en place d'un environnement de test est long, moins on
testera". Le temps qui est investi pour mettre en place l'environnement
de test diminue le temps pendant lequel on pourrait faire des tests.

    *"Plus le temps de mise en place d'un environnement de test est long
    et difficile, moins on testera et plus la barrière psychologique
    pour tester sera importante."*


Mais là n'est pas mon propos. Je voulais parler d'une autre conséquence
néfaste qui est **la barrière psychologique** que représente l'obstacle
de la mise en route. En effet, si votre environnement de test est
difficile à mettre en place, vous allez - peut-être même inconsciemment
- vous limiter dans vos tests. C'est un biais simplement humain, nous
préférons les tâches "simples" et courtes aux activités plus complexes.
Surtout que la mise en place d'un environnement de test logiciel n'est
pas non plus l'activité la plus "intéressante" qui existe :-)

Je prends deux illustrations très concrètes :

-  vous avez mis 1 journée entière pour mettre en place votre
   environnement. Vous allez éviter les cas de tests aux limites qui
   viendrait "casser" votre environnement (suppression de fichiers,
   arrêt électrique, corruption de la base de données...), cas qui
   pourtant pourraient s'avérer très intéressants d'un point de vue
   "test".
-  vous êtes à quelques heures d'une livraison et vous n'avez plus aucun
   environnement de test "propre" ou "standard". Vous avez un doute sur
   une partie du logiciel mais vous allez pourtant omettre ce petit test
   (qui quelque fois vous sauve la mise) avant la livraison car
   (consciemment ou inconsciemment) vous avez envisagé le temps de mise
   en place d'un nouvel environnement propre et que ce n'est peut-être
   pas le moment d'en perdre avant une livraison importante...

Diminuer le temps de mise en place
----------------------------------

Il devient donc important de faciliter la phase de mise en place des
environnements de test. Il faut inciter ou du moins ne pas "décourager"
les testeurs à tester en facilitant l'accès à un environnement prêt à
tester.

    *"Ne pas décourager les testeurs à tester, en facilitant le
    déploiement des environnements de test"*

*Comment ?* Plus facile à dire qu'à faire ! La mise en place
d'environnement nécessite du **matériel**, des **compétences en
virtualisation** ou conteneurisation, et des **compétences en
administration système**. Si vous développez ces compétences, vous aller
pouvoir optimiser votre temps de mise en place d'environnements de test
et globalement augmenter vos capacités de test.

Outils pour aller plus loin
---------------------------

Parmi les outils qui existent pour faciliter la mise en place d'environnement de test, on peut citer :

-  **les outils de type virtualisation / conteneurisation** : Docker,
   Vagrant et toutes les solutions de virtualisation (Virtual box,
   ESXi...)
-  **les outils de gestion de configuration système** : Salt Stack,
   Puppet, Ansible, Chef
-  **les outils de déploiements** :  Open stack, Cobbler, Foreman (Voir
   mon `memo à ce
   sujet <{filename}../2016/memo-deploiement-denvironnement-de-test-ou-autres.rst>`__)

.. [#f1] J'ai l'exemple d'une entreprise où un environnement de test nécessitait plusieurs jours de travail !