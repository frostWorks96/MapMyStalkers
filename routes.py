from app  import app
import sudonFindIPScript
import apiGeoScriptLatLng

@app.route('/test/<ip>', methods=['GET'])
def test(ip):
  lines = sudonFindIPScript.sudanFunction(ip.strip())
  if(lines == "545"):
    return "{error: 545, message: 'invalid ip address'}"
  result = apiGeoScriptLatLng.geoLocationScript(lines)
  if(result == "404"):
    return "{error: 404, message: 'no ip found'}" 
  
  return result

