``locate`` — find files using their names
=========================================
Search for files using their file names.
This method is quick as it uses a file name database.

For example:

.. code-block:: bash

   locate bashrc
   
Output:

.. code-block:: console

   /etc/bash.bashrc
   /etc/skel/.bashrc
   /home/user/.bashrc
   ...

.. note::
   
   This method might not find files that were created or 
   modified recently.
    
   Newer files might not yet be included in the database.   
   To update the database manually, you can run the 
   command:
   
   .. code-block:: bash
   
      sudo updatedb
      
   Alternatively, you can use the 
   :ref:`find <find-command>` command to search for new 
   files.

