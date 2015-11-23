#!/usr/bin/env python

import paramiko

def dossh(host,port,timeout,uname,passwd,cmdarg,results):
	try:
		sh = paramiko.SSHClient()
		sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		sh.connect(host,port,uname,passwd)
		for i in cmdarg:
			stdin,stdout,stderr=sh.exec_command(i)
			stdin.write('Y')
			out=stdout.readlines()
			results.append(out)
			#for o in out:
			#	print o,
		sh.close()
		return results
	except:
		print '%s\tError\n'%(host)

if __name__=='__main__':
	timeout=5
	host='192.168.66.100'
	port=22
	uname='root'
	passwd='123'
	cmd1='''ifconfig | awk -F":" '{if(NR==2)print $2}' | awk -F" " '{print $1}' '''
	cmd2="""ls /root/github """
	cmdarg=(cmd1,cmd2)
	results=[]
	#dossh(str(host),port,timeout,uname,passwd,cmdarg,results):
	outres = dossh(str(host),port,timeout,uname,passwd,cmdarg,results)
	for i in outres:
		for j in i:
			print j,
