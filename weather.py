import requests as rq
def get_weather():
    url="http://api.weatherstack.com/current?access_key=9ff857d7b6320531e9acdf698bd9cfd5&query=kolkata"
    response=rq.get(url)
    data=response.json()
    # print(data)
    info={"Temperature":data['current']['temperature'],"Humidity":data['current']['humidity'],"Weather":data['current']['weather_descriptions'][0],"Feels like":data['current']['feelslike']}
    return info


