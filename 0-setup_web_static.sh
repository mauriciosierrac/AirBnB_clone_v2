#!/usr/bin/env bash
# this script install Ngingx Service and verify if exist some dir and create

# update dependencies and install Nginx service
sudo apt-get install -y update
sudo apt-get install -y upgrade
sudo apt-get install -y ngingx

# verify if a dir exists
sudo mkdir -p ./data
sudo mkdir -p ./data/web_static/
sudo mkdir -p ./data/web_static/releases/
sudo mkdir -p ./data/web_static/shared/
sudo mkdir -p ./data/web_static/releases/test/

# create a fake HTML file
echo 'Holberton School' >> /data/web_static/releases/test/index.html

# create a simbolic link, if exist are deleted and recreated ever time the script is ran
rm ./data/web_static/*
ln -s ./data/web_static/releases/test/ ./data/web_static/current

# asigned ubuntu owner to data dir
sudo chown -R ubuntu:ubuntu ./data/

# update Nginx configuration to serve the content hbnb_Static
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/mauriciosierrac/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" >> /etc/ngingx/sites-available/default

# restart Nginx service
sudo service ngingx restart



