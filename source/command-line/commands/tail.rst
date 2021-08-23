``tail`` — print last few lines of a file
=========================================
With the ``tail`` command, you can view the last few
(default: 10) lines of a file.

For example:

.. code-block:: bash

   tail /usr/share/dict/words

.. code-block:: console

   élan's
   émigré
   émigré's
   émigrés
   épée
   épée's
   épées
   étude
   étude's
   études

The ``tail`` and the ``head`` command discussed
:doc:`earlier <head>`,
are useful when you want to quickly view the
contents of a *large* text file.

In both cases, you can control the *number of lines*
displayed, using the ``-n`` option, instead of the
default value (10).

For example:

.. code-block:: bash

   tail -n 5 /usr/share/dict/words

will display the last 5 lines of the file.
