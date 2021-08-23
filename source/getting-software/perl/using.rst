Using installed modules
=======================

Using included commands
-----------------------
If the module includes commands, those will be installed
in ``$HOME/perl5/bin``. 
This directory will be included in ``$PATH``, when you 
:ref:`configured <configure-local-lib>` local-lib.
Hence, you can start using the commands included in a 
module immediately after installation. 

For example, here is the help page of the ``fasuniq`` 
command included with the FAST package installed in the 
previous step:

.. code-block:: bash

   fasuniq -h
   Usage:
       fasuniq [options] [MULTIFASTA-FILE]

       [MULTIFASTA-DATA-ON-STDIN] | fasuniq [options]
   ...

Using modules in your scripts
-----------------------------
Modules will be installed in:

``$HOME/perl5/lib/perl5/5.30.0``.

.. note::
   
   This is the module path for Perl 5.30.0. 
   
   It you have a different version of Perl installed on 
   your system, it will change.
   
As local-lib makes these modules discoverable automatically,
you can start using them in your scripts immediately. 

Here is an example using the :term:`Bio::Phylo` package.
After installing the module with ``cpanm Bio::Phylo``, 
create a file using a text editor and copy the following 
content:

.. code-block:: perl

   use Bio::Phylo;
 
   # print version
   print Bio::Phylo->VERSION;
    
   # print citation
   print Bio::Phylo->CITATION;

Save the file as ``biophylo_test.pl`` and then run it:

.. code-block:: bash

   perl biophylo_test.pl
   
Output:

.. code-block:: console

   v2.0.1Rutger A Vos, Jason Caravas, Klaas Hartmann, Mark A Jensen and Chase Miller, 2011.
   Bio::Phylo - phyloinformatic analysis using Perl. BMC Bioinformatics 12:63.
   doi:10.1186/1471-2105-12-63

