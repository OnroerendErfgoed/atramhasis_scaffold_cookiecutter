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

#.  Generate an atramhasis project.

    .. code-block:: bash

        cd <parent folder for new repo>
        cookiecutter gh:OnroerendErfgoed/atramhasis_scaffold_cookiecutter

#.  Create a virtual environment and install requirements

    .. code-block:: bash

        # create a new virtual environment for the project, fe python -m venv $HOME/.virtualenvs/atramhasis_app_venv
        # Activate the virtual environment, f.e.source $HOME/.virtualenvs/atramhasis_app_venv/bin/activate
        # Change directory into your newly created project if not already there.
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
