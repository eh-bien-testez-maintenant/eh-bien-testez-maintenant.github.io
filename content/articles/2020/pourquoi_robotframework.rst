Pourquoi Robot Framework ?
##########################

:date: 2020-02-12
:modified: 2023-09-09
:author: apallier
:category: automatisation
:tags: outil, automatisation, robotframework
:slug: pourquoi-robotframework

.. image:: {static}/images/2020-pourquoi-robotframework.jpg
   :width: 300px
   :align: center
   :alt: Image d'un robot en bois sur une pelouse

Pour automatiser des tests, il est nécessaire d'utiliser des outils adaptés. Partir la "fleur au fusil" avec  pour seule arme un langage de programmation n'est pas suffisant,
au risque de devoir réinventer la roue. Nous allons voir ensemble ici les caractéristiques qui font de `Robot Framework <https://robotframework.org/>`__ un bon candidat pour automatiser nos tests logiciels.

.. note::
    09/09/2023: cet article est d'abord paru sur le site "La Taverne du testeur" le 12/02/2020 sous le titre `"Robot Framework : Le Couteau Suisse De L’Automatisation" <https://latavernedutesteur.fr/2020/02/12/pourquoi-robot-framework-alexis-pallier/>`__.
    Comme j'en suis l'auteur et que cela fait maintenant un certain temps (> 3 ans...), je le publie maintenant aussi sur mon blog.

Les auteurs de Robot Framework le définissent lui-même comme :

    | [...] un framework **générique** et open-source d'automatisation pour le **Test de Validation**

Très clairement, et nous le verrons dans la suite de cet article, Robot Framework a été conçu pour automatiser les tests du niveau "Validation" (en anglais: "Acceptance Testing") et pour faire de
l'ATDD (Acceptance Test Driven Development). C'est-à-dire que son domaine de prédilection est le même que celui de l'utilisateur final [1]_.
**Il va permettre d’automatiser les actions que pourraient réaliser l'utilisateur du logiciel que l'on souhaite tester**. D'ailleurs, le nom "Robot" porte en lui-même l'idée que l'on cherche à
reproduire de façon programmatique le comportement d'un humain [2]_.

Un outil générique de validation
--------------------------------

Robot Framework possède des caractéristiques lui permettant de convenir à différentes situations de Test et en particulier de Test de Validation.

La polyvalence
^^^^^^^^^^^^^^

Les `librairies "standard" fournies <http://robotframework.org/robotframework/>`__ [3]_ par Robot Framework permettent de réaliser les multiples actions et vérifications nécessaires que pourrait faire
un utilisateur pour tester un logiciel.

Les librairies standard permettent, entre autres de:

* manipuler des données de base comme les chaines de caractères, les listes ou les dictionnaires
* manipuler des fichiers, dont des fichiers XML
* manipuler des processus
* manipuler des dates
* faire des assertions, ou autrement dit, faire des vérifications sur tous ces objets
* prendre des captures d'écran
* utiliser le protocole Telnet

Voici un exemple de test dans lequel nous allons rechercher une chaîne de caractère dans un fichier et vérifier qu'elle est bien présente (part 1).
Nous allons ensuite lancer un executable et vérifier qu'il s'est réellement bien exécuté :

.. code-block:: robotframework

    *** Test Cases ***
    Test Example
        # Part 1
        ${resultat_recherche}=    Grep File    mon_fichier.log    ${chaine_recherchee}
        Should contain    ${resultat_recherche}    ${chaine_recherchee}
        # Part 2
        Start process    mon_executable.exe    shell=true    alias=process
        ${result}=    Wait For Process    process    timeout=10s    on_timeout=kill
        Should Be Equal As Integers    ${result.rc}    0

L'adaptabilité
^^^^^^^^^^^^^^

**S'adapter au logiciel à tester**

Les librairies "standard" permettent, comme nous l'avons vu, d'écrire des tests basiques. Cependant, cela peut paraître limité pour s'adapter à des contextes de test plus évolués.
Robot Framework permet aussi d'utiliser des **librairies tierces**, codées en Python ou en Java. Ceci ouvre la porte à l'automatisation de nombreux logiciels puisqu'il suffit quasiment [4]_ qu'une librairie
(type harnais de test) existe pour que Robot Framework soit capable de se "brancher" dessus et d'exécuter des tests.

On peut citer surement ce qui est la plus "célèbre" des librairies tierces, `Selenium <https://robotframework.org/SeleniumLibrary>`__, qui permet d'automatiser les tests d'interface web.

Voici un exemple tiré de la documentation de Selenium. Nous allons ouvrir un navigateur sur le site mon-super-site.com,
puis saisir notre login et notre mot de passe et enfin vérifier que nous arrivont bien à la page de "bienvenue".

.. code-block:: robotframework

    *** Settings ***
    Library           SeleniumLibrary

    *** Variables ***
    ${LOGIN URL}      http://mon-super-site.com
    ${BROWSER}        Chrome

    *** Test Cases ***
    Valid Login
        Open Browser    ${LOGIN URL}    ${BROWSER}
        Title Should Be    Login Page
        Input Text    username_field    ${username}
        Input Text    password_field    ${password}
        Click Button    login_button
        Title Should Be    Welcome Page
        [Teardown]    Close Browser

