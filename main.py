import customtkinter
import requests
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL module


class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("350x350")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")
        self.getUserInput()
        self.display_weather = self.DisplayWeather(self)  # Create an instance of DisplayWeather
        self.description_weather = self.DescriptionWeather(self)  # Create an instance of DescriptionWeather
        self.mainloop()

    def getUserInput(self):
        self.user_input = self.GetUserInput(self)

    class GetUserInput:
        def __init__(self, parent):
            self.parent = parent  # Set the parent attribute
            self.button(parent)  # Initialize button after entry
            self.entry = customtkinter.CTkEntry(parent, placeholder_text="Enter City Name", width=200, height=30, border_width=1, font=("Arial", 12), justify="center")
            self.entry.pack(pady=(0, 10), side="bottom")  # Position entry above the button

        def button(self, parent):
            self.btn = customtkinter.CTkButton(parent, text="Confirm", command=self.get)
            self.btn.pack(side="bottom", pady=10)  # Position button at the bottom

        def get(self):
            self.entry_city = self.entry.get()
            if self.entry_city == "Enter City Name" or self.entry_city == "":
                self.parent.display_weather.display("City not found")
                self.parent.display_weather.set_icon(r"assets\weather_icons\iddle_icon.png")
                self.parent.description_weather.update_temperature("N/A")
                return
            self.city_name = self.entry_city
            self.api_key = "your_api_key_here"
            self.base_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"
            self.response = requests.get(self.base_url)
            self.parent.display_weather.filterResponse(self.response.json())  # Update weather display
            self.parent.description_weather.update_temperature(self.response.json())  # Update temperature display
            return print(self.response.json())

    class DisplayWeather:
        def __init__(self, parent):
            self.label = customtkinter.CTkLabel(parent, text="Please enter city name", font=("Arial", 15), width=200, height=30)
            self.label.pack(side="bottom", pady=(10, 40))
            self.image_label = customtkinter.CTkLabel(parent, text="")
            self.image_label.pack(side="bottom", pady=(10, 10))
            self.set_icon(r"assets\weather_icons\iddle_icon.png")

        def filterResponse(self, response):
            self.response = response
            if response["cod"] == "404" or self.response["name"] == "Enter City Name" or self.response["name"] == "":
                self.weather = "City not found"
                self.set_icon(r"assets\weather_icons\iddle_icon.png")
            else:
                self.weather = self.response["weather"][0]["main"].lower()
                self.set_icon_based_on_weather(self.weather)
            self.display(self.weather)

        def display(self, data):
            if data == "":
                data = "No data found"
            self.label.configure(text=data.capitalize())

        def set_icon(self, icon_path):
            self.weatherIcon = Image.open(icon_path)
            self.weatherIcon = self.weatherIcon.resize((100, 100))
            self.weatherIcon = ImageTk.PhotoImage(self.weatherIcon)
            self.image_label.configure(image=self.weatherIcon)
            self.image_label.image = self.weatherIcon  # Keep a reference to avoid garbage collection

        def set_icon_based_on_weather(self, weather):
            if weather == "clear":
                self.set_icon(r"assets\weather_icons\clear.png")
            elif weather == "clouds":
                self.set_icon(r"assets\weather_icons\clouds.png")
            elif weather == "rain":
                self.set_icon(r"assets\weather_icons\rain.png")
            elif weather == "thunderstorm":
                self.set_icon(r"assets\weather_icons\thunderstorm.png")
            elif weather == "snow":
                self.set_icon(r"assets\weather_icons\snow.png")
            else:
                self.set_icon(r"assets\weather_icons\iddle_icon.png")

    class DescriptionWeather:
        def __init__(self, parent):
            self.label = customtkinter.CTkLabel(parent, text="Current temperature: N/A", font=("Arial", 15), width=200, height=30)
            self.label.pack(side="bottom", pady=(10, 10))  # Position temperature label under the icon

        def update_temperature(self, response):
            if response == "N/A" or response["cod"] == "404" or response["name"] == "Enter City Name" or response["name"] == "":
                temperature = "N/A"
            else:
                temperature = response["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
                temperature = f"{temperature:.2f}°C"  # Format temperature to 2 decimal places
            self.label.configure(text=f"Current temperature: {temperature}")


app()