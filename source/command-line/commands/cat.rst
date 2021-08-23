``cat`` — display contents of files or combine them
===================================================
With the ``cat`` command, you can view the contents of a
file on the screen or combine contents of multiple files.

View contents of a file
-----------------------
To view the contents of a file, use
``cat``, followed by the name of the file:

.. code-block:: bash

   cat /usr/share/dict/words

.. code-block:: console

   A
   A's
   AMD
   AMD's
   AOL
   AOL's
   AWS
   AWS's
   Aachen
   ...

This will display the *entire contents* of the file.

Combine contents of files
-------------------------
If you include multiple file names in ``cat``, it will
combine them and print their contents on the screen.

If you would like to save the output to a file instead,
use the following format:

.. code-block:: bash

   cat file1.txt file2.txt > files.txt

The ``>`` operator redirects *standard output* to the file
name following it.
