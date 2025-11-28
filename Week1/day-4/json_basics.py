import json

data = {
    "name" : "Chelsea",
    "age" : 17,
    "skills" : ['Python', 'JavaScript', 'SQL'],
    "address" : {
        "city": "jakarta",
        "country": "Indonesia"
    }
}

#Write to file
with open("user_data.json", "w") as f:
    json.dump(data, f, indent=2)
    
print("data save ti file user_data.json")

#Reading JSON
with open("user_data.json", "r") as f:
    loaded_data = json.load(f)
    
print(f"\n{loaded_data}")
print(f"Name: {loaded_data['name']}")
print(f"Skills: {', '.join(loaded_data['skills'])}")
print(f"City: {loaded_data['address']['city']}")