#!/usr/bin/python3
import os
import sys
import getopt
import json

# Load config
api_key = False
gpg_recipient = False
server = False
home = os.environ['HOME']

config_file = open(home + '/.config/anonupload', 'r')
if(config_file.readable() != True):
	print("[ERROR] Can't read config file!")
	sys.exit()

c = 'aaaaa'
while(c != ''):
	c = config_file.readline().replace('\n','')
	if(c[0:3] == 'API'):
		api_key = c.split(':')[1]
	elif(c[0:6] == 'SERVER'):
		server = c.split(':')[1]
	elif(c[0:3] == 'GPG'):
		gpg_recipient = c.split(':')[1]

config_file.close()

if(server == False):
	print("[ERROR] Server not found, using anonfile!")
	server = "anonfile"
if(gpg_recipient == False):
	print("[ERROR] GPG Name not found, encryption disabled!")
if(api_key == False):
	print("[ERROR] API key not found, do you want to upload anyways? (y/n)")
	answer = input()
	if(answer in ('n', 'N')):
		print("Exiting...")
		sys.exit()

# Handle arguments
opts, args = getopt.getopt(sys.argv[1:], "g:ef:")
g = None	#gzip
e = False	#encrypt
f = None	#file
for opt, arg in opts:
	if(opt == '-g'): #gzip
		if(arg in (1,2,3,4,5,6,7,8,9)):
			g = arg
		else:
			g = 5
	elif(opt == '-e'): #encrypt
		e = True

f = args[0] #file

# Process file
if(f != None): # Copy
	print("[INFO] Making copy to work on...")
	os.system('cp ' + f + ' cp_' + f)
	f = 'cp_' + f

if(e == True): # Encryption
	print("[INFO] Encrypting using " + gpg_recipient + " public key...")
	os.system('gpg -e -r ' + gpg_recipient + ' ' + f)
	os.system('rm ' + f)
	f = f + '.gpg'

if(g != None): # Gzip
	print("[INFO] Gzip-ing with -" + str(g) + " argument...")
	os.system('gzip -' + str(g) + ' ' + f)
	f = f + '.gz'

if(f != None): # Upload #TODO: If API exists, use api upload, not non-api
	print("[INFO] Uploading to " + server + '...')
	url = 'https://anonfile.com/api/upload'
	if(server == 'megaupload'):
		url = 'https://megaupload.com/api/upload'
	elif(server == 'bayfiles'):
		url = 'https://bayfiles.com/api/upload'

	output = os.popen('curl -F "file=@' + f + '" ' + url).read()
	output_formatted = json.loads(output)
	print("[UPLOAD OK] File link: " + output_formatted['data']['file']['url']['short'])
	print("[INFO] Removing copy file...")
	os.system('rm ' + f)
