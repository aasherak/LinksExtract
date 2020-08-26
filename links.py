import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import ssl
import requests
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def linksExtract() :
	siteName = input("Enter website (e.g. https://aasherakhlaque.me): ")
	fileName = input("Enter file name to be saved as (e.g. links.txt) : ")

	if siteName[len(siteName) - 1] == '/' :
		siteName = siteName[:len(siteName) - 1]

	try :
		r = requests.get(siteName)
	except :
		print("Url could not be reached. Check the url again")
		quit()

	html = r.text
	
	# tags = re.findall(r'\<\s*?a[\s\S]*?\>', html)
	tags = re.findall(r'href\s*?=\s*?[\'\"][\S]*?[\'\"]', html)

	try :
		newFile = open(fileName, 'w+')
	except :
		print("File could not be opened. Please try again.")
		quit()

	for tag in tags :
		tag = tag.replace(" ", "")[6:-1];
		if tag.startswith('h') :
			newFile.write('link : ' + tag + '\n')
		elif tag.startswith('//') :
			newFile.write('link : ' + "https:" + tag + '\n')
		elif tag.startswith('/') :
			newFile.write('link : ' + siteName + tag + '\n')
		elif tag.startswith('m') :
			s = tag.find('?')
			if s == -1 :
				newFile.write('email : ' + tag[7:] + '\n')
			else :
				newFile.write('email : ' + tag[7:s] + '\n')


	newFile.close()

	print("Saved as", fileName)

linksExtract()