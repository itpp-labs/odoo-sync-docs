[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Source of https://odoo-sync.sh website

# Roadmap
* TODO: automate publishing github pages
* TODO: demonstrate direct odoo 2 telegram integration (without lambda):

  * rename existing page https://odoo-sync.sh/odoo2x/odoo2telegram/documentation.html to odoo2telegram-via-lambda
  * use name odoo2telegram for the new page
* To demonstrate odoo2odoo integrations use following example: create note in second odoo when task is deleted in the first odoo

# How to contribute

## Initialization

* Fork this repo
* Clone to your machine
* Install dependencies:

      sudo pip install sphinx sphinx-autobuild
      sudo pip install alabaster
      sudo pip install git+https://github.com/sphinx-contrib/video


## Contribution

* Edit files in the repo. Check documentations:

  * http://www.sphinx-doc.org/en/stable/rest.html
  * http://www.sphinx-doc.org/en/stable/domains.html
  * http://www.sphinx-doc.org/en/stable/markup/index.html

* Try it out:

      cd /path/to/odoo-test/doc-src
      make html

      # (check warningn and errors in compilation logs and fix them if needed)

      # open result
      google-chrome _build/html/index.html

* To publish:

      cd /path/to/odoo-test/doc-src
      make github
      
* Make commits, push, create Pull Request
