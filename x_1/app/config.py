import json

class Config():
    _config_dir = None
    _config_data = None

    def get_property(self, property_name):
        pass

class MyViewConfig(Config):
    def get_folder_dir(self):
        pass
    
    def get_csv_name(self):
        pass

class CustomerConfig(Config):
    def get_customer_number(self):
        pass

    def get_char_lists(self):
        pass

    def get_name_list(self):
        pass

    def get_country_code(self):
        pass

    def get_door_number(self):
        pass

    def get_phone_length(self):
        pass

    def get_frequency_range(self):
        pass