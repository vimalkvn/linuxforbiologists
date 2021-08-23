Notes
=====

You will need to update these packages manually
-----------------------------------------------
Packages installed in this manner should also be updated 
manually. 

When you notice there is an update for the 
package, for example, from the project's website or from 
their source code repository, follow the steps in 
:ref:`update-python-package` to install the 
latest version.

.. _why-pip3:
   
Why pip3 and not pip?
---------------------
The :term:`pip` package includes the following commands:

* ``pip3`` — Python 3 version 
* ``pip`` — Python 2 version

*Support for Python 2 ended in January 2020.*

Since there is a possibility for both commands to exist on 
a system, it is safer to use ``pip3`` when installing 
packages using this method.

What about programs written in Python 2?
----------------------------------------
*Support for Python 2 ended in January 2020.*

If you do need to use a program written only in Python 2, 
you can create an isolated environment — either using 
Python venv or Conda and then install the package there. 

Related sections:

* :ref:`virtualenv`
* :doc:`../conda/index`

.. _when-virtualenv:

When should I use a virtual environment?
----------------------------------------
The method described here will not work if the programs 
you are installing require two different versions of the
same package from PyPI.

In that case, you can consider creating an isolated 
environment — either using Python virtualenv or Conda and then 
installing the packages there. 

Related sections:

* :ref:`virtualenv`
* :doc:`../conda/index`

Older versions of pip
---------------------
If the version of pip installed in your system is older 
than 20.0, it will attempt to install packages in system
paths by default, resulting in *permission denied* errors.

To avoid that, you will need to add the ``--user`` option to
the ``install`` and ``uninstall`` commands, for example:

.. code-block:: bash

   pip3 install --user biopython

A better approach is to *upgrade* your local version of pip.
Once upgraded, you will no longer need to user ``--user``.

To upgrade pip, do:

.. code-block:: bash

   pip3 install --user -U pip
   

You can check the installed version of pip using:

.. code-block:: bash

   pip3 -V

