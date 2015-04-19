# vhost-split.py
Splits an apache vhost file into separate files so you could use them in the 
Apache folders `sites-available` and `sites-enabled`.

Just pass itthe configuration file and the script will generate a bunch of files
named with the ServerName variable found in each virtual host. 
Note that repeated entries will generate separate files (http://www.mydomain.com, http://www.mydomain.com-1, …). 

TODO:  
The script will also report commented entries.

Source:  
https://axelio.wordpress.com/2007/02/15/split-virtualhost-directives-into-multiple-files/
