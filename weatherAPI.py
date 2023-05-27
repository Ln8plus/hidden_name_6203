
import requests, dicttoxml
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class myWeatherAPI(Resource):
    
    def get(self):
        city = request.args.get('city')
        output_format = request.args.get('output_format')
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":city}
        api_key = ""
        #Reading API key from another file.
        with open("secrets.txt", "r") as f:
            api_key = f.readline()
 
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        output_body = {
                        "Temperature":str(data["current"]["temp_c"]) + " C", 
                        "City":data["location"]["name"] +", "+ data["location"]["country"],
                        "Latitude":data["location"]["lat"], 
                        "Longitude":data["location"]["lon"]                                                                                             
                    }
        
        #Converting output_body to relevant format as per query param.
        if output_format == 'json':
            return jsonify(output_body)
        elif output_format == 'xml':
            xml = dicttoxml.dicttoxml(output_body)
            xml_str = xml.decode('utf-8')
            return xml_str, 200, {'Content-Type': 'application/xml'}
        else:
        # Default format
            return jsonify(output_body)
        
api.add_resource(myWeatherAPI, "/weather", endpoint="weather")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, port = 9000)
