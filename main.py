from AQIUptader import update_aqi
from MenuManager import MenuManager


def main():
    menu_manager = MenuManager()
    menu_manager.display_menu()
    update_aqi(menu_manager.aqi_requester)


if __name__ == "__main__":
    main()
