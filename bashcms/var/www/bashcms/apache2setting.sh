#!/bin/bash

#ディレクトリ移動
cd /etc/apache2/sites-available/
#ブログ用に設定ファイルを作成
cp 000-default.conf blog.conf
#ディレクトリ移動　このディレクトリから、リンクをsites-available配下のファイルに貼ることで有効化できる。
cd ../sites-enabled/
#いらないショトカを削除
rm 000-default.conf
#新たなショトカを作成
ln -s ../sites-available/blog.conf blog.conf

#rootでwww-dataのホームディレクトリへの書き込み付与及びログディレクトリの設定
sudo -s
cd /var/www/
mkdir www-data
chown www-data:www-data www-data/
mkdir /var/log/bashcms　#logディレクトリはアプリごとにいちいち作成する必要あり。
chown root:adm /var/log/bashcms #書き込み権限はrootのみが持つようにする。

#おまじない
sudo a2enmod cgi

#最後に再起動が必要だよん
sudo systemctl restart apache2
sudo service apache2 restart

