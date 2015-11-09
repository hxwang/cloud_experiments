
### Install
- Update: `sudo apt-get update`
- Install apache2: `sudo apt-get install apache2`

### Configuration
- Website folder read/write permission
  - Enable apache to read files, edit file `/etc/apache2/apache2.conf`
  ```
  <Directory /home/ubuntu/website>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
  </Directory>
  ```
  - Change local folder permission `chmod -R 775 /home/ubuntu/website/`
- Configure DocumentRoot in file `/etc/apache2/sites-available/000-default.conf`
  - `DocumentRoot /home/ubuntu/website`
  
### Restart service
- restart service `sudo /etc/init.d/apache2 restart`

### Logs
- all access logs `/var/log/apache2/access.log`
  - include `2XX`, `3XX` `4XX`


### Bugs
- Public DNS problem
  - If your instance is not configured with public DNS, then you may meet the error
    - `AH00557: apache2: apr_sockaddr_info_get() failed for ip-`
  - Solution: go to `VPC` pannel, and enable DNS name etc. Then a public DNS name will be set for the instance.
  
