
.. _installing-pypi-package:

Installing a Python package
===========================
Open a terminal. 

Use the ``pip3 install`` command with
by the name of the package, you would like to install.

Using biopython as an example:

.. code-block:: bash

   pip3 install biopython
   
Output:
   
.. code-block:: console

    Collecting biopython
     Downloading biopython-1.78-cp38-cp38-manylinux1_x86_64.whl (2.3 MB)
        |********************************| 2.3 MB 2.1 MB/s
   Collecting numpy
     Downloading numpy-1.20.1-cp38-cp38-manylinux2010_x86_64.whl (15.4 MB)
        |********************************| 15.4 MB 90 kB/s
   Installing collected packages: numpy, biopython
   Successfully installed biopython-1.78 numpy-1.20.1

.. note::
   
   One limitation of this method is that, 
   you will not be able to install *multiple versions* of 
   a package. This can be solved using a 
   :ref:`virtual environment <virtualenv>`.
      
