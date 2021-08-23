Notes
=====
.. _verify-sha256sum:

How to verify the installer's SHA256 checksum
---------------------------------------------
1. Navigate to the folder containing the installer 
   file — ``Miniconda3-latest-Linux-x86_64.sh``:
   
   .. code-block:: bash
      
      cd Downloads

2. Use the ``sha256sum`` command to verify the 
   SHA256 checksum of the file:

   .. code-block:: bash
      
      sha256sum Miniconda3-latest-Linux-x86_64.sh
   
   Output:
   
   .. code-block:: console
   
      879457af6a0bf5b34b48c12de31d4df0ee2f06a8e68768e5758c3293b2daf688  Miniconda3-latest-Linux-x86_64.sh

The output of the ``sha256sum`` command should match the 
value listed on the downloads page.

.. _why-disable-auto-activate:

Why disable auto-activation of base environment?
------------------------------------------------
If you are installing packages using other methods, for 
example :ref:`installing-pypi-package` from PyPI, there is 
a possibility that you might *accidentally* install the 
package in Conda ``base`` environment instead of the 
intended location.

Even if you disable auto-activation of the ``base`` 
environment, you can activate it using the 
``conda activate base`` command, when you need it.
  
.. Links

.. _Anaconda: https://docs.continuum.io/anaconda/
.. _Anaconda Cloud: https://anaconda.org


.. _Conda: https://conda.io



