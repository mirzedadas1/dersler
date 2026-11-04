#virtual muhit(venv),pip,requirements.txt.
#requests
#flask
#django
#python -m venv venv

 #venv\Scripts\Activate.ps1
 #venv\Scripts\activate.bat

#python -m pip install requests
#python -m  pip list
#python -m pip show requests
# python -m pip uninstall   requests
#python -m pip install requests==2.34.4

"""import requests


url = (
    "https://api.open-meteo.com/v1/forecast?latitude=40.4093&longitude=49.8671&current_weather=true"
)

response = requests.get(url)
data = response.json()


current = data["current_weather"]
print("Temperatur: ",current['temperature'] )

"""

#python -m pip freeze > requirements.txt
#python -m pip install -r requirements.txt      