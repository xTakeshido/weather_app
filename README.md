# Weather App

This is a simple weather application built using Python and `customtkinter`. The application allows users to enter a city name and fetches the current weather information for that city using the OpenWeatherMap API.

## Features

- Enter a city name to get the current weather information.
- Displays the weather description and an appropriate weather icon.
- Shows the current temperature in Celsius.

## Requirements

- Python 3.x
- `customtkinter`
- `requests`
- `Pillow`

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Set the API key in [main.py](http://_vscodecontentref_/2)

3. Run the [main.py](http://_vscodecontentref_/2) file to start the application:

    ```sh
    python main.py
    ```

4. Enter the name of a city in the input field and click the "Confirm" button.
5. The application will display the current weather information for the entered city.

## Files

- [main.py](http://_vscodecontentref_/3): The main application file containing the code for the weather app.
- [requirements.txt](http://_vscodecontentref_/4): A file listing the dependencies required for the project.
- [README.md](http://_vscodecontentref_/5): This readme file.

## Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api) for providing the weather data.
- [Pillow](https://python-pillow.org/) for image processing.
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for the custom tkinter widgets.