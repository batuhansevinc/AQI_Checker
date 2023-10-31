import threading
from AQIChecker import AQIChecker


def update_aqi(aqi_requester):
    aqi, city, status = aqi_requester.get_aqi()
    if aqi and city and status:
        print(f'Air Quality Index (AQI) for {city}: {aqi} - Status: {status}')
        AQIChecker(aqi, city, status).check_aqi()
    else:
        print('AQI could not be obtained or city could not be determined.')
    threading.Timer(600, update_aqi, args=(aqi_requester,)).start()

