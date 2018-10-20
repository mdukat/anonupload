#!/usr/bin/python3 
import os
import requests
import getopt
import sys

def findDownloadLink(url):
	page = requests.get(url)
	a = page.content[page.content.find(b'download-url')+54:]
	link = str(a[:a.find(b'>')-1])
	link = link[2:]
	link = link[:-1]
	return link

#def getFilesListArray():
#	home = os.environ['HOME']
#	a = open(home + '/.cache/anonupload.files', 'r')
#	c = 'aaaaa'
#	d = []
#	while(c != ''):
#		c = a.readline().replace('\n', '')
#		c = c.split(';')
#		d.append(c)
#	a.close()
#	return d

opts, args = getopt.getopt(sys.argv[1:], "lr")
#l = False #link
#r = False #read
#for opt, arg in opts:
#	if(opt == '-l'):
#		l = True
#		r = False
#		value = args[0]
#	elif(opt == '-r'):
#		r = True
#		l = False

value = args[0]

if(True == True):
	dl_link = findDownloadLink(value)
	os.system('wget ' + dl_link)

#if(r == True):
#	a = getFilesListArray()
#	for name, link in a:
#		print(name + ' = ' + link)
