``mv`` — move a file or directory
=================================
With the ``mv`` command, you can move a file or directory
from one location (source) to another (destination).
You can choose to keep the existing file or directory
name or rename them.

The basic format of the command is:

.. code-block:: bash

   mv source destination

A safer approach is to add the ``-iv`` options to the
command:

.. code-block:: bash

   mv -iv source destination

With ``-i`` (*interactive*), ``mv`` will require your
confirmation before overwriting a file or directory,
if it exists already in destination.

``-v`` (*verbose*) will print the command's actions on
the screen.

For convenience, you can :ref:`add an alias <alias-mv>`.

.. _sample-files:

Sample files
------------
To follow the examples below, you will need to copy
the following files into your home directory using the
:doc:`cp <cp>` command:

.. code-block:: bash

   cp -v /usr/share/dict/words ~
   cp -rv /usr/share/doc/bash ~

``~`` is a shortcut for home directory.


Moving a file or directory
--------------------------
The simplest use case is to move a file or
directory from one location (directory) to another.

Moving a File
.............
For example, to move the ``words`` file copied
:ref:`above <sample-files>` into your ``Documents``
directory, use:

.. code-block:: bash

   mv -iv words Documents/

Output:

.. code-block:: console

   renamed 'words' -> 'Documents/words'

Moving a directory
..................
Similarly, to move the ``bash`` directory copied
:ref:`above <sample-files>` into your ``Documents``
directory, use:

.. code-block:: bash

   mv -iv bash Documents/

Output:

.. code-block:: console

   renamed 'bash' -> 'Documents/bash'

In both cases, the file or directory name will not be
changed.

Renaming a file or directory
----------------------------
In this case, you would like to rename a file or directory.

Renaming a file
...............
To rename the ``words`` file copied
:ref:`above <sample-files>` to ``dictionary.txt``, use:

.. code-block:: bash

   mv -iv words dictionary.txt

Alternatively, to move it into your ``Documents``
directory and rename it at the same time, use:

.. code-block:: bash

   mv -iv words Documents/dictionary.txt

Renaming a directory
....................
To rename the ``bash`` directory copied
:ref:`above <sample-files>` into ``bash-commands``, use:

.. code-block:: bash

   mv -iv bash bash-commands

Notes
-----

What happens if a file exists?
..............................
You will notice a prompt requesting you for confirmation
to overwrite the file.

Type ``y`` and press the :guilabel:`ENTER` key to proceed:

.. code-block:: console

   mv: overwrite 'Documents/words'? y
   renamed 'words' -> 'Documents/words'

To cancel, simply press :guilabel:`ENTER` key at the prompt.


What happens if a directory exists?
...................................
``mv`` will overwrite a directory only if it is empty.
You can either:

- :doc:`copy <cp>` files into destination directory or
- rename the destination directory

.. _alias-mv:

Adding an alias for ``mv``
..........................
Rather than typing ``mv -iv``, every time you need to use
the command, you can add an :ref:`alias <bash_aliases>`
for the command in your ``~/.bash_aliases`` file.

For example:

.. code-block:: bash

   alias mv='mv -iv'

Now, when you type ``mv``, you will actually be running
``mv -iv``.
