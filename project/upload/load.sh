#!/usr/bin/expect -f


#set host 10.10.28.228
set host [lindex $argv 0]
set password [lindex $argv 1]
set port [lindex $argv 2]
set user [lindex $argv 3]
set source_dir [lindex $argv 4]
set target_dir [lindex $argv 5]
set timeout -1


#set host 192.168.66.200
#set password redhat
#set source_dir /root/github/python/project/auto-opration/
#set target_dir /root/scp/


#spawn scp -r -P $port /root/github/python/project/auto-opration/ $user@$host:/root/scp/
spawn scp -r -P $port $source_dir $user@$host:$target_dir
expect {
	"(yes/no)?"
	{
		send "yes\n"
		expect "password:"
		{
			send "$password\r"
		}
	}
	"*password:"
		{
			send "$password\r"
		}

}

#send "$password\r"
expect eof
