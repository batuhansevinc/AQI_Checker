import requests

api_key = 'GET YOUR API KEY FROM https://waqi.info/'


class AQIRequester:
    def __init__(self, city=None):
        self.city = city

    def get_aqi(self, city=None):
        if city:
            url = f'https://api.waqi.info/feed/{city}/?token={api_key}'
        else:
            url = f'https://api.waqi.info/feed/here/?token={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'aqi' in data['data'] and 'city' in data['data'] and 'name' in data['data']['city']:
                aqi = data['data']['aqi']
                city = data['data']['city']['name']
                status = self.get_aqi_status(aqi)
                return aqi, city, status
            else:
                print('City not found or enter a valid city name.')
                return None, None, None
        else:
            print(f'Hata: {response.status_code} - {response.text}')
            return None, None, None

    @staticmethod
    def get_aqi_status(aqi):
        if 0 <= aqi <= 50:
            return 'GOOD'
        elif 51 <= aqi <= 100:
            return 'MODERATE'
        elif 101 <= aqi <= 150:
            return 'UNHEATLY'
        elif 151 <= aqi <= 200:
            return 'DANGEROUS'
        elif 201 <= aqi <= 300:
            return 'VERY DANGEROUS'
        else:
            return 'HAZARDOUS'
