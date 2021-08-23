.. _install-from-cran:

Installing a package from CRAN
==============================
You can search for R packages on CRAN by consulting the 
`Task Views <https://cran.r-project.org/web/views/>`_ for
a categorized listing or the 
`Table of available packages <https://cran.r-project.org/web/packages/available_packages_by_name.html>`_
(currently 17157 packages). 
Once you have identified a package to install, you can 
follow the steps below to install it. 

.. _install-biocmanager:

I will install the :term:`BiocManager` package as an
example below.

1. Install package using ``install.packages()`` command
-------------------------------------------------------
:ref:`Start an R session <start-r-session>`. 

At the prompt, type the ``install.packages()`` command 
with the name of the package in quotes. For example:
   
.. code-block:: r
   
   install.packages("BiocManager")
   
Press the :guilabel:`ENTER` key to proceed.
   
2. Confirm use of personal library
----------------------------------
You will notice a prompt requesting you to confirm if 
you would like to use a personal library:
  
.. code-block:: console

   Installing package into ‘/usr/local/lib/R/site-library’
   (as ‘lib’ is unspecified)
   Warning in install.packages("BiocManager") :
   'lib = "/usr/local/lib/R/site-library"' is not writable
   Would you like to use a personal library instead? (yes/No/cancel) yes
      
Type ``yes`` to confirm and press the :guilabel:`ENTER` key. 
:ref:`why-use-personal-lib`.

3. Create personal library if necessary
---------------------------------------
If you have never installed a package, the personal library 
directory will not exist. If so, you will be prompted for 
confirmation to create it: 

.. code-block:: console

   Would you like to create a personal library
   ‘~/R/x86_64-pc-linux-gnu-library/3.6’
   to install packages into? (yes/No/cancel) yes
   
Type ``yes`` to confirm and press the :guilabel:`ENTER` 
key.

.. note::

   The next time you install a package, you will not see 
   this prompt.

4. Package installation summary
-------------------------------
Installation should now proceed:
   
.. code-block:: console

   trying URL 'https://cloud.r-project.org/src/contrib/BiocManager_1.30.10.tar.gz'
   Content type 'application/x-gzip' length 40205 bytes (39 KB)
   ==================================================
   downloaded 39 KB

   * installing *source* package ‘BiocManager’ ...
   ** package ‘BiocManager’ successfully unpacked and MD5 sums checked
   ** using staged installation
   ** R
   ** inst
   ** byte-compile and prepare package for lazy loading
   ** help
   *** installing help indices
   ** building package indices
   ** installing vignettes
   ** testing if installed package can be loaded from temporary location
   ** testing if installed package can be loaded from final location
   ** testing if installed package keeps a record of temporary installation path
   * DONE (BiocManager)

   The downloaded source packages are in
      ‘/tmp/RtmpDgmOZ8/downloaded_packages’
   > 

If there are no errors during the process, the package 
installation is successful.

