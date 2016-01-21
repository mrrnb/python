#/bin/bash
#date: 2016.01.14

#memcmd=`ps -f  -C "memcached" | sed -n '/-p 11211/p' | awk -F'data' '{print "/data"$2}'`
memcmd="/data/memcached/bin/memcached -d -m 2048 -l 0.0.0.0 -p 11211 -u root -v"
mempid=`ps -fC "memcached" | sed -n '/-p 11211/p'| awk '{print $2}'`

if [[ $1 = "stop" ]];then
        if [[ `ps -fC "memcached" | sed -n '/-p 11211/p'` = "" ]];then
                echo "memcached is not running !"
        else
                #ps -fC "memcached" | sed -n '/-p 11211/p'
                echo -e "Memcached pid is "$mempid" !\nNow kill it !"
                kill $mempid
                #ps -fC "memcached" | sed -n '/-p 11211/p'
                service httpd stop
        fi
elif [[ $1 = "start" ]];then
        echo -e "start memcached cmd is:\n$memcmd\nNow start it !\n"
        $memcmd
        service httpd start
elif [[ $1 = "restart" ]];then
        if [[ `ps -fC "memcached" | sed -n '/-p 11211/p'` = "" ]];then
                echo "memcached is not running !"
        else
                #ps -fC "memcached" | sed -n '/-p 11211/p'
                echo -e "Memcached pid is "$mempid" !\nNow kill it !"
                kill $mempid
                echo -e "start memcached cmd is:\n$memcmd\nNow start it !\n"
                $memcmd
                #ps -fC "memcached" | sed -n '/-p 11211/p'
                service httpd restart
        fi
else
        echo "( stop | start | restart )"
fi
