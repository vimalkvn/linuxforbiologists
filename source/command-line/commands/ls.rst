``ls`` — list files
===================
To list files in a directory, use the ``ls`` command:

.. code-block:: bash

   ls

Output:

.. code-block:: console

   Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos


Listing hidden files
--------------------
You can provide additional options to ``ls``. 
It will change how the command works.

For example, to display hidden files and directories
too, use:

.. code-block:: bash

   ls -a

Output:

.. code-block:: console

   .              .cache     Downloads    .local    Public
   ..             .cinnamon  .gnupg       .bash_history  .config
   .bash_logout   Desktop    Pictures     .var      Videos
   .bashrc        Documents  .linuxmint   .profile  .Xauthority

Getting a detailed file listing
-------------------------------
To get a detailed listing of files, use:

.. code-block:: bash

   ls -l

Output:

.. code-block:: console

   total 32
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Desktop
   drwxr-xr-x 2 user user 4096 Mar  4 11:41 Documents
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Downloads
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Music
   drwxr-xr-x 2 user user 4096 Mar  4 11:27 Pictures
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Public
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Templates
   drwxr-xr-x 2 user user 4096 Feb 17 11:13 Videos


Combining multiple options
--------------------------
You can combine multiple options like this:

.. code-block:: bash

   ls -la

Output:

.. code-block:: console

   total 144
   drwxr-xr-x 19 user user  4096 Mar 12 10:00 .
   drwxr-xr-x  3 root root  4096 Feb 17 10:51 ..
   -rw-------  1 user user   190 Mar  4 10:32 .bash_history
   -rw-r--r--  1 user user   220 Feb 17 10:51 .bash_logout
   -rw-r--r--  1 user user  3771 Feb 17 10:51 .bashrc
   drwx------ 17 user user  4096 Mar  3 19:28 .cache
   drwxrwxr-x  4 user user  4096 Feb 17 11:40 .cinnamon

To see the list of all options that ``ls`` supports, use:

.. code-block:: bash

   ls --help
