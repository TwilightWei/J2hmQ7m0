import json

class Config():
    def __init__(self):
        self._config_dir = "app/config.json"
        self._config_data = None
        with open(self._config_dir, 'r') as json_file:
            self._config_data = json.load(json_file)

    def _get_property(self, property_name):
        return self._config_data[property_name]

class TasksConfig(Config):
    def get_url(self) -> str:
        return self._get_property("url")
    
    def get_keyword(self) -> str:
        return self._get_property("keyword")

