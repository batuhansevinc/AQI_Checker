import platform

from plyer import notification


class NotificationManager:
    @staticmethod
    def send_notification(title, message):
        try:
            if platform.system() == "Darwin":  # For macOS
                import pync
                pync.notify(message, title=title)
            elif platform.system() == "Windows":  # For Windows
                notification.notify(
                    title=title,
                    message=message,
                    timeout=10  # Show for 10 seconds
                )
            else:
                print("No notification support for this platform.")
        except Exception as e:
            print(f"Notification error: {e}")

