import requests

api_key = "a536fccca7d7747062a788bebfc96813"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Debug (optional)
print("\nDEBUG:", data)

if data.get("cod") == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")
else:
    print("\n❌ Error:", data.get("message"))