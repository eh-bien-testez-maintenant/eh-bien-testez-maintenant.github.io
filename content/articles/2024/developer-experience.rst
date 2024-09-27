Expérience développeur et Qualité logicielle
============================================

:date: 2024-09-06
:author: apallier
:category: opinion
:tags: experience developpeur, developer experience, devex, DX, qualité, QA
:slug: experience-developpeur-qualite-logicielle

.. image:: {static}/images/2024-experience-developpeur-qualite-logicielle.jpg
    :width: 300px
    :align: center
    :alt: Image d'un tableau abstrait avec des carrés colorés

..
    Photo de Edward Jenner: https://www.pexels.com/fr-fr/photo/art-colore-concevoir-designer-4252895/

Je m’intéresse depuis quelques mois à l’“Expérience développeur” ou “devex” ou “DX” pour “Developer Experience”.

En résumé, la “devex” fait référence à la qualité globale des interactions et des perceptions qu'une personne qui
travaille dans le développement informatique a lorsqu’elle utilise un produit, un outil ou une plateforme de
développement.

Après avoir vu travailler un certain nombre d’équipes depuis le début de ma carrière :) je suis persuadé que la "devex"
a un impact aussi sur la qualité du produit développé. Et donc forcément, ça m’intéresse en tant que QA/Testeur.

*Voici notamment les 4 aspects de la “devex” qui me paraissent cruciaux pour la Qualité logicielle* :

Une bonne documentation
-----------------------

La qualité de la documentation est souvent un point noir des équipes de dev. Une certaine interprétation de l’Agilité
n’y a pas aidé. On a cru à tort que l’Agilité prônait le moins de documentation possible… Le paradoxe est que, dans le
développement logiciel, on passe une grande partie de notre temps à lire des informations, y compris notre propre
documentation qui n'est des fois pas toujours la meilleure :/

**Conseil** : créez une documentation de qualité, pas forcément exhaustive mais à jour et facilement accessible. Tâche
difficile mais on peut commencer par des choses simples comme nettoyer, ranger et référencer puis ensuite appliquer un
framework de documentation.

L’automatisation
----------------

L'automatisation des tâches courantes peut grandement améliorer la productivité. Je ne parle pas ici forcément que des
tests mais aussi de toutes les autres tâches comme le déploiement, les tâches administratives, le monitoring de KPI,
etc.

**Conseil** : automatisez toutes les tâches répétitives que vous pouvez. Pour cela, je conseille d’aller voir aussi du
côté du no code/low code (outils comme Make.com, Zapier, JIRA automation, Robot Framework, …)

Des outils et environnements communs
------------------------------------

La présence de templates, d’images Docker communes, de librairies de code, etc… va jouer sur la productivité et la
satisfaction globale. Pourquoi passer du temps à refaire (des fois en moins bien) ce que les collègues ont déjà fait ?

**Conseil** : observez ce qui fonctionne bien et industrialisez-le pour votre équipe (l’automatisation peut aider).
Créez des templates avec Cookiecutter, utilisez les templates de GitLab CI, JIRA, … Pour les librairies, distribuez-les
sous forme de package installable, et pour vos outils internes sous forme d’images Docker.

Support et communauté
---------------------

Dans les équipes de développement plus larges, la présence de canaux de communication thématiques ou de formations
internes permet d’arriver plus vite au niveau de connaissance nécessaire.

**Conseil** : mettez en place des canaux thématiques (code, outil, test, …) dans votre messagerie instantanée
d’entreprises. Créez des tutoriels sur les points douloureux récurrents que rencontrent les nouveaux arrivants.

Conclusion
----------

Les bénéfices de la "devex" sur la Qualité logicielle sont réels mais, soyons réalistes, la "devex" n’est pas facile à
mettre en place. Elle nécessite une vision plus large que la vision “produit” qui prédomine aujourd’hui. Elle n’est
néanmoins pas incompatible et a même pour objectif de la soutenir.
