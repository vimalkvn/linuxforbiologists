Using installed packages
========================

Where are the files installed?
------------------------------
You can use the ``pip3 show`` command with the name of the 
package to identify the path where it is installed:

.. code-block:: bash
   
   pip3 show biopython

Output:

.. code-block:: console
   :emphasize-lines: 8

   Name: biopython
   Version: 1.78
   Summary: Freely available tools for computational molecular biology.
   Home-page: https://biopython.org/
   Author: The Biopython Contributors
   Author-email: biopython@biopython.org
   License: UNKNOWN
   Location: /home/user/.local/lib/python3.8/site-packages
   Requires: numpy
   Required-by: 
   
The installation path will be listed next to the 
``Location`` keyword.

Using Python packages and modules
---------------------------------
Python packages and modules will be installed in 
``$HOME/.local/lib/python3.8/site-packages``. 

.. note::

   This is the path for Python 3.8. 
   
   If you have a different version of Python installed, 
   this value will change.

This directory will be automatically included in 
``$PYTHONPATH``. So, you can import and use installed 
packages and modules in your scripts, without any extra 
effort.

For example, here is a simple Python script to test 
BioPython installed using pip:

.. code-block:: python

   from Bio.Seq import Seq
   
   seq = Seq('ATGC')
   comp = seq.complement()
   
   print(f'The complement of {seq} is {comp}')
   
The ``Bio.Seq`` package is part of BioPython. 
Copy the code sample above and save it as 
``biopy_test.py``. Then run it from the terminal like so:

.. code-block:: bash

   python3 biopy_test.py
   
Output:

.. code-block:: console
   
   The complement of ATGC is TACG

Using included commands
-----------------------
If the package includes commands, those will be 
installed in ``$HOME/.local/bin`` directory. For these 
commands to be easily accessible, you will 
need to add this directory to ``PATH``, as mentioned under 
:ref:`requirements <local-bin-path>`.

As an example, when you install the Python package of 
:term:`cutadapt`, the ``cutadapt`` command will be installed
in ``$HOME/.local/bin``, which you can then run from a 
terminal like this:

.. code-block:: bash
   
   cutadapt --version
   
Output:

.. code-block:: console

   3.1

