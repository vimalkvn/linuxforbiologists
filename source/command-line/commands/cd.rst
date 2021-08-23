``cd`` — change directory
=========================
To change into a directory, use ``cd``
followed by the name of that directory.

For example, to change into ``/home/user/Downloads``,
use:

.. code-block:: bash

   cd Downloads

.. note::

   When you log in or open a new terminal window, you
   will be placed in your home directory —
   ``/home/user``, where ``user`` is your username.

You can verify your current directory using the
``pwd`` command discussed :ref:`earlier <pwd>`:

.. code-block:: bash

   pwd

.. code-block:: console

   /home/user/Downloads

``cd`` with no arguments
------------------------
No matter where you are in the file system, typing
``cd`` *without any arguments* will take you to your
home directory.

.. code-block:: bash

   user@cookbook:/usr/share/dict$ cd
   user@cookbook:~$

Go to parent directory
----------------------
Use ``cd ..`` to go to the parent directory.

For example, when you are in ``/home/user/Downloads``
and type:

.. code-block:: bash

   cd ..

You will be taken to ``/home/user``.

A single dot (``.``) refers to the *current* directory.
