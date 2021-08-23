Installing Conda
================
A minimal installation of Conda can be setup by installing 
:term:`Miniconda`. You will need to download and run the
Miniconda installer following the steps below.

1. Downloading Miniconda
------------------------
To download the correct version of Miniconda:

1. Open the Conda downloads_ page in a browser.
2. Navigate to the :guilabel:`Linux installers` section
   (:numref:`fig-324a`)
   
   .. _fig-324a:

   .. figure:: images/miniconda-installers.png
      :alt: Miniconda installers for Linux
      
      Miniconda installers for Linux

3. Click on the download link corresponding to:
 
   :guilabel:`Python 3.8 — Miniconda3 Linux 64-bit`
   
   Save the file. It will be saved as:

   ``Miniconda3-latest-Linux-x86_64.sh``

   .. note::

      You can verify the file's SHA256 checksum to
      ensure it has been downloaded correctly.
      :ref:`How? <verify-sha256sum>`

2. Running the installer
------------------------

Run the installer using the ``bash`` command:

.. code-block:: bash

   bash Miniconda3-latest-Linux-x86_64.sh

This will print a welcome message:

.. code-block:: console

   Welcome to Miniconda3 py38_4.8.3

   In order to continue the installation process, please 
   review the license agreement.
   Please, press ENTER to continue

3. Reviewing licence agreement
------------------------------

Press the :guilabel:`ENTER` key to view the licence agreement. 
Scroll down to read the licence. Towards the end,  you will 
notice a prompt:

.. code-block:: console

   Do you accept the license terms? [yes|no]
   [no] >>> yes

You will need to type *yes* to accept the agreement and 
then press the :guilabel:`ENTER` key to proceed.

4. Confirming Miniconda install location
----------------------------------------

Next, you will be asked to provide a path to install 
Miniconda.

.. code-block:: console

   Miniconda3 will now be installed into this location:
   /home/user/miniconda3

     - Press ENTER to confirm the location
     - Press CTRL-C to abort the installation
     - Or specify a different location below

   [/home/user/miniconda3] >>> 

Press :guilabel:`ENTER` here to accept the default value.

Installation will now proceed.
When complete, you will notice a prompt asking if you would 
like to *initialize Miniconda 3*.

.. code-block:: console

   Do you wish the installer to initialize Miniconda3
   by running conda init? [yes|no]
   [no] >>> yes

Type ``yes`` and then press the :guilabel:`ENTER` key.
This will add the ``conda`` command to your 
``$PATH``. 

As a result of this configuration, Conda ``base`` 
environment will be activated automatically when you 
open a terminal session. 
This can be disabled in the next step. 
:ref:`Why? <why-disable-auto-activate>`

5. Disabling auto-activation of base environment
------------------------------------------------
Open a new terminal. Your shell prompt should now appear 
like the following:

.. code:: bash

   (base) user@cookbook:~$ 

The ``(base)`` label at the beginning of the prompt, 
indicates that Conda base environment is now active.

To disable this behaviour, so you can activate the 
environment manually when you need it, run the 
following command:

.. code:: bash

   conda config --set auto_activate_base false

6. Setting up channels
----------------------

Channels provide additional software for Conda.

Conda's configuration includes a defaults_ channel.
The :term:`bioconda` and conda-forge_ channels can also be
added to access an even larger collection of software. 
The bioconda channel, for example, provides over 7000 
packages of Bioinformatics software.

To add these channels to your configuration, you can run 
the commands below.

.. attention::

   *You will need to run these commands in the same
   order as given below.*

.. code:: bash

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   
---

Installation and configuration of Conda is now complete. 

You can now start using Conda to create environments and 
install packages from repositories.



.. _conda-forge: https://conda-forge.org/
.. _defaults: https://repo.anaconda.com/pkgs
.. _bioconda: https://bioconda.github.io/

.. _Miniconda: 
.. _downloads: https://docs.conda.io/en/latest/miniconda.html

