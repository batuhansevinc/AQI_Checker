import sys
import time
import threading

class LoadingAnimation:
    def __init__(self):
        self.loading = False
        self.loading_thread = None

    def start(self):
        self.loading = True
        self.loading_thread = threading.Thread(target=self.animate)
        self.loading_thread.start()

    def stop(self):
        self.loading = False
        if self.loading_thread:
            self.loading_thread.join()

    def animate(self):
        chars = "|/-\\"
        while self.loading:
            for char in chars:
                sys.stdout.write(f'\rGetting AQI data {char}')  # Satır başına dön ve metni yazdır
                sys.stdout.flush()  # Buffer'ı hemen temizle ve metni yazdır
                time.sleep(0.2)  # Kısa bir süre bekle
