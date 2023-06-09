# Verloop-WeatherAPI
## Setup
### Running this code:
Note: The following steps Docker to be already installed on your system.
If you instead want to run this app without docker you can do so from the command line using 
```
python e: weatherAPI.py
```
Be sure to install all the dependencies using the requirements file prior to that. Using a venv is reccomended.

1. Firstly you'll need to clone this repo or download the code and extract it in a local folder.
```
git clone https://github.com/Ln8plus/Verloop-WeatherAPI
```

2. Provide your RapidAPI key in the secrets.txt file. 
You can btain your RapidAPI key from:
```
https://rapidapi.com/auth/sign-up?referral=/weatherapi/api/weatherapi-com/
```

3. For our web app we'll need to manually build an image and then run it. Building the image is done by:
```
docker build -t rapid_weather_api .
```
The above command builds a docker image using the files of the current folder and names it "pymongo".

4. Next run the web app using:
```
docker run -p 9000:9000 rapid_weather_api
```
This command runs the image and binds port 9000 of the container to our local machine.


## API endpoint

- GET Returns City name, Temperature, Latitude & Longitude of specified city.
Output format can be either json or xml. (To be specified with URL)

Sample URLs:
```
http://localhost:9000/weather?city=Monaco&output_format=json
```

```
http://localhost:9000/weather?city=Monaco&output_format=xml
```

JSON Output:
![image](https://drive.google.com/uc?export=view&id=1tZLUEpdwT9Av809s80T-7Xi_yiyKcmuO)&nbsp;&nbsp;

XML Output:
![image](https://drive.google.com/uc?export=view&id=1cDRspPwAwXltwAKdbMvv19zpUb8FB6zB)&nbsp;&nbsp;