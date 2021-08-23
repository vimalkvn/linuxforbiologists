.. _galaxy-requirements:

Check system requirements
=========================
Before running Galaxy, you will need to:

1. Install Git and Python virtualenv module
2. Check if there is enough free disk space
3. Ensure that a Conda environment is not active

Install Git and Python virtualenv module
----------------------------------------
Git is necessary for getting the latest version of
Galaxy's source code from GitHub.
Python virtualenv module is necessary to set up an
isolated virtual environment for running Galaxy.

To install them, use :term:`Software Manager` 
or :term:`apt`, and search and install the 
following packages:

1. ``git``
2. ``python3-venv``

Check free disk space
---------------------
You will need *at least* 5 GB of free disk space for
the initial setup.
More space will be needed for your analyses and for
the tools you might install from the Galaxy tool shed.

To check available disk space, you can use the
:guilabel:`Disk Usage Analyzer` application or the
:ref:`df <df>` command.

.. index:: Conda

Ensure a Conda environment is not active
----------------------------------------

.. note::

   If you are not using Conda, you can ignore
   this requirement and proceed to the next step:
      
   ``->`` :ref:`get-galaxy`

If you are using Conda, please make sure an
environment is not active before the :ref:`start-galaxy`
step.

You can deactivate an active Conda environment using
the command:

.. code-block:: bash

   conda deactivate

Although it is possible to install Galaxy using an
existing Conda installation, it is simpler to
create and use a virtual environment using
Python's venv module.

---

With all the requirements satisfied, you can proceed
towards getting the latest release of Galaxy using Git.

