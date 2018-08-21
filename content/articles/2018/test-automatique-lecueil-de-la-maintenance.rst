Test automatique : l'écueil de la maintenance
#############################################
:date: 2018-01-19 08:28
:author: apallier
:category: opinion
:tags: automatisation, test logiciel
:slug: test-automatique-lecueil-de-la-maintenance

.. raw:: html

   <div dir="ltr" style="text-align: justify;">

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

La confusion n'est pas loin - et le terme est trompeur - entre
"*automatiser des tests*"* *\ et\ * *"*tester automatiquement un
logiciel*". Or il s'agit bien du premier terme dont on parle lorsqu'on
dit "Test automatique". Cette différence tenue est pourtant fondamentale
car elle nous dit que les tests ne vont pas vraiment fonctionner tout
seuls. Il va falloir les écrire et les maintenir au même titre
d'ailleurs que  n'importe quel logiciel informatique...

.. raw:: html

   </div>

.. raw:: html

   <div dir="ltr">

**
Pourquoi ?**

.. raw:: html

   </div>

.. raw:: html

   <div dir="ltr">

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: justify;">

Les tests automatiques vérifient un logiciel. Ce logiciel est sujet à
des modifications, si du moins le projet est "vivant". Ces changements
devront nécessairement se répercuter dans les tests et/ou dans
l'environnement de test. Or ces changements ont un coût. Ce coût englobe
le temps, les personnes et les compétences qu'il est nécessaire de
déployer pour que les tests automatiques fonctionnent tout au long de la
vie du projet.

.. raw:: html

   </div>

.. raw:: html

   <div style="text-align: justify;">

Des tests automatiques non maintenus perdent très vites de leur valeur,
surtout si le logiciel qu'ils testent évolue vite. On peut même imaginer
arriver à un point de non retour où il n'est plus rentable de les
remettre à jour. L'investissement dans les tests auto ne sera jamais
rentabilisé, créant alors beaucoup de déception.

.. raw:: html

   </div>

| 

.. raw:: html

   <div dir="ltr">

**Mieux vaut prévenir...**

.. raw:: html

   </div>

.. raw:: html

   <div dir="ltr" style="text-align: justify;">

La négligence des aspects de maintenance est à mon avis l'une des
principales causes d'échec des projets d'automatisation. Après avoir
investi dans la mise en place d'un environnement de test, on se rend
compte que cela ne marche pas exactement "tout seul", il y a toujours
besoin de réaliser des ajustements. On est déçu et on abandonne.

.. raw:: html

   </div>

.. raw:: html

   <div dir="ltr" style="text-align: justify;">

On rêverait tous d'un logiciel qui s'auto-teste tout seul (pléonasme ?).
En attendant, à nous testeurs de rappeler aux décideurs que **l'enjeu de
la maintenance est crucial** afin qu'il n'y ait pas de déception et que
l'on puisse se lancer (ou non d'ailleurs) dans des projets
d'automatisation de tests en **connaissance de cause**, en sachant sans
feindre de l'ignorer quel est le vrai "prix" de l'automatisation.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. |image0| image:: https://2.bp.blogspot.com/-pdVmK5WMBT8/WmGrjHSdvRI/AAAAAAAACEI/g7LDnEsZ6dMd5ooj2o5hsTUMaFMVC1a-QCLcBGAs/s200/P1090393.jpg
   :width: 200px
   :height: 150px
   :target: https://2.bp.blogspot.com/-pdVmK5WMBT8/WmGrjHSdvRI/AAAAAAAACEI/g7LDnEsZ6dMd5ooj2o5hsTUMaFMVC1a-QCLcBGAs/s1600/P1090393.jpg
