# Air Quality Index (AQI) Checker

This program allows users to check the Air Quality Index (AQI) for a specific city or based on their current location. The AQI data is fetched from the World Air Quality Index (WAQI) API, and the program is structured following the OOP and SOLID principles for better modularity and maintainability.

## Features
- Fetch AQI data for a specific city.
- Fetch AQI data based on the user's current location.
- Display AQI data along with a status indicating the air quality (e.g., Good, Moderate, Unhealthy, etc.).
- Continuous updates on AQI data at intervals of 10 minutes.
- Displays a loading animation while fetching AQI data.
- Error handling for invalid city names or unavailable AQI data.

## Usage
1. The user is presented with a menu to choose from:
   - Show air quality based on their location and start updates.
   - Enter the name of the city to show air quality.
   - Exit the program.
2. If the user chooses to fetch AQI data based on their location, the program fetches and displays the AQI data, and starts updating it every 10 minutes.
3. If the user chooses to fetch AQI data for a specific city, they are prompted to enter the city name. The program then fetches and displays the AQI data for that city, and starts updating it every 10 minutes.
4. If the user chooses to exit, the program terminates.

## Future Enhancements
- Adding a graphical user interface (GUI) for a more user-friendly experience.
- Providing notifications to the user when AQI reaches unhealthy levels.
- Allowing users to customize the update interval for AQI data.
- Adding support for other languages.

## Dependencies
- `requests` for making HTTP requests to the WAQI API.
- `threading` for handling continuous updates on AQI data.

## How to Run
1. Ensure you have Python installed on your machine.
2. Install the required dependencies using pip:
   ```bash
   pip install requests
3. Clone the repository and navigate to the project directory.
4. Run the `main.py` script to start the program:
   ```bash
   python main.py
