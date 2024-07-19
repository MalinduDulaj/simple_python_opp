import requests
from bs4 import BeautifulSoup

def get_weather_information():
    url = "https://www.meteo.gov.lk/index.php?lang=en"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the section containing weather information
        weather_section = soup.find('div', class_='sp-module-content')

        # Extract Max and Min temperature
        max_temperature = weather_section.find('strong', text='Max Temperature').find_next('div').text.strip()
        min_temperature = weather_section.find('strong', text='Min Temperature').find_next('div').text.strip()

        # Extract Max Rainfall with location
        max_rainfall_location = weather_section.find('strong', text='Max Rainfall').find_next('div').text.strip()
        max_rainfall = weather_section.find('strong', text='Rainfall (mm)').find_next('div').text.strip()

        # Print the extracted information
        print(f"Max Temperature: {max_temperature}")
        print(f"Min Temperature: {min_temperature}")
        print(f"Max Rainfall Location: {max_rainfall_location}")
        print(f"Max Rainfall: {max_rainfall} mm")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    get_weather_information()
