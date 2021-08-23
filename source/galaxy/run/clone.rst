.. _get-galaxy:

Getting the latest release of Galaxy
====================================
Create a directory to set up Galaxy and change into it:

.. code-block:: bash

   mkdir ~/programs
   cd ~/programs

Here ``~`` is a shortcut for your home directory.

.. note::

   This directory is not specific for Galaxy.
   
   You can use it for installing or storing other 
   programs too.

.. index:: Git

Get the latest release of Galaxy from the project's
repository on GitHub. The latest release at the time
of this writing is :guilabel:`21.01`.

You can get (or clone) the repository using
the ``git clone`` command:

.. code-block:: bash

   git clone -b release_21.01 https://github.com/galaxyproject/galaxy.git

The ``-b`` option of ``git clone``, checks out the
specified Git branch — ``release_21.01`` in this case.

Output:

.. code-block:: console

   Cloning into 'galaxy'...
   remote: Enumerating objects: 364, done.
   remote: Counting objects: 100% (364/364), done.
   remote: Compressing objects: 100% (232/232), done.
   remote: Total 497693 (delta 184), reused 237 (delta 131), pack-reused 497329
   Receiving objects: 100% (497693/497693), 520.44 MiB | 3.89 MiB/s, done.
   Resolving deltas: 100% (391502/391502), done.
   Updating files: 100% (5826/5826), done.

This will take some time depending on your
network connection.
Once complete, you will find a directory named
``galaxy`` in the current directory.

Next, you will need to create a Python virtual 
environment.

