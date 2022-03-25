import requests 
import json
import GeoScriptAPIKey
def findAndPrint(result, response):
	str="" 
	num = 10
	 
	for element in range(result , len(response.text)):
		
		if(response.text[element] == '\"'):
			break;
		str+=response.text[element]
	#print(str)
	return str
def geoLocationScript(text): 
	lines = []
	num = 0
	for line in text:
		string = ""
		url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
		
		str1 = str(line.strip())
		querystring = {"ip":str1}
		headers = {
			'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
			'x-rapidapi-key': GeoScriptAPIKey.getAPIKey()
			} 
		response = requests.request("GET", url, headers=headers,params=querystring)
		state = "region\":\""
		latitude = "\"latitude\":\""
		longitude = "\"longitude\":\""
		city = "city\":\""
		country = "country\":\""
		if(response.text.find(country)== -1):
			return "404"
		data = response.json()
		string +="\t\tvar marker =  new H.map.Marker({lat:" + str(data["latitude"])
		string +=", lng:" + str(data["longitude"])
		string += "});\n\t\tmap.addObject(marker);\n"
		 
		 
		#num+=1
		lines.append(string)
		 
		if(num >=2):
			break
	return lines
