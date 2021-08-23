.. _using-conda:

Using Conda
===========
In this short guide on using Conda, I will show you how to:

1. Create an environment
2. Activate the environment 
3. Search, install and use packages — using the NCBI BLAST+ 
   program as an example
4. Remove an environment when you no longer need
   it
   
.. note::

   A `cheat sheet`_ with commonly used commands for working 
   with Conda is available from the project's website.

Creating an environment
-----------------------
To create an environment, use the 
``conda create`` command with the ``-n`` option, followed by
a name for the environment — ``blast`` in this example:

.. code:: bash

   conda create -n blast

Activating an environment
-------------------------
You can get a *list* of all environments using the command:

.. code-block:: bash

   conda envs list

To activate an environment, use the ``conda activate`` 
command with the *name* of the environment:

.. code-block:: bash

   conda activate blast

Searching, installing and using Packages
----------------------------------------
To search and install packages:

1. First, activate the environment, if you haven’t 
   done so already.
   
   To demonstrate, I will activate the ``blast`` 
   environment created earlier:

   .. code-block:: bash

      conda activate blast

2. To search for packages, open 
   `Anaconda.org <https://anaconda.org/>`_ in a browser. 
   
   Type your search term in the :guilabel:`Search Packages` 
   field and press the :guilabel:`ENTER` key 
   (:numref:`fig-324b`).

   .. _fig-324b:

   .. figure:: images/anaconda-search-blast.png
      :alt: Searching for packages on Anaconda cloud

      Searching for a package on Anaconda.org

   Alternatively, you can use the ``conda search`` command:

   .. code-block:: bash

      conda search blast
      
   This will output matching packages:

   .. code-block:: console
      :emphasize-lines: 7

      Loading channels: done
      # Name   Version           Build  Channel
      blast     2.2.31               1  bioconda
      ...
      blast      2.9.0 pl526he19e7b1_7  bioconda
      ...
      blast     2.10.1 pl526he19e7b1_2  bioconda

3. To install the package, use the ``conda install`` command 
   with the *name* and *version* number of the package.

   .. attention::
   
      You will need to use the *highest* version number
      of the program, obtained from search results. 
      Otherwise, an older version might get installed.

   .. code-block:: bash

      conda install blast==2.10.1

4. Once installed, you can start using programs included 
   with the package, for example:

   .. code-block:: bash

      (blast) user@cookbook:~$ blastn -version
      
   Output:
   
   .. code-block:: console

      blastn: 2.10.1+
       Package: blast 2.10.1, build Oct 14 2020 11:36:30

Deactivating an environment
---------------------------
When your work is complete, you can deactivate an 
environment. To do so, use the command:

.. code-block:: bash
   
   conda deactivate

Your shell prompt will change to its default state i.e., 
without the name of the Conda environment — ``(blast)`` in
this case.

Removing an environment
-----------------------
To remove an environment, when you no longer need it, use 
the command:

.. code-block:: bash

   conda remove -n blast --all
   
Here ``-n`` is used to indicate the name of environment 
you would like to remove and ``--all`` removes all packages
installed in that environment.


.. _cheat sheet: https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html
