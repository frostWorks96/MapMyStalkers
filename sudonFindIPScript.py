
from shodan import Shodan 
import shodanAPIKey
def sudanFunction(ip):
	ip = ip.strip()
	lines=[]   
	api = Shodan(shodanAPIKey.getAPIKey())
	count = 0 
	if isAnIP(ip) != 1:	
		return "545"
	else:
		# Perform the search
		query = ip
		result = api.search(query)
	for service in result['matches']:
		if(count >= 100):
			break
		lines.append(service['ip_str'])
		count+=1
	return lines

def isAnIP(ip):
	sum = 0
	strTemp = "" 
	count= 0
	#1.3.5.7
	if(len(str(ip)) < 7):
		return -1
	for index in range(len(ip)):
		letter = ip[index]
		if(letter.isdigit() and letter != '.'):
			strTemp+=letter
		elif(str(letter) == "."):
			sum = int(strTemp)
			 
			if(sum > 254):				 
				return -1
			sum = 0
			strTemp = ""
			count+=1
		else: 			 
			return -1
	if(int(strTemp) >254):
		return -1
	if(count!=3):		 
		return -1
	return 1
