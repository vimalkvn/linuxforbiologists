.. _df:

``df`` — report disk usage
==========================
The ``df`` command will report used and available
disk space on all storage devices connected to the
system.

For example, to find the amount of disk space used
in ``/`` — the root filesystem, you can use the command:

.. code-block:: bash

   df -h /

Output:

.. code-block:: console

   Filesystem               Size  Used Avail Use% Mounted on
   /dev/mapper/vgmint-root   28G  6.9G   20G  26% /

The ``-h`` option makes the output human-readable. Without 
this, available disk space will be reported as ``20600196`` 
instead of ``20G``.


