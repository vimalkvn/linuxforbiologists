Notes
=====
  
The r-base-dev and build-essential packages
-------------------------------------------
If you are installing additional packages from CRAN and 
other sources, you will also need to install the 
``r-base-dev`` and ``build-essential`` packages.
However, when you install ``r-base``, these packages 
will also be installed as dependencies so, you do not 
have to install them manually.

.. _why-use-personal-lib:

Why use a personal library?
---------------------------
When installing packages, R will first attempt to use a 
system library — for example, ``/usr/local/lib/R/site-library``.
This path can only be modified by a user
with administrator privileges. This is why a personal
library in the ``$HOME`` directory is a better option for 
users to install packages.
