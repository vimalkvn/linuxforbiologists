Search database using query sequence
====================================
With the query sequence downloaded and the database
downloaded and formatted, you can start performing a
BLAST search.

First, change into the directory containing the
query sequence:

.. code-block:: bash

   cd ~/projects/sars-cov-2

Now run the ``blastp`` command using the query sequence
and the complete path to the database:

.. code-block:: bash

   blastp -query P0DTC2.fasta \
   -db /home/user/databases/swissprot \
   -out blastp-results.txt \
   -outfmt "7 sacc stitle qlen slen pident"

What the options mean:

``-query``
   Path to the query sequence.

``-db``
   Complete path of the sequence database.

``-out``
   File to save results to.

``-outfmt``
   Format of the output file. This will use format
   option ``7`` (tab-delimited text) and include the
   following information:

   - accession number and description of matching sequences
     (``sacc`` and ``stitle``),
   - query and subject sequence lengths (``qlen`` and ``slen``)
   - percentage identity of the match (``pident``).


When the database search is complete, you can open
``blastp-results.txt`` to view the results:

.. code-block:: bash

   less -S blastp-results.txt
   
The ``-S`` option of the ``less`` command disables
word-wrap.

Output:

.. code-block:: text

    # BLASTP 2.9.0+
    # Query: sp|P0DTC2|SPIKE_SARS2 Spike glycoprotein OS=Severe acute respiratory syndrome coronavirus 2 OX=2697049 GN=S PE=1 SV=1
    # Database: /home/user/databases/swissprot
    # Fields: subject acc., subject title, query length, subject length, % identity
    # 88 hits found
    P0DTC2	Spike glycoprotein OS=Severe acute respiratory syndrome coronavirus 2 OX=2697049 GN=S PE=1 SV=1	1273	1273	100.000
    P59594	Spike glycoprotein OS=Severe acute respiratory syndrome coronavirus OX=694009 GN=S PE=1 SV=1	1273	1255	76.038
    Q3LZX1	Spike glycoprotein OS=Bat coronavirus HKU3 OX=442736 GN=S PE=3 SV=1	1273	1242	76.041
    Q3I5J5	Spike glycoprotein OS=Bat coronavirus Rp3/2004 OX=349344 GN=S PE=1 SV=1	1273	1241	75.334
    Q0Q475	Spike glycoprotein OS=Bat coronavirus 279/2005 OX=389167 GN=S PE=3 SV=1	1273	1241	74.745
    ...


