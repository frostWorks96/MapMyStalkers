from flask import Flask, request, render_template
import sudonFindIPScript
import apiGeoScriptLatLng
from templates import app
app = Flask(__name__)
app.config.from_object('configurations.DevelopmentConfig')
app.run()
@app.route('/')
def home():
    return render_template('submitIP.php') + render_template('basicMap.html') + render_template('closeJavaScript.html')

@app.route('/', methods=['POST'])
def my_form_post():
	string = render_template('submitIP.php')
	string +="<br>"
	string += render_template('basicMap.html') +"\n"
	string += render_template('addDots.html') +"\n"
	string += "\t\tvar berlinMarker = new H.map.Marker({lat:52.5192,lng:13.4061});\n"
	string += "\t\tmap.addObject(berlinMarker);\n"
	string += render_template('closeDots.html') +"\n"

	string += render_template('closeJavaScript.html')
	#return string
	text = request.form['text']
	processed_text = text.upper()
	lines = sudonFindIPScript.sudanFunction(text.strip())
	if(lines == "545"):
		string = "the ip addres you sumbmited was wrong <br>"
		string += render_template('submitIP.php')
		return string
        
	result = apiGeoScriptLatLng.geoLocationScript(lines)
	string = ""
	if(result == "404"):
		string = "sudan database does not contain any connecting ip address with the ip adress provided<br>"
		string += render_template('submitIP.php')
		
	else:
		string = render_template('submitIP.php')
		string +="<br>"
		string += render_template('MapOpen.html')
		for line in result:
			string+=line
		string+=render_template('MapClose.html')
	print("\n\n"+string+"\n\n") 
	return string
	
if __name__ == '__main__':
    app.run(debug=True)
