import random
import datetime

# ---- Tool: Get Weather (Mock Real-Time) ----
def get_weather(city):
    weather_data = [
        {"temp": 35, "condition": "Sunny ☀️"},
        {"temp": 28, "condition": "Cloudy ☁️"},
        {"temp": 24, "condition": "Rainy 🌧️"},
        {"temp": 18, "condition": "Cool 🌥️"}
    ]
    
    data = random.choice(weather_data)
    data["city"] = city
    data["time"] = datetime.datetime.now().strftime("%H:%M:%S")
    
    return data

# ---- Outfit Logic ----
def suggest_outfit(temp, condition):
    if "Rainy" in condition:
        return "Carry an umbrella ☔ and wear waterproof footwear."
    elif temp > 32:
        return "Wear light cotton clothes, stay hydrated 🧴."
    elif temp > 25:
        return "Comfortable casual wear is fine 👕."
    else:
        return "Wear a jacket or sweater 🧥."

# ---- ReAct Agent ----
class WeatherAgent:
    
    def run(self, city):
        print("\n" + "="*60)
        print("User Input:", city)

      
        
        weather = get_weather(city)

       
        outfit = suggest_outfit(weather["temp"], weather["condition"])
        
        print(f"📍 City: {weather['city']}")
        print(f"🌡️ Temperature: {weather['temp']}°C")
        print(f"🌤️ Condition: {weather['condition']}")
        print(f"👗 Outfit Suggestion: {outfit}")

# ---- Run Multiple Inputs ----
agent = WeatherAgent()

city = input(f"\nEnter City : ")
agent.run(city)


