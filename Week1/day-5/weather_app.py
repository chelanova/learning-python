import requests
import json
from datetime import datetime 

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.saved_locations = self.load_saved_locations()
        
    def load_saved_locations(self):
        try:
            with open("saved_locations.json", 'r') as f:
                return json.load(f)
            
        except FileNotFoundError:
            return []
        
    def save_locations(self):
        with open("saved_locations.json", 'w') as f:
            json.dump(self.saved_locations, f, indent=2)
            
    def get_current_weather(self, city):
        url = f"{self.base_url}/weather"
        
        params = {
            "q" : city,
            "appid" : self.api_key,
            "units" : "metric"  
        }
        
        try:
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"City {city} not found!")
                return None
            else:
                print(f"Error: {response.status_code}")
                
        except Exception as e:
            print(f"Error to connect to API: {e}")
            return None
        
    def get_forecast(self, city, days=5):
        url = f"{self.base_url}/forecast"
        params = {
            "q" : city,
            "appid" : self.api_key,
            "units" : "metric",
            "cnt" : days * 8
        }
        
        try:
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error: {e}")
            
    def display_current_weather(self, data):
        if not data:
            return
        
        print("\n" + "="*60)
        print(f"WEATHER IN {data['name'].upper()}, {data['sys']['country']}")
        print("="*60)
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description'].capitalize()
        
        print(f"\nTemperature: {temp}°C (feels like: {feels_like}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Pressure: {data['main']['pressure']} hPa")
            
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        
        print("\n" + "="*60 + "\n")
        
    def display_forecast(self, data):
        if not data:
            return
        
        print("\n" + "="*60)
        print(f" 5-DAY FORECAST FOR {data['city']['name'].upper()}")
        print("="*60)
        
        forecasts_by_day = {}
        
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            
            if date not in forecasts_by_day:
                forecasts_by_day[date] = {
                    'temp' : [],
                    'conditions' : [],
                    'humidity' : []
                }
                
            forecasts_by_day[date]['temp'].append(item['main']['temp'])
            forecasts_by_day[date]['conditions'].append(item['weather'][0]['description'])
            forecasts_by_day[date]['humidity'].append(item['main']['humidity'])
                
        for data, info in list(forecasts_by_day.items())[:5]:
            day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%A, %B %d')
            avg_temp = sum(info['temp'])/ len(info['temp'])
            max_temp = max(info['temp'])
            min_temp = min(info['temp'])
            common_condition = max(set(info['conditions']), 
                                 key=info['conditions'].count)
            avg_humidity = sum(info['humidity'])/ len(info['humidity'])
            
            print(f"{day_name}")
            print(f"Temp: {avg_temp:.1f}°C (max: {max_temp:.1f}°C, min: {min_temp:.1f}°C)")
            print(f"{common_condition.capitalize()}")
            print(f"Humidity: {avg_humidity:.0f}%")
            
        print("="*60 + "\n")
         
    def add_saved_locations(self, city):
        if city not in self.saved_locations:
            self.saved_locations.append(city)
            self.save_locations()
            
            print(f"{city} added to saved locations!")
        else:
            print(f"{city} is already in saved locations.")
            
    def show_saved_locations(self):
        if not self.saved_locations:
            print("No saved locations yet!")
            return
        
        print("\nSaved Locations:")
        for i, city in enumerate(self.saved_locations, 1):
            print(f"{i}. {city}")
        print()
def main():
    print("=== WEATHER APP ===\n")
    
    api_key = input("Enter your OpenWeatherMap API key\n(Get free key at: openweathermap.org/api): ").strip()
    
    if not api_key:
        print("API key required")
        return
    
    app = WeatherApp(api_key)
    
    while True:
        print("\n=== WEATHER APP MENU ===")
        print("1. Current Weather")
        print("2. 5-Day Forecast")
        print("3. Saved Locations")
        print("4. Add Location to Favorites")
        print("5. Exit")
        choice = input("\nChoose option (1-5): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            if city:
                data =  app.get_current_weather(city)
                app.display_current_weather(data)
                
                if data:
                    save = input("Save this location? (y/n):").strip().lower()
                    if save == 'y':
                        app.add_saved_locations(city)
        elif choice == '2':
            city = input("Enter city name: ").strip()
            if city:
                data =  app.get_forecast(city)
                app.display_forecast(data)
                
        elif choice == '3':
            app.show_saved_locations()
            
            if app.saved_locations:
                check = input("\nCheck weather for a saved location? (enter number or 'n'): ").strip()
                if check.isdigit():
                    idx = int(check) - 1
                    if 0 <= idx < len(app.saved_locations):
                        city = app.saved_locations[idx]
                        data = app.get_current_weather(city)
                        app.display_current_weather(data)
                
                
        elif choice == '4':
            city = input("Enter city name for saved: ").strip()
            if city:
                app.add_saved_locations(city)
                
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()                   