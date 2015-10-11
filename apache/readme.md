
### Install
- `sudo apt-get install apache2`

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
