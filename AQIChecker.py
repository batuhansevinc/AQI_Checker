from NotificationManager import NotificationManager


class AQIChecker:
    def __init__(self, aqi, city, status):
        self.aqi = aqi
        self.city = city
        self.status = status

    def check_aqi(self):
        if self.aqi and self.city and self.status:
            if self.aqi > 150:
                NotificationManager.send_notification(f'{self.city} - High AQI',
                                                      f'AQI: {self.aqi} - Status: {self.status}')
            print(f'Air Quality Index (AQI) for {self.city}: {self.aqi} - Status: {self.status}')
        else:
            print('AQI is not available or city information is false.')
