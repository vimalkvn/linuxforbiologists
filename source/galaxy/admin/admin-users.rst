Adding user to list of admin users
==================================
With ``galaxy.yml`` open in Text Editor, search 
for the ``admin_users`` setting. 

You will find the following section:

.. code-block:: ini   

   # Administrative users - set this to a comma-separated 
   # list of valid Galaxy users (email addresses).  These 
   # users will have access to the Admin section of the 
   # server, and will have access to create users,
   # groups, roles, libraries, and more.  For more 
   # information, see: https://galaxyproject.org/admin/
   #admin_users: null

Uncomment ``admin_users`` by removing the ``#`` symbol at
the beginning.

Replace ``null`` with the email address of the user account. 

For example:

.. code-block:: ini

  admin_users: user@example.org

Save the file.

