Notes
=====

.. _adding-directories-to-path:

Adding directories to PATH
--------------------------
The ``PATH`` variable stores the list of directories that 
will be searched to locate commands you type. 
If you have a :term:`command <commands>` that is stored in a
directory that is not on this list, you will need to add 
it to ``PATH``.

You can display the current value of ``PATH`` using the 
:doc:`echo <commands/echo>` command:

.. code-block:: bash

   echo $PATH
   
Output:

.. code-block:: console

   /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   
To modify ``PATH`` and add a directory, you can follow the 
steps below. This example adds ``/home/user/.local/bin`` 
to ``PATH``.

.. attention::

   *You will need to be careful while editing PATH*.
   
   You will also need to ensure that it includes ``$PATH``
   in the list. Otherwise, you will not be able to 
   access any commands!

1. Open ``$HOME/.bashrc`` in a :term:`text editor`.

2. Add the following lines at the end of the file. 
   Add the directory you wish to add separated by
   a colon. The list should end in ``$PATH``.

   .. code-block:: bash

      PATH=/home/user/.local/bin:$PATH
      export PATH
      
   .. note::
      
      If a line with ``PATH`` exists already in the file, 
      update it instead.
3. Verify the change using ``echo``:

   .. code-block:: bash
   
      echo $PATH
      
   Output:
   
   .. code-block:: console
   
      /home/user/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
      
   
When you log in again or open a new terminal session, 
commands in ``/home/user/.local/bin`` will be 
accessible.

Dealing with spaces in file names
---------------------------------
When you create a new file or directory, it is a good
idea to *not use spaces* in the file or directory name.
This is especially useful while working with these files 
or directories in the command-line.
Instead, you can use an underscore 
(``_``) or hyphen (``-``) to separate words in file names.

If you do have to work with file or directory names 
containing spaces, you can use quotes around the file or 
directory name.

For example:

.. code-block:: bash

   mkdir "Sample Data"
   
To change into the ``Sample Data`` directory, use:

.. code-block:: bash

   cd "Sample Data"
   
Print current directory:

.. code-block:: bash

   pwd

Output:
   
.. code-block:: console

   /home/user/Sample Data
   
This would have been simpler if the directory name is
``sample-data``. You will not need to use quotes in that 
case.


