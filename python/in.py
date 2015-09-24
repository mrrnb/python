import sys
import grape_method 
class wcontrol():
	hostlist=[]
if __name__ == '__main__':
#	host_list=['10.10.112.44','10.10.105.186']
#	port=22
#	timeout=3
#	uname='root'
#	passwd='#qaz@WSX#'
#	cmd_list=['ps -ef|grep crond']
#pdolinux_r=grape_method.pdolinux(host_list,port,timeout,uname,passwd,cmd_list)
#for i in pdolinux_r:
#	print '%s\n'%(i)
	host_list=['10.10.79.38','10.10.71.173','10.10.78.225','10.10.73.162','10.10.143.162','10.10.127.53','10.10.185.171']
	port=22
	timeout=5
	uname='root'
	passwd='Xtbg&SW#X'
	cmd_list=['rsync -var -e "ssh -i /home/nobody/.ssh/id_rsa" nobody@10.10.79.38:/app/www/  /app/www/','/app/nginx/sbin/nginx -s reload']
if len(sys.argv) < 2:
	print "Grape need more parameters.Using \'python %s -?\' get more help infomation."%(sys.argv[0])
	sys.exit(0)
elif len(sys.argv) == 2:
	if sys.argv[1] == "-?":
		print "python %s platform \"cmd1\" \"cmd2\" \"cmd... ...\""%(sys.argv[0])
		sys.exit(0)
	elif sys.argv[1] == "windows":
		pdowindows_r=grape_method.pdowindows(host_list,port,timeout,uname,passwd,cmd_list)
		for i in pdowindows_r:
			print '%s\n'%(i)
		sys.exit(0)
	elif sys.argv[1] == "linux":
		pdolinux_r=grape_method.pdolinux(host_list,port,timeout,uname,passwd,cmd_list)
		for i in pdolinux_r:
			print '%s\r'%(i)
		sys.exit(0)
	else:
		print "Unknown parameters:%s"%(sys.argv[1])
		sys.exit(1)
else:
#	for i in range(1,len(sys.argv)):
#		print "Param:",i,sys.argv[i]
	sys.exit(0)
