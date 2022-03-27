import requests 
import json
import GeoScriptAPIKey
def geoLocationScript(text): 
	jsonOBJ = []
	num = 0
	for line in text:
		
                
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
		jsonOBJ.append({"lat": data["latitude"], "lng": data["longitude"]})
	return json.dumps(jsonOBJ) 
