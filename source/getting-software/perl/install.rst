Installing a Perl module
========================
Open a terminal window. 

Install the module with the ``cpanm`` command:

.. code-block:: bash
   
   cpanm FAST
   
This will install the module and its dependencies, if there
are any.

Output:

.. code-block:: console
   
   --> Working on FAST
   Fetching http://www.cpan.org/authors/id/D/DH/DHARD/FAST-1.06.tar.gz ... OK
   Configuring FAST-1.06 ... OK
   ==> Found dependencies: Bit::Vector, Sort::MergeSort, Sort::Key
   --> Working on Bit::Vector
   Fetching http://www.cpan.org/authors/id/S/ST/STBEY/Bit-Vector-7.4.tar.gz ... OK
   Configuring Bit-Vector-7.4 ... OK
   ...
   Building and testing FAST-1.06 ... OK
   Successfully installed FAST-1.06
   6 distributions installed

