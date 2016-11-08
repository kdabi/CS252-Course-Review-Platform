import httplib2
import csv
import json
import requests
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
r = requests.get('http://cse.iitk.ac.in/pages/Faculty.html')
soup = BeautifulSoup(r.text)
for fac in soup.select('.page'):
	
	lena = len(fac.findAll('a'));		
	faculty = []
	for a in range(0,32):
		faculty_data={}
		faculty_data['fac_webpage'] = ''
		faculty_data['fac_name'] = ''
        	faculty_data['fac_data'] = ''
        	faculty_data['fac_id'] = ''
		faculty_data['fac_webpage']= fac.findAll('a')[a]['href']
		faculty_data['fac_name']= fac.findAll('span')[a].text.strip()		
		l= fac.findAll('div')[2*a].text.strip()
                words = l.split()
                t = len(words)
                for i in range(0,t):
			if '(' in words[i]:
				faculty_data['fac_id'] = words[i][1:-1] + '@cse.iitk.ac.in'
				break
		faculty_data['fac_data'] = ''
		for m in range(i+1,t):
			faculty_data['fac_data'] =faculty_data['fac_data']+ ' ' + words[m]
                #faculty[a] = faculty_data
		faculty.append(faculty_data)	
		

file = open("facultydata.json", "w")
json.dump(faculty, file)
file.close()
