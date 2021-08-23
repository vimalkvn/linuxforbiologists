Important files in home directory
=================================
.. index:: bashrc

``.bashrc``
-----------
This is the configuration file used by Bash, the default
shell for user accounts. You will mostly use this 
file, when you need to set or modify 
environment variables like ``PATH``.

.. index:: bash_aliases

.. _bash_aliases:

``.bash_aliases``
-----------------
You can use the ``.bash_aliases`` file to set aliases
for commands.

For example, here is a commonly used alias:

.. code-block:: bash

   alias l='ls -l'

This means when you type ``l`` at the command-line, the
bash shell will execute ``ls -l``, which will output a
long listing of files, instead of the default.

.. note::
   
   To learn more about the ``ls`` command, read 
   the :doc:`/command-line/commands/ls` section.

