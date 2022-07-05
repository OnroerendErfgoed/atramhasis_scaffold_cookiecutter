==================
atramhasis project
==================

Create your own Atramhasis implementation

Requirements
------------

*   Python 3.6+
*   npm
*   `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

#.  Generate an atramhasis project. To create a project from a specific cookiecutter branch/release you can checkout a specific branch/release

    .. code-block:: bash

        cookiecutter gh:OnroerendErfgoed/atramhasis_scaffold_cookiecutter --checkout develop
 

#.  Create a virtual environment, change dir to project folder and install requirements

    .. code-block:: bash
        
        cd atramhasis_app
        python -m venv $HOME/.virtualenvs/atramhasis_app
        source $HOME/.virtualenvs/atramhasis_app/bin/activate
        pip install -r requirements-dev.txt
        pip install -e .

#.  Setup database

    .. code-block:: bash

        alembic upgrade head

#.  install frontend requirements

    .. code-block:: bash

        cd <package-name>/static
        npm install

#.  Run server

    .. code-block:: bash

        cd <root of repo>
        pserve development.ini
