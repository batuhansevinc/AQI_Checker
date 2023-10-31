import threading

from AQIUptader import update_aqi
from AQIRequester import AQIRequester
from LoadingAnimation import LoadingAnimation


class MenuManager:
    def __init__(self):
        self.user_city = None
        self.aqi_requester = AQIRequester()
        self.loading_animation = LoadingAnimation()
        self.show_menu = True

    def display_menu(self):
        while self.show_menu:  # show_menu durumu True olduğunda menüyü göster
            print("Menu:")
            print("1. Show air quality based on your location and start updates")
            print("2. Enter the name of the city to show air quality")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.loading_animation.start()  # Animasyonu başlat
                aqi, city, status = self.aqi_requester.get_aqi()
                self.loading_animation.stop()  # Animasyonu durdur
            elif choice == '2':
                while True:
                    city_input = input("Enter the city name: ")
                    self.loading_animation.start()  # Animasyonu başlat
                    aqi, city, status = self.aqi_requester.get_aqi(city_input)
                    self.loading_animation.stop()  # Animasyonu durdur
                    if aqi and city and status:
                        self.show_menu = False  # Geçerli veriler alındıysa menüyü tekrar gösterme
                        break
                    print('Invalid city name or city not found, please try again.')
                continue
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")
                continue

            if aqi and city and status:
                print(f'Air Quality Index (AQI) for {city}: {aqi} - Status: {status}')
                threading.Thread(target=update_aqi, args=(self.aqi_requester,)).start()  # Start updates
            elif choice != '2':  # Error message already printed for choice '2'
                print('AQI could not be obtained or city could not be determined.')



