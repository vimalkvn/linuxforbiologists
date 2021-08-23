``cp`` — copy files
===================
With the ``cp`` command, you can copy files or
directories from one place (*source*) to another
(*destination*).

Copying one file
----------------
To copy one file, use the following format:

.. code-block:: bash

   cp source_file destination

Where  ``source_file`` is the file you would like to
copy and ``destination`` can *either* be a file name or
a directory.

If destination is a file name
.............................
The copied file will have that file name.

For example:

.. code-block:: bash

   cp /usr/share/dict/words /home/user/Documents/dictionary.txt

This will copy the ``words`` file from
``/usr/share/dict/`` to ``/home/user/Documents/`` and
save it as ``dictionary.txt``.

If destination is a directory
.............................
The file will be copied *into* that directory with
the *same* file name.

For example:

.. code-block:: bash

   cp /usr/share/dict/words /home/user/Documents

This will copy the ``words`` file from
``/usr/share/dict/`` to ``/home/user/Documents/`` with
the same file name.

Copying multiple files
----------------------
To copy multiple files, use the following format:

.. code-block:: bash

   cp source_file1 source_file2 destination

Where ``source_file1`` and ``source_file2`` are the
files you would like to copy. You can have *any* number
of source files. Here, *destination* is the directory where 
you would like to copy source files into.

For example:

.. code-block:: bash

   cp /usr/share/dict/words /usr/share/dict/spanish /home/user/Documents

This will copy the ``words`` and ``spanish`` dictionary
files from ``/usr/share/dict/`` into
``/home/user/Documents``.

Copying directories
-------------------
You can copy entire directories using the ``-r``
(recursive) option.

For example:

.. code-block:: bash

   cp -r /usr/share/dict /home/user/Documents

This will copy the ``/usr/share/dict`` directory
and its contents to the ``Documents`` directory.
