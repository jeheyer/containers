Apache2.4 + mod-wsgi + python3.8 container built on Ubuntu

Instructions:

The container uses the standard TCP ports of 80 for HTTP and 443 for HTTPS.  

To use a custom configuration:

- Mount any custom configuration files in /etc/apache2/conf-enabled/
- Mount any custom virtual host files in /etc/apache2/sites-enabled/

