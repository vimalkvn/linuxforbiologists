.. index:: Python, venv, pip, setuptools, wheel

.. _galaxy-create-venv:

Creating a Python virtual environment
=====================================
In this step, you will use Python 3 ``venv`` module to
create an isolated virtual environment for Galaxy.

.. note::

   For a detailed guide on creating and using 
   virtual environments, read:
   
   ``->`` :ref:`virtualenv`

To create the virtual environment:

1. Change into the ``galaxy`` directory:
   
   .. code-block:: bash

      cd galaxy

2. Create virtual environment using ``.venv`` as the 
   name.

   .. code-block:: bash

      python3 -m venv .venv
   
   .. attention::
      
      The dot (``.``) in ``.venv``, is important.
  
3. Activate the virtual environment:

   .. code-block:: bash

      source .venv/bin/activate
      
   Your shell prompt will now change to include 
   ``(.venv)``:

   .. code-block:: bash
      
      (.venv) user@cookbook:~/programs/galaxy$

4. Install or upgrade Python build tools:

   .. code-block:: bash

      pip3 install -U pip setuptools wheel
   
   This step is necessary, so additional packages will 
   build and install without any issues.
   
5. Finally, exit the virtual environment:

   .. code-block:: bash

      deactivate

In the :ref:`next step <start-galaxy>`, the start-up 
script will detect this environment and use it to 
install all :term:`dependencies` necessary for running 
Galaxy.

