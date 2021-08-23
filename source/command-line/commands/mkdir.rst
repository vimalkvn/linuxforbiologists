``mkdir`` — create new directory
================================
Use ``mkdir`` followed by the name of the
directory you would like to create:

.. code-block:: bash

   mkdir Workspace

.. attention::

   *The directory you're creating must not already exist
   or this command will not work.*

As discussed :ref:`earlier <case-sensitive>`, directory
names are case-sensitive, so a directory named
``Workspace`` is different from another named
``workspace``.


Spaces in directory names
-------------------------
If there are spaces in the directory name, use
double quotes, for example:

.. code-block:: bash

   mkdir "Project Work"

Without that, two separate directories — Project
and Work will be created.
