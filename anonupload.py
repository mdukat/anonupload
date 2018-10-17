#!/usr/bin/python3
import os
import sys
import getopt
import json

# Tests
for executable in ('gpg', 'gzip', 'bzip2', 'tar', 'curl', 'ls'):
	if(os.system('which ' + executable + ' > /dev/null') != 0):
		print("[ERROR] Can't find " + executable + "!")
		sys.exit()

print("[INFO] Tests ok!")

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

encryption_lock = False

if(server == False):
	print("[ERROR] Server not found, using anonfile!")
	server = "anonfile"
if(gpg_recipient == False):
	print("[ERROR] GPG Name not found, encryption disabled!")
	encryption_lock = True
if(api_key == False):
	print("[ERROR] API key not found, do you want to upload anyways? (y/n)")
	answer = input()
	if(answer in ('n', 'N')):
		print("Exiting...")
		sys.exit()

# Handle arguments
opts, args = getopt.getopt(sys.argv[1:], "hedg:b:")
g = None	#gzip
b = None	#bzip2
e = False	#encrypt
f = None	#file
d = False	#directory
for opt, arg in opts:
	if(opt == '-g'): #gzip
		if(arg in (1,2,3,4,5,6,7,8,9)):
			g = arg
		else:
			g = 5
	elif(opt == '-b'): #bzip2
		if(arg in (1,2,3,4,5,6,7,8,9)):
			b = arg
		else:
			b = 5
	elif(opt == '-e'): #encrypt
		e = True
	elif(opt == '-h'): #help
		print("anonupload - Fast upload files from terminal\nsyntax: anonupload -e -h -g[1-9] -b[1-9] -d [file_name/directory_name]\n-e - encrypt using GPG\n-h - shows this help\n-g[1-9] - gzip file\n-b[1-9] - bzip2 file\n-d - use when you want to tar whole directory")
		sys.exit()
	elif(opt == '-d'): #directory
		d = True

f = args[0] #file
if(os.system('ls ' + f + ' > /dev/null 2>&1') != 0):
	print("[ERROR] File not found!")
	sys.exit()

# Process file
if(d == True): # Create tar
	print("[INFO] Creating tar from directory...")
	os.system('tar cvf ' + f + '.tar ' + f)
	f = f + '.tar'

if(f != None and d == False): # Copy
	print("[INFO] Making copy to work on...")
	os.system('cp ' + f + ' cp_' + f)
	f = 'cp_' + f

if(e == True and encryption_lock == False): # Encryption
	print("[INFO] Encrypting using " + gpg_recipient + " public key...")
	os.system('gpg -e -r ' + gpg_recipient + ' ' + f)
	os.system('rm ' + f)
	f = f + '.gpg'

if(g != None): # Gzip
	print("[INFO] Gzip-ing with -" + str(g) + " argument...")
	os.system('gzip -' + str(g) + ' ' + f)
	f = f + '.gz'

if(b != None): # Bzip2
	print("[INFO] Bzip2-ing with -" + str(b) + " argument...")
	os.system('bzip2 -' + str(b) + ' ' + f)
	f = f + '.bz2'

if(f != None): # Upload #TODO: If API exists, use api upload, not non-api
	print("[INFO] Uploading to " + server + '...')
	url = 'https://anonfile.com/api/upload'
	if(server == 'megaupload'):
		url = 'https://megaupload.com/api/upload'
	elif(server == 'bayfiles'):
		url = 'https://bayfiles.com/api/upload'
	if(api_key != False):
		url = url + '?token=' + api_key
	output = os.popen('curl -F "file=@' + f + '" ' + url).read()
	output_formatted = json.loads(output)

print("[UPLOAD OK] File link: " + output_formatted['data']['file']['url']['short'])
print("[INFO] Removing copy file...")
os.system('rm ' + f)
