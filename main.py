import os
import requests
from twilio.rest import Client
import googlemaps
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# API Keys and Twilio Credentials (use environment variables for security)
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OPENWEATHER_API_KEY", "your_openweather_api_key")
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
gmaps_api_key = os.getenv("GOOGLE_MAPS_API_KEY", "your_google_maps_api_key")

# Helper Functions
def get_location(location_name):
    """Get latitude and longitude using Google Maps API."""
    gmaps = googlemaps.Client(key=gmaps_api_key)
    try:
        geocode_result = gmaps.geocode(location_name)
        if not geocode_result:
            raise ValueError(f"Could not find the location: {location_name}")
        location = geocode_result[0]["geometry"]["location"]
        return location["lat"], location["lng"]
    except Exception as e:
        messagebox.showerror("Location Error", str(e))
        return None, None

def fetch_weather_data(latitude, longitude, forecast_hours):
    """Fetch weather data from OpenWeatherMap API."""
    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "cnt": forecast_hours,
    }
    try:
        response = requests.get(OWM_Endpoint, params=weather_params)
        response.raise_for_status()
        weather_data = response.json()
        if weather_data.get("cod") != "200":
            raise ValueError(weather_data.get("message", "Unknown error"))
        return weather_data
    except Exception as e:
        messagebox.showerror("Weather Data Error", str(e))
        return None

def analyze_weather(weather_data):
    """Analyze weather data and prepare notifications."""
    notifications = []
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        temperature = hour_data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius

        # Check for rain
        if int(condition_code) < 700:
            notifications.append("It's going to rain. Remember to bring an umbrella.")
        # Check for snow
        if 600 <= int(condition_code) < 700:
            notifications.append("It's going to snow. Stay warm!")
        # Check for extreme temperatures
        if temperature > 35:
            notifications.append("It might get extremely hot. Stay hydrated!")

    return notifications

def send_notifications(notifications):
    """Send notifications via Twilio."""
    try:
        client = Client(account_sid, auth_token)
        combined_message = "\n".join(notifications)
        message = client.messages.create(
            body=combined_message,
            from_="+14025265155",
            to="+393202677867"
        )
        messagebox.showinfo("Success", f"Notification sent: {message.body}")
    except Exception as e:
        messagebox.showerror("Notification Error", str(e))

def save_notifications_to_file(notifications):
    """Save notifications to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("weather_notifications.txt", "a") as file:
        file.write(f"\n[{timestamp}]\n")
        file.write("\n".join(notifications) + "\n")
    messagebox.showinfo("Saved", "Notifications saved to weather_notifications.txt.")

# GUI Functions
def get_weather_and_notify():
    location_name = location_entry.get()
    forecast_days = int(forecast_days_var.get())

    if not location_name:
        messagebox.showwarning("Input Error", "Please enter a location.")
        return

    latitude, longitude = get_location(location_name)
    if latitude is None or longitude is None:
        return

    forecast_hours = forecast_days * 8  # Each day has 8 intervals (3 hours each)
    weather_data = fetch_weather_data(latitude, longitude, forecast_hours)
    if weather_data is None:
        return

    notifications = analyze_weather(weather_data)

    if notifications:
        send_notifications(notifications)
        save_notifications_to_file(notifications)
    else:
        messagebox.showinfo("No Alerts", "No significant weather notifications.")

# GUI Setup
app = tk.Tk()
app.title("Weather Notification System")
app.geometry("400x300")

# Location Input
tk.Label(app, text="Enter Location:").pack(pady=5)
location_entry = tk.Entry(app, width=30)
location_entry.pack(pady=5)

# Forecast Days Dropdown
tk.Label(app, text="Select Forecast Days:").pack(pady=5)
forecast_days_var = tk.StringVar(value="1")
forecast_days_menu = tk.OptionMenu(app, forecast_days_var, "1", "2", "3", "4", "5")
forecast_days_menu.pack(pady=5)

# Get Weather Button
tk.Button(app, text="Get Weather & Notify", command=get_weather_and_notify).pack(pady=20)

# Run the GUI
app.mainloop()
