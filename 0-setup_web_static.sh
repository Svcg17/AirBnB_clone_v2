#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx restart
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server;/a location /hbnb_static/ {' /etc/nginx/sites-available/default
sed -i '/location \/hbnb_static\/ {/a alias \/data\/web_static\/current\/;' /etc/nginx/sites-available/default
sed -i '/current\/;/a }' /etc/nginx/sites-available/default
service nginx restart
