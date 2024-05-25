"""
In sign up there has to be a username field and at its side 3 double fields with the title
of initial conditions
this Data will be sent to Username
below these fields there has to be a button to submit (this will auto generate the password)
and send the data to the database, the encrypted username will be returned by the Username class
and the hashed passwrod returned by the Encrypting class.
The console should print the encrypted username and not encrypted password

below that section put a log in section
a username field to log the encrypted username and the initial conditions, this will be sent again to Username
but to decrypt
and put the password that was set.
Here the controller should be able to call the encrypt again witht the password and compare with what was set
in the database, also compare the decrypted username and username of the database

So the databse will store the decrypted username and encrypted passeword
"""