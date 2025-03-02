import tkinter as tk
import requests
import json

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.city_label = tk.Label(master, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(master)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.temp_label = tk.Label(master, text="Temperature: ")
        self.temp_label.pack()

        self.humidity_label = tk.Label(master, text="Humidity: ")
        self.humidity_label.pack()

        self.conditions_label = tk.Label(master, text="Conditions: ")
        self.conditions_label.pack()
    def get_weather(self):
        city = self.city_entry.get()
        api_key = "b83ab54266114418d641392d8201fd7b" 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  
            weather_data = response.json()

            temp_celsius = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            conditions = weather_data["weather"][0]["description"]

            self.temp_label.config(text=f"Temperature: {temp_celsius}°C")
            self.humidity_label.config(text=f"Humidity: {humidity}%")
            self.conditions_label.config(text=f"Conditions: {conditions}")
        
        except requests.exceptions.RequestException as e:
             self.temp_label.config(text=f"Error: {e}")
             self.humidity_label.config(text="")
             self.conditions_label.config(text="")
        
        except (KeyError, IndexError) as e:
            self.temp_label.config(text=f"Error: Data parsing error: {e}")
            self.humidity_label.config(text="")
            self.conditions_label.config(text="")


root = tk.Tk()
app = WeatherApp(root)
root.mainloop()