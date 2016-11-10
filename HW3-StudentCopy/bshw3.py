# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

# Creating index.html file
fopen = open('index.html', 'w')

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(url).read().decode()
soup = BeautifulSoup(html, 'html.parser')

# Searching for text that includes the word student
students = soup.find_all(text=re.compile('student'))

for line in students:
	replace = line.replace('student', 'AMAZING student')
	# Using replace_with function from bs4 doc
	line.replace_with(replace)

for img in soup.find_all('img'):
	if img['src'] == 'logo2.png':
	    img['src'] = 'media/logo.png'
	else:
	    img['src'] = 'media/image.jpg' 

prettify = soup.prettify()
fopen.write(prettify)

