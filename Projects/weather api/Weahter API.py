# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Hae Ji Chong
# 11/18/23

import requests
import json


# Use zip code to get latitude and longitude coordinate
def get_zip(zip_code):
    api_key = "YOUR_API_KEY"
    url_zip ="http://api.openweathermap.org/geo/1.0/zip?zip=" + zip_code + ",US"+"&appid=" + api_key
    try:
        response = requests.get(url_zip)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error: ", err)
    else:
        data_zip = response.json()
        lat = data_zip["lat"]
        lon = data_zip["lon"]
        get_weather(lat, lon)


# Use city and state name input to get latitude and longitude of the place
def get_city(city, state):
    api_key = "YOUR_API_KEY"
    url_city = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "," + state + ",US" + "&appid=" + api_key
    try:
        response = requests.get(url_city)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    else:
        data_city = json.loads(response.text)
        if not data_city:
            print('You have input an invalid city/state, please try again')
        else:
            lat = data_city[0]["lat"]
            lon = data_city[0]["lon"]
            get_weather(lat, lon)


# From obtained latitude and longitude, get various information such as weather and description
# Also asks the user what metric they would like to use
# Prints HTTP error if the website is not found
def get_weather(lat, lon):
    unit_temp = input("Which metric would you like to use for measurement? metric for C, imperial for F, standard "
                      "for K, q to exit: ")
    if unit_temp.lower() == "metric" or unit_temp.lower() == "imperial" or unit_temp.lower() == "standard":
        api_key = "YOUR_API_KEY"
        weather_api = ("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon)
                       + "&appid=" + api_key + "&units=" + unit_temp)
        try:
            response = requests.get(weather_api)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print("HTTP Error:", err)
        else:
            weather = json.loads(response.text)
            temperature = weather["main"]
            print("--------------------------------------------")
            print("Current weather condition for " + str(weather["name"]))
            print("current temp: " + str(temperature["temp"]) + "°")
            print("feels temp: " + str(temperature["feels_like"]) + "°")
            print("low temp: " + str(temperature["temp_min"]) + "°")
            print("high temp " + str(temperature["temp_max"]) + "°")
            print("pressure: " + str(temperature["pressure"]) + "hPa")
            print("humidity: " + str(temperature["humidity"]) + "%")
            print("description: " + str(weather["weather"][0]["description"]))
            print("--------------------------------------------")
    else:
        if unit_temp == "q":
            print("Thank you for using the program")
        else:
            print("Please put a valid unit")
            get_weather(lat, lon)


# Main method to ask the user how they want to look up the weather
def main():
    while True:
        search = input('Type zip code, city name, or q to quit: ')
        if search.lower() == 'q':
            print('Thank you for using the program!')
            break
        elif search.isdigit():
            get_zip(search)
        else:
            state = input('Please type in state name: ')
            get_city(search, state)


if __name__ == '__main__':
    main()
