Conventions pour les messages de commit sous Git
################################################

:date: 2024-05-13
:author: apallier
:category: revue
:tags: code, git
:slug: conventions-messages-commit-git

.. image:: {static}/images/2024-conventions-messages-commit.jpg
   :width: 300px
   :align: center
   :alt: Image d'un bloc-note avec une main qui tient un crayon

.. Photo de Karolina Grabowska: https://www.pexels.com/fr-fr/photo/cahier-bureau-stylo-ecrite-4195401/

Est-ce que vous pensez aussi que les messages de commit dans Git font partie de la qualité d’un logiciel au sens
large ?

J’ai creusé un peu la question ces derniers temps et je présente ici un résumé des différentes conventions que j’ai
trouvées pour les messages de commit sous Git.

|

1. Les Conventional Commits
---------------------------

Sûrement le plus connu, "Conventional Commits" propose un standard pour la création de messages de commit,
avec des préfixes définis tels que “feat” (pour les nouvelles fonctionnalités), “fix” (pour les corrections de bugs),
“chore” (pour les tâches de maintenance), etc.

* Site Web : https://www.conventionalcommits.org
* Outils qui permettent de générer les messages de commit
    * `better-commit <https://github.com/Everduin94/better-commits>`_
    * `Commitizen <https://github.com/commitizen/cz-cli>`_

* Linter de message : `Commitlint <https://github.com/conventional-changelog/commitlint>`_

Exemple de message de type commit :

.. code-block:: text

    fix(api): prevent racing of requests

    Introduce a request id and a reference to latest request. Dismiss
    incoming responses other than from latest request.

    Remove timeouts which were used to mitigate the racing issue but are
    obsolete now.

    Reviewed-by: ABC
    Refs: #123


2. La Convention Angular
------------------------

Il me semble que les “Conventional commits” viennent d’Angular qui a développé ses propres directives de messages de
commit. Ces directives recommandent un format structuré pour les messages de commit, en utilisant des en-têtes avec
des mots-clés spécifiques pour indiquer le type de changement.

* GitHub Repository : https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit

Résumé de l'en-tête de la Convention Angular :

.. code-block:: text

    <type>(<scope>): <short summary>
      │       │             │
      │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
      │       │
      │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
      │                          elements|forms|http|language-service|localize|platform-browser|
      │                          platform-browser-dynamic|platform-server|router|service-worker|
      │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|
      │                          devtools
      │
      └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test


3. Gitmoji
----------

Gitmoji propose une approche plus ludique pour ajouter des émojis aux messages de commit afin d'indiquer le type de
changement introduit par le commit. Chaque emoji a une signification spécifique (comme 🐛 pour les corrections de bugs,
✨ pour les nouvelles fonctionnalités, etc.), ce qui rend les messages de commit plus visuels et expressifs.

* Site web : https://gitmoji.dev/

Exemples de messages de commit avec Gitmoji :

.. code-block:: text

    🏗️ Transform project into a monorepo (#1235)
    * 🏗️ Define monorepo architecture
    * 🚚 Extract `gitmojis` as an isolated package
    * 🚚 Extract `website` as an isolated package
    * 🚚 Clean-up root package.json
    * ➕ Install `turbo`
    * 🔧 Setup turborepo
    * 👷 Use `turbo` in `ci` workflow
    * 👷 Update `npm-publish` workflow with `turbo`
    * ♻️ Migrate yarn from `classic` to `berry`
    * 📝 Update contributing guide
    * 🎨 Update readme
    * 📝 Add readme file for `gitmojis` package
    * 🚚 Move `public` folder to `website` package


4. La convention Atom
---------------------

Bien que l'éditeur Atom ne soit plus maintenu, il avait créé un guide pour les messages de commit qui a
l'intérêt d'être très concis.

* GitHub Repository : https://github.com/atom/atom/blob/master/CONTRIBUTING.md#git-commit-messages


.. note::
    Pour l'anecdote, on peut noter que
    `la Commission Européenne <https://ec.europa.eu/component-library/v1.15.0/eu/docs/conventions/git/>`_
    utilise la convention "Angular" pour les messages de commit dans ses projets.


Conclusion
----------

Il existe plusieurs conventions pour les messages de commit sous Git. La "Conventional Commit Convention" semble être
une référence aujourd'hui.

L'adoption d'une convention pour les messages de commit dans un projet Git améliore la traçabilité du développement,
favorise la cohérence au sein de l'équipe, et facilite l'automatisation de certaines tâches liées à la gestion du code
source et permet de créer de l'outillage.

Bref, c'est un outil au service de la Qualité logicielle.
