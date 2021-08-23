``free`` — view free and used memory
====================================
With ``free``, you can find the amount of free and used 
memory (:abbr:`RAM (Random Access Memory)`) and swap space.

Usage:

.. code-block:: bash

   free -h
   
Output:

.. code-block:: console

                 total        used        free      shared  buff/cache   available
   Mem:          3.8Gi       618Mi       1.3Gi       7.0Mi       1.9Gi       3.0Gi
   Swap:         979Mi          0B       979Mi
   
The ``-h`` option makes the output human-readable with 
corresponding units displayed. In the example above, the 
amount of free physical memory (RAM) is 1.3 GiB (Gibibytes).

