``rm`` — remove files or directories
====================================
With the ``rm`` command, you can remove (or delete) files
or directories.

The basic format of the command is:

.. code-block:: bash

   rm source

A safer approach is to add the ``-iv`` options to the
command:

.. code-block:: bash

   rm -iv source

With ``-i`` (*interactive*), ``rm`` will require your
confirmation before deleting a file or directory.

``-v`` (*verbose*) will print the command's actions on
the screen.

For convenience, you can :ref:`add an alias <alias-rm>`.

.. _rm-sample-files:

Sample files
------------
To follow the examples below, you will need to:

1. Copy the following files into your home directory using
   the :doc:`cp <cp>` command:

   .. code-block:: bash

      cp -v /usr/share/dict/words ~
      cp -rv /usr/share/doc/bash ~

   ``~`` is a shortcut for home directory.

2. Create an empty directory:

   .. code-block:: bash

      mkdir empty-dir


Removing files
--------------
To remove a file, for example, the ``words`` file
copied :ref:`above <rm-sample-files>`, you can use:

.. code-block:: bash

   rm -iv words

Output:

.. code-block:: console

   rm: remove regular file 'words'? y
   removed 'words'


Removing directories
--------------------

Removing empty directories
..........................
If the directory is empty, you can remove it using the
``-d`` option:

.. code-block:: bash

   rm -d empty-dir

Alternatively, you can use the :doc:`rmdir <rmdir>`
command:

.. code-block:: bash

   rmdir empty-dir

Removing directories with content
.................................
If the directory has some content i.e., files or
subdirectories, you will need to add the ``-r`` (recursive)
option.

For example, using the ``bash`` directory copied
:ref:`above <sample-files>`:

.. code-block:: bash

   rm -ivr bash

This command will ask for your confirmation for
deleting every file in the directory and then delete it:

.. code-block:: console

   rm: descend into directory 'bash'? y
   rm: remove regular file 'bash/RBASH'? y
   removed 'bash/RBASH'
   ...
   rm: remove regular file 'bash/README.gz'? y
   removed 'bash/README.gz'
   rm: remove directory 'bash'? y
   removed directory 'bash'

Instead of ``-i``, you could use the ``-I`` option,
which will only prompt once, when removing directories
recursively:

.. code-block:: bash

   rm -Ivr bash

Output:

.. code-block:: console

   rm: remove 1 argument recursively? y
   removed 'bash/RBASH'
   ...
   removed 'bash/README.gz'
   removed directory 'bash'

If you are *completely sure* you do not need the
directory and its contents, you can *force* its removal
using the ``-f`` option:

.. code-block:: bash

   rm -vrf bash

``rm`` will delete the directory without confirmation.

Notes
-----

.. _alias-rm:

Adding an alias for ``rm``
..........................
Rather than typing ``rm -iv``, every time you need to use
the command, you can add an :ref:`alias <bash_aliases>`
for the command in your ``~/.bash_aliases`` file.

For example:

.. code-block:: bash

   alias rm='rm -iv'

Now, when you type ``rm``, you will actually be running
``rm -iv``.
