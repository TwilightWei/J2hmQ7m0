import json

class Config():
    def __init__(self):
        self._config_dir = "app/config.json"
        self._config_data = None
        with open(self._config_dir, 'r') as json_file:
            self._config_data = json.load(json_file)

    def get_property(self, property_name):
        return self._config_data[property_name]

class MyViewConfig(Config):
    def get_folder_dir(self):
        return self.get_property("folder_dir")
    
    def get_csv_name(self):
        return self.get_property("csv_name")

class CustomerConfig(Config):
    def get_id_length(self):
        return self.get_property("id_length")

    def get_name_number(self):
        return self.get_property("name_number")

    def get_name_list(self):
        return self.get_property("name_list")

    def get_country_code(self):
        return self.get_property("country_code")

    def get_door_number(self):
        return self.get_property("door_number")

    def get_phone_length(self):
        return self.get_property("phone_length")

    def get_frequency_range(self):
        return self.get_property("frequency_range")