import json
import os

class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Creating new config.")
                return self.create_default_config()
             
        else:
            return self.create_default_config()
                 
    def create_default_config(self):
        default = {
            "app_name": "My Python App",
            "version": "1.0.0",
            "settings": {
                "theme": "dark",
                "language": "en",
                "auto_save": True
            },
            "paths": {
                "data_folder": "./data",
                "backup_folder": "./backup"
            }
        }
        
        self.save_config(default)
        return default
    
    def save_config(self, config=None):
        if config is None:
            config = self.config
            
        try:
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
        
    def get(self, key, default=None):
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
                
            else: 
                return default
            
        return value
    
    def set(self, key, value):
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
            
        config[keys[-1]] = value
        self.save_config()
        
    def show_config(self):
        print("\n" + "="*50)
        print("CURRENT CONFIGURATION")
        print("="*50)
        print(json.dumps(self.config, indent=2))
        print("="*50+'\n')
        
if __name__ == "__main__":
    config = ConfigManager()
    config.show_config()
    
    print(f"Theme: {config.get('settings.theme')}")
    print(f"Language: {config.get('settings.language')}")
    
    config.set('settings.theme', 'light')
    config.set('user.name', 'chelsea')
    config.show_config()