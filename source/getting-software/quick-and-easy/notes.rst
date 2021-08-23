Notes
=====

.. index:: apt

.. _apt-install-software:

The command-line version (``apt``)
----------------------------------
You can use the :term:`apt` package manager to install
software from the command-line.

Searching for software
......................
Open a terminal to perform a search for matching
packages in the repositories.

For example, here is a search for ``pymol``

.. code-block:: bash

   apt search pymol

.. note:: You do not need to include ``sudo`` here.

This will output matching results from repositories,
if any:

.. code-block:: console
   :emphasize-lines: 1

   p   pymol           - Molecular Graphics System
   p   pymol-data      - data files for PyMOL
   p   python3-pymol   - Molecular Graphics System (Python 3 module

Once you have identified the correct package name — in
this case, it is ``pymol`` you can proceed
towards installing the package.

Installing a package
....................
You can install a package using the following command:

.. code-block:: bash

   sudo apt install pymol

.. attention::

   *You need to include sudo here.*

   Also, in the commands below, you will be asked to
   enter *your password*.
   
   You will also need to confirm if
   you would like to continue with the changes.
   Type ``y`` and then press the ``ENTER`` key to proceed.

.. code-block:: console
   :emphasize-lines: 1, 14

   [sudo] password for user:
   Reading package lists... Done
   Building dependency tree
   Reading state information... Done
   The following additional packages will be installed:
     pymol-data python3-pymol
   The following NEW packages will be installed:
     pymol pymol-data python3-pymol
   0 upgraded, 3 newly installed, 0 to remove and 
   4 not upgraded.
   Need to get 0 B/5,192 kB of archives.
   After this operation, 19.8 MB of additional disk 
   space will be used.
   Do you want to continue? [Y/n] y

The package will now be installed.

Removing an installed package
.............................
To remove an installed package, use the command:

.. code-block:: bash

   sudo apt remove pymol

The command above does not remove dependent packages.
You can remove them using:

.. code-block:: bash

   sudo apt autoremove

Updating packages
.................
To update *all installed packages*, you can use these
commands:

.. code-block:: bash

   sudo apt update
   sudo apt upgrade

To update *a specific package* —
if an update is available, you can simply use
``apt install`` again:

.. code-block:: bash

   sudo apt install package_name

Why is this a quick and easy method?
------------------------------------
You can use a graphical user interface (Software Manager)
or the command-line (``apt``) to install software
available in Linux package repositories. 

Software installed in this manner will also be kept 
updated along with the rest of the system.

Additional software repositories
--------------------------------
It takes some time for newer versions of software to 
become available in distribution repositories.  

If your software of interest is not available or if you 
need a more recent version of the software, you could 
try installing them from these additional sources:

- :doc:`../python/index` from :term:`PyPI`
- :doc:`../perl/index` from :term:`CPAN`
- :doc:`../r/index` from :term:`CRAN` or :term:`Bioconductor`
- :doc:`Conda packages <../conda/index>` from :term:`Anaconda Cloud`

.. attention::

   Software installed using these methods, will also need 
   to be kept updated manually.

