Sample Module Repository
========================

This simple project is an example repo for Python projects.

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

This is not the repo you are looking for
========================================

You (probably) want `the upstream repo <https://github.com/kennethreitz/samplemod>`_ instead.

Setup
======

.. highlight:: shell

Anaconda
----------

https://conda.io/docs/using/envs.html#managing-environments

::

    conda create --name envname --file requirements.txt python=3


Pipenv
-------

https://github.com/kennethreitz/pipenv

::

    pip install pipenv
    pipenv --three
    pipenv install --dev


Virtualenvwrapper
------------------

https://virtualenvwrapper.readthedocs.io/en/latest/

::

    pip install virtualenvwrapper
    export WORKON_HOME=~/venv
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv env1
    pip install -r requirements.txt


Run setup.py
==============

::

   python setup.py build
   python setup.py bdist
   python setup.py sdist
   python setup.py test
   python setup.py nosetests
   python setup.py build_sphinx
   python setup.py clean --all
   python setup.py --help-commands
