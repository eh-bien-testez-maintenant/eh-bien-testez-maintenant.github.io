##############################################################
 Comparatif Robot Framework - Playwright - Cypress - Selenium
##############################################################

:date: 2026-09-21
:author: apallier
:category: automatisation
:tags: Robot Framework, Playwright, Cypress, Selenium, tests, automatisation, qualité, QA
:slug: comparatif-robotframework-playwright-cypress-selenium

.. image:: {static}/images/2026-comparatif-robotframework-playwright-cypress-selenium.png
    :width: 300px
    :align: center
    :alt: Image d'un tableau comparatif entre Robot Framework, Playwright, Cypress et Selenium

On compare souvent les outils d'automatisation Robot Framework, Playwright, Cypress et Selenium car ils font référence
dans le domaine de l'automatisation de tests et en particulier les tests "web" (via un navigateur).

Certaines comparaisons que l'on peut trouver çà et là sur internet me dérangeaient puisqu'elles confondaient certaines
notions. On ne peut pas par exemple comparer une librairie et un framework.

J'ai voulu voir ce qu'il en était vraiment, en détail, pour essayer de mieux comprendre. En partant du modèle "gTAA"
(`Generic Test Automation Architecture
<https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf>`_), j'ai créé cette vue synthétique qui,
je l'espère, permet d'éclairer l'usage précis de chacun de ces outils d'automatisation de tests.

*********************************
 Selenium n'est pas un framework
*********************************

Selenium n'est pas un framework au sens strict du terme mais une librairie capable de piloter un navigateur en utilisant
le protocole WebDriver [1]_.

C'est une librairie utilisée pour tester mais elle n'offre à elle seule aucun cadre pour écrire des tests et nécessite
un "Test Runner" pour remplir, a minima, le rôle de "framework".

Associé à des frameworks de tests comme TestNG, JUnit ou autres, il a cependant été la référence pendant des années dans
les tests "web".

**************************************************
 Playwright et Cypress : 2 frameworks comparables
**************************************************

D'un point de vue purement "framework", Playwright et Cypress sont très comparables : orientés test "web", ils proposent
quasiment les mêmes fonctionnalités.

Playwright semble cependant gagner en adoption au détriment de Cypress ces derniers temps [2]_.

******************************************
 Robot Framework : le plus "orienté Test"
******************************************

Tous les frameworks de ce comparatif "se tiennent" dans les couches basses du modèle "gTAA", mais Robot Framework tire
son épingle du jeu sur l'approche "Test" pur.

Sa force réside dans son approche plus complète sur les aspects "Test" purs. Les personnes orientées Test/QA vont bien
s'y retrouver mais les profils plus "développeurs" vont avoir moins d'appétence à l'utiliser. C'est en tous cas ce que
j'ai remarqué dans mon expérience personnelle.

***************
 Le comparatif
***************

.. figure:: {static}/images/2026-comparatif-robotframework-playwright-cypress-selenium.png
    :target: {static}/images/2026-comparatif-robotframework-playwright-cypress-selenium.png
    :align: center
    :alt: Image d'un tableau comparatif entre Robot Framework, Playwright, Cypress et Selenium

    Robot Framework, Playwright, Cypress et Selenium positionnés selon le modèle gTAA

----

.. [1] Voir `WebDriver - MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/WebDriver>`_.

.. [2] Sur `npm trends <https://npmtrends.com/cypress-vs-playwright>`_, les téléchargements hebdomadaires de Playwright
    ont dépassé ceux de Cypress mi-2024 et l'écart n'a cessé de se creuser depuis. Le sondage `State of JS 2025
    <https://2025.stateofjs.com/en-US/libraries/testing/>`_ va dans le même sens : Playwright y reste le framework de
    test E2E le mieux noté, en popularité (usage) comme en satisfaction, avec un écart qui continue de se creuser face à
    Cypress.
