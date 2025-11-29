import requests
import json

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        respone = requests.get(url)
        
        if respone.status_code == 200:
            joke = respone.json()
            print(f"\n{joke['setup']}")
            print(f"  {joke['punchline']}\n")
            
        else:
            print(f"Error: {respone.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        
def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
    
        if response.status_code == 200:
            user = response.json()
            print(f"\n== GitHub User: {user['login']} ==")
            print(f"Name: {user.get('name', 'N/A')}")
            print(f"Bio: {user.get('bio', 'N/A')}")
            print(f"Public Repos: {user['public_repos']}")
            print(f"Followers: {user['followers']}")
            print(f"Following: {user['following']}")
            print(f"Profile: {user['html_url']}\n")
        elif response.status_code == 404:
            print('User not found!')
        else:
            print(f"Error: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")
        
import requests

def get_weather(city):
    """Get weather data using wttr.in API"""
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            current = data["current_condition"][0]

            print(f"\n Weather in {city.capitalize()}:")
            print(f"   Temperature: {current['temp_C']}°C")
            print(f"   Description: {current['weatherDesc'][0]['value']}\n")

        else:
            print("Could not get weather data.")

    except Exception as e:
        print(f"Error: {e}")


         
if __name__== "__main__":
    print("=== API EXAMPLES ===\n")
    
    print("1. Getting a random joke...")
    get_random_joke()
    
    print("2. Getting GitHub user info...")
    username = input("Enter GitHub username (or press Enter for 'torvalds'): ").strip()
    get_github_user(username or "torvalds")
    
    print("3. Getting weather...")
    city = input("Enter city name: ").strip()
    get_weather(city)
    