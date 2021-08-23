.. _find-command:

``find`` — search for files
===========================
Search for files using their file name, file type etc.,

For example, to find files in the home directory with 
``.bash`` in their name, use the command:

.. code-block:: bash

   find ~ -name ".bash*"
   
Output:

.. code-block:: console

   /home/user/.bashrc
   /home/user/.bash_history
   /home/user/.bash_logout
   
.. note::

   The ``~`` here is a shortcut for home directory.
   
   The asterisk symbol (``*``) in ``.bash*`` acts as a 
   wildcard.
   
   The ``find`` command does not use a database, so 
   the search will be slower when compared to 
   ``locate``. However, it can identify files 
   that were created or modified recently.
  

