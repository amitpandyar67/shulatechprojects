import tkinter as tk
import requests

API_KEY = "d62ad69f5e50219c15fbb96643bd1e74"  

def get_weather():
    city = city_entry.get()
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_info.set(f"Temperature: {data['main']['temp']}°C\n"
                             f"Humidity: {data['main']['humidity']}%\n"
                             f"Condition: {data['weather'][0]['description'].title()}")
        else:
            weather_info.set("City not found!")

# GUI setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack()

weather_info = tk.StringVar()
tk.Label(root, textvariable=weather_info, font=("Arial", 14)).pack()

root.mainloop()
