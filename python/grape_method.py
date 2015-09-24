import telnetlib
import paramiko
import time
import threading
def dotelnet(host,port,timeout,uname,passwd,cmdarg,results):
#	print str(host)+str(uname)+str(passwd)
	finish='>'
	tn = telnetlib.Telnet(str(host),port,timeout)
	tn.set_debuglevel(3)
	tn.read_until('login: ')
	tn.write(uname+'\r')
	tn.read_until('password: ')
	tn.write(passwd+'\r')
	for cmd in cmdarg:
		time.sleep(0.5)
		tn.write(cmd+'\r')
		time.sleep(timeout)
		results.append(tn.read_very_eager())
#		print result
	tn.close()
def dossh(host,port,timeout,uname,passwd,cmdarg,results):
	try:
		sh=paramiko.SSHClient()
		sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		sh.connect(host,port,uname,passwd)
		for i in cmdarg:
			stdin,stdout,stderr=sh.exec_command(i)
			stdin.write("Y")
			out=stdout.readlines()
			results.append(out)
#			for o in out:
#				print o
		sh.close()
	except:
		print '%s\tError\n'%(host)	
def pdowindows(host_list,port,timeout,uname,passwd,cmd_list):
	threads=[]
	results=[]
	for host in host_list:
		t=threading.Thread(target=dotelnet,args=(host,port,timeout,uname,passwd,cmd_list,results))
		t.setDaemon(True)
		threads.append(t)
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	return results
def pdolinux(host_list,port,timeout,uname,passwd,cmd_list):
	threads=[]
	results=[]
	for host in host_list:
		t=threading.Thread(target=dossh,args=(host,port,timeout,uname,passwd,cmd_list,results))
		t.setDaemon(True)
		threads.append(t)
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	return results
if __name__=='__main__':
	timeout=5
	ip='10.10.112.44'
	port=22
	uname='root'
	passwd='#qaz@WSX#'
	cmdarg=('ls','ifconfig')
	results=[]
#dossh(str(ip),port,timeout,uname,passwd,cmdarg,results)










