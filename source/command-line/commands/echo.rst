``echo`` — display text or values of variables
==============================================
With the ``echo`` command, you can print text or
the values of *environment variables* on the screen.

The basic format of the command is:

.. code-block:: bash

   echo text_or_variable

Printing text
-------------
To print text on the screen, use ``echo`` followed by
the text you would like to display.

.. code-block:: bash

   echo "Hello, This is echo!"

Output:

.. code-block:: console

   Hello, This is echo!

Printing values of environment variables
----------------------------------------
You can also use ``echo`` to display values of your
environment variables.

For example:

.. code-block:: bash

   echo $PATH

The ``$`` in ``PATH`` indicates, it is a variable.

Output:

.. code-block:: console

   /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

``PATH`` contains the list of paths (directories) that will
be searched for locating programs or commands.

You can set or modify environment variables in your
``~/.bashrc``.
