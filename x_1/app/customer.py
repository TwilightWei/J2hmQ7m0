import random
import string

from app.config import CustomerConfig

class Customer():
    def __init__(self):
        self.config = CustomerConfig()
        self.customer_list = self._initial_customer_list()

    def generate_customer(self) -> dict:
        customer_number = self.config.get_customer_number()
        customers = {}

        while len(customers) < customer_number:
            customer_mobile = self._generate_customer_mobile()
            if not customer_mobile in customers.keys():
                customer_id = self._generate_customer_id()
                customer_name = self._generate_name() + '.' + customer_id
                frequency = self._generate_frequency()

                customer = {
                    'customer_id': customer_id,
                    'customer_name': customer_name,
                    'frequency': frequency
                }
                customers[customer_mobile] = customer
        return customers
        
    def _generate_customer_id(self) -> str:
        id_length = self.config.get_id_length()
        customer_id = ''
        customer_id += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase))
        customer_id += ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=id_length-1))
        return customer_id

    def _generate_name(self) -> str:
        customer_name = random.choice(self.customer_list)
        return customer_name

    def _generate_customer_mobile(self) -> str:
        country_code = self.config.get_country_code()
        door_number = self.config.get_door_number()
        phone_length = self.config.get_phone_length()
        phone_number = random.choice(door_number)
        phone_number += ''.join(random.choices(string.digits, k=phone_length-len(phone_number)))
        phone_number = country_code + phone_number[1:]
        return phone_number

    def _generate_frequency(self) -> int:
        frequency_range = self.config.get_frequency_range()
        frequency = random.randint(frequency_range[0], frequency_range[1])
        return frequency
    
    def _initial_customer_list(self) -> list:
        name_number = self.config.get_name_number()
        name_list = self.config.get_name_list()
        customer_list = random.sample(name_list, k=name_number)
        return customer_list