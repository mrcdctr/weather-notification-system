<<<<<<< HEAD
# weather-notification-system
This Python application fetches weather forecasts from the OpenWeatherMap API and sends notifications about significant weather conditions (rain, snow, extreme heat) via Twilio SMS. It also logs notifications to a text file for later reference. The script is highly customizable and allows users to input their location and desired forecast duration.
=======
Weather Notification System

This Python application fetches weather forecasts from the OpenWeatherMap API and sends notifications about significant weather conditions (rain, snow, extreme heat) via Twilio SMS. It also logs notifications to a text file for later reference. The script is highly customizable and allows users to input their location and desired forecast duration.

Features

Dynamic Location Input: Enter a city or location name to fetch weather forecasts for your area.

Weather Notifications: Get SMS alerts for rain, snow, and extreme temperatures.

Extended Forecast: Choose between 1 to 5 days of weather forecasts.

Error Handling: Gracefully handles invalid inputs and API errors.

Data Logging: Saves all notifications to a weather_notifications.txt file.

Prerequisites

1. APIs and Accounts

OpenWeatherMap:

Sign up at OpenWeatherMap.

Generate an API key for the weather forecast.

Twilio:

Sign up at Twilio.

Get your Account SID, Auth Token, and a verified Twilio phone number.

2. Python Libraries

Install the required Python packages using:

pip install requests twilio geopy

How to Use

1. Clone or Download

Download this repository or clone it using:

git clone <repository_url>

2. Set Up API Keys

Open the script and replace the placeholders:

__YOUR_OWM_API_KEY__ with your OpenWeatherMap API key.

__YOUR_TWILIO_ACCOUNT_ID__ with your Twilio Account SID.

__YOUR_TWILIO_AUTH_TOKEN__ with your Twilio Auth Token.

Replace YOUR TWILIO VIRTUAL NUMBER and YOUR TWILIO VERIFIED REAL NUMBER with appropriate phone numbers.

3. Run the Script

Execute the script using Python:

python weather_twilio_script.py

4. Interact with the Application

Enter a location name (e.g., "New York").

Specify the number of forecast days (1-5).

Receive notifications via SMS if rain, snow, or extreme temperatures are detected.

5. View Notifications Log

Check the weather_notifications.txt file to see a log of all weather alerts sent.

Example Usage

Input:

Enter Location: London

Forecast Days: 3

Output:

SMS sent: "It's going to rain today. Remember to bring an ☔️"

SMS sent: "It might get extremely hot today. Stay hydrated!"

Log File (weather_notifications.txt):

It's going to rain today. Remember to bring an ☔️
It might get extremely hot today. Stay hydrated!

Error Handling

Invalid location input will terminate the program with a clear error message.

OpenWeatherMap or Twilio API errors will be caught and displayed.

Invalid forecast duration defaults to 1 day.

Customization

1. Notification Messages

You can modify the notification text by editing the analyze_weather() function.

2. Additional Weather Conditions

To include other conditions (e.g., fog, wind), extend the analyze_weather() logic.

3. Logging Format

Modify the save_notifications_to_file() function to change how notifications are logged.

License

This project is licensed under the MIT License.

Acknowledgments

OpenWeatherMap for the weather data API.

Twilio for SMS delivery.

Geopy for geolocation services.
>>>>>>> ba700d1 (Signed commit)
