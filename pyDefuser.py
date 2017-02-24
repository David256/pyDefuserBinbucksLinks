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

def decodificar(url):
	"""
	This method URL decode the url parameter.
	"""
	return urllib.parse.unquote(url)

if len(sys.argv)==1:
	usage()
	exit(0)