.. _virtualenv:
   
Python virtual environments
===========================
A virtual environment is a *self-contained* directory 
tree containing Python and some additional packages. 

Advantages
----------
These are *some* advantages of using virtual 
environments.

No administrator privileges
...........................
You do not need administrator privileges
to create a virtual environment or install packages in 
an environment.

Multiple environments
.....................
Multiple virtual environments can be created with  
each containing their own sets of packages. 

These are isolated and packages in an environment can be 
installed, updated or removed without affecting other 
environments.

Share your environment
......................
You can share your configuration with others. They 
will be able to reproduce your environment, with the 
exact versions of packages.

.. _create-virtualenv:

Creating a virtual environment
------------------------------
First, using :doc:`../quick-and-easy/index`, search and 
install the ``python3-venv`` package. This includes the 
``venv`` module necessary for creating virtual environments.

You can create a virtual environment in any directory 
where you have write privileges, for example, your 
home directory.

To demonstrate, I will create a virtual environment called
``py3env`` in my home directory.

.. code-block:: bash

   python3 -m venv py3env

If successful, you will find a directory named ``py3env`` 
in the current directory. No messages will be displayed.

.. note::

   ``python3`` is the command to run the Python 3
   interpreter. Its complete path is ``/usr/bin/python3``.
   
   ``venv`` is the Python module to create virtual 
   environments.
   
   The ``-m`` option runs the ``venv`` module as a script.

Before you can use a virtual environment, you will need to 
activate it.

Activating a virtual environment
--------------------------------
You will need to activate a virtual environment before you
can start using it. To do so, use the ``source`` command 
with the path to the virtual environment's ``activate`` 
script.

For example, to activate ``py3env`` created in the
:ref:`previous step <create-virtualenv>`, use:

.. code-block:: bash

   source py3env/bin/activate

Your shell prompt will now change to indicate that
the virtual environment is now active.
Note the ``(py3env)`` label at the beginning of the
prompt:

.. code-block:: bash

   (py3env) user@cookbook:~$
   
You can now start using this virtual environment.

.. note::
   
   *Before you start installing packages...*
   
   It is a good idea to install (or upgrade) 
   Python build tools — :term:`pip`, 
   :term:`setuptools`, and :term:`wheel` in a new 
   virtual environment.
   
   These build tools are necessary for building and 
   installing packages from :term:`PyPI` and other 
   sources.
   
   Installing them will ensure that additional packages
   will build and install without errors.

Installing Python build tools
-----------------------------
Use ``pip3 install`` to install or upgrade the
required packages:

.. code-block:: bash

   pip3 install -U pip setuptools wheel

The ``-U`` option of ``pip3 install``, will upgrade
listed packages, if newer versions are available.

Output:

.. code-block:: console

   Collecting pip
   Downloading pip-21.0.1-py3-none-any.whl (1.5 MB)
   ...
   Installing collected packages: pip, setuptools, wheel
   ...
   Successfully installed pip-21.0.1 setuptools-54.2.0 wheel-0.36.2


Deactivating a virtual environment
----------------------------------
To exit a virtual environment, use the command:

.. code-block:: bash

   deactivate

Your shell prompt will change to its original
appearance:

.. code-block:: bash

   user@cookbook:~$

