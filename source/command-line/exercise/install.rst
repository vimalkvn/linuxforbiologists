
.. index:: apt

Install NCBI BLAST+ package
===========================
.. attention::

   *This procedure installs software in system paths and
   so requires administrator privileges.*


NCBI BLAST+ is available in the Linux package
repositories. You can install it using ``apt``:

.. code-block:: bash

    sudo apt install ncbi-blast+

Type ``y`` when prompted to continue.

.. code-block:: console

    [sudo] password for user:
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    The following additional packages will be installed:
      libmbedcrypto3 libmbedtls12 libmbedx509-0 ncbi-data
    The following NEW packages will be installed:
      libmbedcrypto3 libmbedtls12 libmbedx509-0 ncbi-blast+ ncbi-data
    0 upgraded, 5 newly installed, 0 to remove and 0 not upgraded.
    Need to get 14.9 MB of archives.
    After this operation, 75.0 MB of additional disk space will be used.
    Do you want to continue? [Y/n] y