**S'adapter aux testeurs**

Nous avons vu comment Robot Framework pouvait s'adapter au logiciel à tester et au contexte de test. Il faut savoir que Robot Framework peut aussi adapter sa manière d'écrire les tests.
En effet, il est possible d'**écrire les tests de plusieurs manières différentes**, soit en KDT [5]_ (ce que nous avons vu jusque ici dans les extraits de code) c'est à dire avec des instructions qui
"collent" aux actions et vérifications que pourrait faire un utilisateur, soit en utilisant le langage Gherkin, couramment utilisé en BDD [6]_ [7]_.

.. code-block:: robotframework

    *** Test Cases ***
    Gherkin Test Example
        Given login page is open
        When valid username and password are inserted
        and credentials are submitted
        Then welcome page should be open

Cela signifie que l'on peut d'abord partir sur une démarche ATDD, moins contraignante et évoluer ensuite vers une démarche BDD.
Cette liberté de choix est aussi intéressante car un même outil peut convenir à plusieurs "populations" différentes au sein d'une même entreprise (Développeur, Testeur, Métier...).

L'évolutivité
^^^^^^^^^^^^^

Enfin, je voulais parler d'un aspect, qui je pense est moins connu, mais qui est extrêmement puissant.
Il est possible de **modifier le cœur du fonctionnement de Robot Framework** grâce à son API et à un système de plugin [8]_.

Sans trop rentrer dans les détails techniques - car il est vrai que cet aspect est plus technique - il est possible d'intercepter et de modifier l'exécution et la manière dont Robot Framework
réalise ses actions et exécute les tests. Cela offre une multitude de possibilité et pour n'en citer qu'une, je donnerais l'exemple du plugin `robotframework-testrail <https://github.com/ATEME/robotframework-testrail>`_
qui permet de pousser les résultats d'exécutions des tests Robot Framework dans l'outil de gestion de tests `TestRail <https://www.gurock.com/testrail>`__.

Dans l'exemple ci-dessous, on a ajouté un tag avec le numéro du test qui correspond à celui du test dans TestRail (``test_case_id=1234``).
En utilisant l'API de Robot Framework, le plugin est capable de récupérer facilement ce numéro et le résultat du test puis de le publier dans TestRail :

.. code-block:: robotframework

    *** Test Cases ***
    Valid Login
        [Tags]  test_case_id=1234
        Given login page is open
        When valid username and password are inserted
        and credentials are submitted
        Then welcome page should be open

Conclusion
----------

Dans mon expérience personnelle, j'ai rencontré des tests Robot Framework dans différents domaines (Télécommunication, TV numérique, Web), sur différents types de technologie (Embarqué, API REST,
webservices, serveurs web, microservices) et programmés dans différents langages (Python, C/C++, Javascript), pour ne citer que quelques exemples que je connais.
J'ai donc pu constater la polyvalence, l'adaptabilité et les possibilités d'évolution de Robot Framework, qui font de lui un **outil générique pour automatiser les tests de Validation**.
Ce n'était pas l'objet de cet article, mais nous aurions pu ajouter bien d'**autres caractéristiques intéressantes** (lisibilité, dynamisme de la communauté, fiabilité, structure...).

Pour conclure, on peut dire que Robot Framework, ayant été réalisé **"par des testeurs"** [9]_ et **"pour des testeurs"** [10]_, est particulièrement bien adapté à eux.
C'est donc un outil de choix lorsqu'on veut faire de l'automatisation de tests.

----------------------------------------------

.. rubric:: Notes

.. [1] : Cela ne veut pas forcément dire que Robot Framework ne pourra pas être utilisé à d'autres fins et à d'autres niveaux de test bien-sûr. Je pense notamment aux tests d'API qui sont généralement situés au niveau des tests d'Intégration.

.. [2] : La possibilité de faire du RPA avec Robot Framework est une preuve supplémentaire qu'il s'inscrit bien dans une optique d'automatisation d'actions habituellement réalisées par un humain.

.. [3] : Les librairies fournies par Robot Framework sont ce qu'on appelle techniquement en Test Logiciel des `harnais de test <https://en.wikipedia.org/wiki/Test_harness>`__.

.. [4] : Le "il suffit" peut paraître un raccourci un peu trop facile. Cependant, de nos jours, de nombreuses librairies existent avec une interface en Python ou en Java. Ces langages étant nativement "lisibles" par Robot Framework, le travail d'adaptation est généralement simple.

.. [5] : KDT = Keyword Driven Testing. Voir https://latavernedutesteur.fr/2017/11/03/kdt-keyword-driven-testing/

.. [6] : BDD = Behavior Driven Development. Voir ces articles : https://latavernedutesteur.fr/tag/bdd/

.. [7] : On pourrait également ajouter l'écriture en DDT (Data Driven Testing) mais il constitue une variante du KDT

.. [8] : Voir `l'interface "Listener" <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface>`__ de Robot Framework

.. [9] : `Pekka Klarke <http://eliga.fi/>`, le créateur de Robot Framework, se définit lui-même comme un "Testeur Agile"

.. [10] : Voir à ce sujet cet `article de JP Lambert <https://jp-lambert.me/comparatif-outils-de-r%C3%A9daction-de-sp%C3%A9cifications-ex%C3%A9cutables-acd83266f273>`__
