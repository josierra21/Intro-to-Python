#DSC510
#Week12: Weather Application
#Programming Assignment: Final Project Week12
#Author: Joanna Sierra-Mendoza
#02/23/24


import requests

def geo_lookup(api_key, zip_code=None, city_name=None, state_code=None):
    country_code = "US"  #hardcode country

    if zip_code:
        url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}'
    elif city_name and state_code:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={api_key}'
    else:
        print("Invalid input. Provide either zip code or city/state information.")
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:  #successfull connection
            data = response.json()
            if data.get('sys', {}).get('country') != country_code:
                print("Location not found in the United States. Please check your input.")
                return None
            return data['coord']['lat'], data['coord']['lon']
        elif response.status_code == 404: #resource can't be found
            print("Location not found. Please check your input.")
        else:
            print(f"Unexpected error: {response.status_code}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

    return None


def retrieve_weather_info(api_key, lat, lon, unit='metric'):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={unit}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200:
            return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

    return None


def display_weather_info(weather_info, unit_label):
    print("\nWeather Forecast for " f"{weather_info['name']}, {weather_info['sys']['country']}")
    print("--------------------------------")
    weather_data = [
        ("Temperature", f"{weather_info['main']['temp']} {unit_label}"),
        ("Feels Like", f"{weather_info['main']['feels_like']} {unit_label}"),
        ("Min Temperature", f"{weather_info['main']['temp_min']} {unit_label}"),
        ("Max Temperature", f"{weather_info['main']['temp_max']} {unit_label}"),
        ("Pressure", f"{weather_info['main']['pressure']} hPa"),
        ("Humidity", f"{weather_info['main']['humidity']}%"),
        ("Description", weather_info['weather'][0]['description']),
        ("Wind Speed", f"{weather_info['wind']['speed']} m/s"),
        ("Wind Direction", f"{weather_info['wind']['deg']}°"),
        ("Cloudiness", f"{weather_info['clouds']['all']}%"),
    ]
    max_length = max(len(label) for label, _ in weather_data) + 2
    for label, value in weather_data: #two column display
        print(f"{label:{max_length}} {value}")

def main():
    api_key = '7309886f14fea70c8006128068954e05'
    print("WELCOME TO MY WEATHER APP")
    while True:
        input_choice = input("\nSelect one of the input methods: (1 for zip code, 2 for city/state, Q to quit): ")
        if input_choice.lower() == 'q':
            print("\nThank you for using my weather program!")
            break
        if input_choice == '1':
            zip_code = input("Enter zip code: ")
            location_info = geo_lookup(api_key, zip_code=zip_code)
        elif input_choice == '2':
            city_name = input("Enter city name: ")
            state_code = input("Enter state code: ")
            location_info = geo_lookup(api_key, city_name=city_name, state_code=state_code)
        else:
            print("Invalid input choice. Please try again.")
            continue
        if not location_info:
            print("Failed to retrieve location information. Please try again.")
            continue
        lat, lon = location_info

        while True:
            unit_choice = input(
                "Choose temperature unit (1 for Celsius, 2 for Fahrenheit, 3 for Kelvin): ")
            units = {'1': 'metric', '2': 'imperial', '3': 'standard'}
            unit = units.get(unit_choice)
            unit_label = '°C' if unit_choice == '1' else '°F' if unit_choice == '2' else 'K'

            if unit:
                break  # loop breaks if an invalid unit is provided
            else:
                print("Invalid unit choice. Please try again.")
        weather_info = retrieve_weather_info(api_key, lat, lon, unit=unit) #api call 2

        if weather_info:
            display_weather_info(weather_info, unit_label)
        else:
            print("Failed to retrieve weather information. Please try again.")

if __name__ == "__main__":
    main()
