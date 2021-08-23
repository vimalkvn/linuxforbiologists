Installing a package from Bioconductor
======================================
You can search the Bioconductor
`software package list <https://www.bioconductor.org/packages/release/BiocViews.html#___Software>`_
on the website (currently has 1974 packages). Once you have 
identified a package to install, you can follow the steps 
below to install it. 

I will install the :term:`edgeR` package as an example.

Install package using ``BiocManager::install()`` command
--------------------------------------------------------
1. :ref:`Start an R session <start-r-session>`.

2. :ref:`Install the BiocManager package <install-biocmanager>`. 
   This is necessary for installing R packages from 
   Bioconductor repository.
   
   .. note::
      
      You only need to do this once. 
      
      The next time you wish to install a package from 
      Bioconductor, you can proceed to step 3.

3. At the R prompt, use the ``BiocManager::install()`` 
   command with the name of the package you would like to 
   install in quotes. 

   For example:
      
   .. code-block:: r
      
      BiocManager::install("edgeR")
      
   Press the :guilabel:`ENTER` key to proceed.

   The package and its dependencies will now be downloaded, 
   compiled and installed.

   Output:

   .. code-block:: console

      Bioconductor version 3.10 (BiocManager 1.30.10), R 3.6.3 (2020-02-29)
      Installing package(s) 'BiocVersion', 'edgeR'
      also installing the dependencies ‘limma’, ‘locfit’, ‘Rcpp’
      ...
      ** testing if installed package can be loaded from temporary location
      ** checking absolute paths in shared objects and dynamic libraries
      ** testing if installed package can be loaded from final location
      ** testing if installed package keeps a record of temporary installation path
      * DONE (edgeR)
      

If there are no errors during the process, the package 
installation is successful.


