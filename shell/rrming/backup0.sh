#!/bin/bash
# Author: Ezreal
# Date: 2015-11-18

riqi=`date "+%Y%m%d%H%M%S"`

service httpd stop
cd /app/www/
tar -czvf /app/backup/KRM_iosqa_webserver_${riqi}.tar.gz *
ps -ef | grep memcache
