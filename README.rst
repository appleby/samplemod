Sample Module Repository
========================

This simple project is an example repo for Python projects.

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

Setup
======

Anaconda
----------

https://conda.io/docs/using/envs.html#managing-environments

.. code-block:: shell
   conda create --name envname --file requirements.txt python=3


Pipenv
-------

https://github.com/kennethreitz/pipenv

.. code-block:: shell
   pip install pipenv
   pipenv --three
   pipenv install --dev


Virtualenvwrapper
------------------

https://virtualenvwrapper.readthedocs.io/en/latest/

.. code-block:: shell
   pip install virtualenvwrapper
   export WORKON_HOME=~/venv
   mkdir -p $WORKON_HOME
   source /usr/local/bin/virtualenvwrapper.sh
   mkvirtualenv env1
   pip install -r requirements.txt
