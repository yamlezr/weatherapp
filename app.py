#Name: Arsalan Anwar
#Please review a basic weather script that I built.

#Downloaded requests library by using pip install requests and then imported it in the script.
import requests 

#Copy and pasted the api_key from the OpenWeatherMap website.
api_key="5b3379ef981aa4463623efa60e2e72ff"

#Created a user_input variable that will prompt the user to input the city.
user_input = input("Enter city: ")

#Created a variable called city_forecast and Uploaded the URL in the script using requests.get command. (I copy pasted the URL from the OpenWeatherMap website, it was in the API.doc)
city_forecast = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")

#Used print command to get the content from the URL in json format.
#print(city_forecast.json())

#Created these new variables and gave them values according to the dictionary that was printed. (Note I rounded off where the values were in decimal numbers.)
temperature = round(city_forecast.json()['main']['temp'])
sky = city_forecast.json()['weather'][0]['description']
min_temp = round(city_forecast.json()["main"]["temp_min"])

#Used an if command here to say if the min_temp is greater than 60 degrees, print the weather being Warm.
if min_temp > 60:
    print(f"The weather in {user_input} is: Warm")
    print(f"The temperature is: {temperature}F")
    print(f"If you look up, the sky looks like {sky}.")
    print(f"You should plan a picnic with your family")
#If the min_temp is less than 60 degrees, print the weather being Chilly.
else:
    print(f"The weather in {user_input} is: Chilly")
    print(f"The temperature is: {temperature}F")
    print(f"If you look up, the sky looks like {sky}.")
    print(f"Maybe you should stay in the house.")

#Thank you DirectSupply for giving me an opportunity to showcase my skills.
