Download query sequence
=======================
You can follow these steps to download the
query sequence:

1. Create new directory
2. Change into it
3. Download query sequence
4. View the downloaded sequence (optional)

Create new directory — ``mkdir``
--------------------------------
To keep the input and output files related to
this project together, create a new directory in
your home directory using the
:doc:`mkdir <../commands/mkdir>` command.

.. code-block:: bash

   mkdir -p ~/projects/sars-cov-2

Here:

``~`` is shortcut for home directory.

``-p`` creates parent directories if necessary.
In this case, the ``projects`` directory does not
exist, so it is also created.

Change directory — ``cd``
-------------------------
Change into the newly created directory using the
:doc:`cd <../commands/cd>` command:

.. code-block:: bash

   cd ~/projects/sars-cov-2

Download sequence — ``wget``
----------------------------
To download the sequence file, you can use the
``wget`` command with the link to download as the
argument. In this case, the link to download is the URL
corresponding to the FASTA format file
(see :ref:`sample data <sample-data>`):

.. code-block:: bash

   wget https://www.uniprot.org/uniprot/P0DTC2.fasta

When the download is complete, you can use the
:doc:`ls <../commands/ls>` command to verify if the file
exists:

.. code-block:: bash

   ls -l

Output:

.. code-block:: console

   total 4
   -rw-rw-r-- 1 user user 1414 Feb 10 00:00 P0DTC2.fasta

View downloaded sequence — ``cat`` or ``less``
----------------------------------------------
Since ``P0DTC2.fasta`` is in FASTA format — a plain-text
format, you can use the
:doc:`cat <../commands/cat>` command to view the
file's contents:

.. code-block:: bash

   cat P0DTC2.fasta

Output:

.. code-block:: console

   >sp|P0DTC2|SPIKE_SARS2 Spike glycoprotein OS=Severe acute respiratory syndrome coronavirus 2 OX=2697049 GN=S PE=1 SV=1
   MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFS
   NVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIV
   NNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLE
   GKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQT
   LLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETK
   CTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISN
   CVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIAD
   YNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPC
   NGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVN
   FNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITP
   GTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSY
   ECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTI
   SVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQE
   VFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDC
   LGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAM
   QMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALN
   TLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRA
   SANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPA
   ICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDP
   LQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDL
   QELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDD
   SEPVLKGVKLHYT

For more control, you can use the
:doc:`less <../commands/less>` command instead of ``cat``.

