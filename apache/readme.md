
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

### Restart service

### Logs
