Test automatique : la Flakiness
###############################
:date: 2018-09-02 8:30
:author: apallier
:category: opinion
:tags: automatisation, test logiciel
:slug: test-automatique-flakiness


.. image:: {static}/images/2018-test-automatique-flakiness.jpg
   :width: 300px
   :align: center
   :alt: Test automatique : la Flakiness

Qu'est-ce que la flakiness ?
----------------------------

Il existe un phénomène peut-être méconnu ou bien sous-estimé lorsque l'on fait du Test automatique : la "**flakiness**".

Google définit le terme "*flaky*" de la façon suivante [#f1]_ :

   Un résultat de test est "*flaky*" lorsque le test peut à la fois passer et être un échec sur le même code
   
La *flakiness* est donc ce qui caractérise des tests qui peuvent passer ou être en échec entre deux exécutions exactement identiques 
(mêmes logiciels, versions, environements...). On a donc des résultats contradictoires sur deux campagnes de test identiques.
Il devient alors difficile de se faire un avis précis de l'état du logiciel testé. On ne peut plus distinguer les "vrais" bugs 
des "*flaky*" tests.

Quand la rencontre-t'on ?
-------------------------

Ce phénomène est une *constante lorsqu'on fait du Test automatique* [#f2]_. C'est un peu comme les infections nosocomiales,
on ne peut pas vraiment y échapper, il faut faire avec, tout en essayant de la mitiger au maximum.

Elle a tendance à augmenter avec le niveau de test. Par exemple, on peut en avoir un peu en tests unitaires, plus en intégration et encore
beaucoup plus en test d'acceptance via l'interface graphique.

Pourquoi ?
----------

Malheureusement, les causes de la *flakiness* sont nombreuses.

Pêle-mêle, on peut citer :

* Les environnements de test instables / non maitrisés. Un bon exemple : le réseau
* Les données de test (Test Data) non maitrisées. Exemple : données d'entrée aléatoires ou changeantes
* L'utilisation de threads, les exécutions parallèles, l'asynchronicité
* Les dépendances logicielles ou produits tiers non maitrisés. Exemple : des versions qui peuvent changer d'une exécution à l'autre
* Les tests via une interface graphique 
* La mémoire utilisée et la taille des binaires. Voir l'étude de Google [#f3]_ à ce sujet.

Que faire pour éviter la flakiness ?
------------------------------------

Il y a autant de solutions spécifiques que de causes différentes mais on peut citer les bonnes pratiques suivantes:

* Maitriser la configuration de son environnement à l'aide de fixtures (setup/teardown des tests)
* Limiter ou maîtriser les dépendances.
   Solutions : virtualiser les `environnements de test <{static}/articles/2016/memo-deploiement-denvironnement-de-test-ou-autres.rst>`_, 
   bouchonnner les outils tiers...
* Utiliser des attentes actives [#f4]_ plutôt que des attentes incompressibles pour attendre la fin d'une exécution
* Eviter de paralléliser les exécutions
* Limiter les tests via l'interface graphique ou utiliser l'*UI encapsulation* [#f5]_
* Rejouer automatiquement les tests en échec

Conclusion
----------

La *flakiness* est un véritable problème lorsque l'on fait du Test automatique. Il faut en prendre conscience pour ne pas être déçu
car, oui, cela engendre du `travail de maintenance des tests <{static}/articles/2018/test-automatique-lecueil-de-la-maintenance.rst>`_.
Mais elle permet également, si elle est vraiment prise en compte, de mieux comprendre comment fonctionne le logiciel que l'on teste.

Enfin, elle permet aussi de relativiser l'importance - quelque fois irraisonnable - que l'on place dans les résulats 
des tests automatiques ;-)

---------------

.. rubric:: Notes

.. [#f1] *"We define a "flaky" test result as a test that exhibits both a passing and a failing result with the same code."*
   https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html

.. [#f2] Voir paragraphe "A war you can’t win" de cet article : https://hackernoon.com/flaky-tests-a-war-that-never-ends-9aa32fdef359

.. [#f3] https://testing.googleblog.com/2017/04/where-do-our-flaky-tests-come-from.html

.. [#f4] Exemple d'implémentation d'attente active avec Robot Framework, le keyword `Wait Until Keyword Succeeds` : 
   http://robotframework.org/robotframework/latest/libraries/BuiltIn.html#Wait%20Until%20Keyword%20Succeeds
 
.. [#f5] Voir le paragraphe "Follow the Testing Pyramid" de cet article : https://smartbear.com/resources/ebooks/managing-ui-test-flakiness/
