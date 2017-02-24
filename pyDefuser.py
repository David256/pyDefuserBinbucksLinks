#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"""

import sys
import base64
import requests
import urllib.parse

FIN = '[0m'
CC = chr(27)

def usage():
	print('''\x1b[1;92mPyDefuserBinbucksLinks.\x1b[0m
With this tool you will get the link after the binbucks link.

{realname} <url> : Where url is the binbucks link. Example:

{realname} http://binb.ooo/POvAo

--- the end ---
'''.format(realname=sys.argv[0]))

def decode(url):
	"""
	This method URL decode the url parameter.
	"""
	return urllib.parse.unquote(url)

if len(sys.argv)==1:
	usage()
	exit(0)

the_url = sys.argv[1]

try:
	web_handler = requests.get(the_url)
except Exception as e:
	print('\x1b[1;91mGot an error: %s\x1b[0m' % str(e))
	exit(-1)

new_url = web_handler.url

thing = new_url.replace('http://www.binbucks.com/site/sc?','')

parameters = thing.split('&')

try:
	gold_encoded_link = parameters[1][2:]
except Exception as e:
	print('URL invalid. I tried to parse the url, but: %s' % str(e))
	exit(-1)

gold_link = decode(gold_encoded_link)

diamond_link = base64.b64decode(gold_link)

print('OK. the link is:')
print(diamond_link.decode('utf-8'))