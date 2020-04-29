import random
import string

from app.config import CustomerConfig

class Customer():
    def __init__(self):
        pass

    # Generate a specific number of random customer data
    def generate_customer(self) -> dict:
        config = CustomerConfig()
        customer_number = config.get_customer_number()
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
        config = CustomerConfig()
        id_length = config.get_id_length()
        customer_id = ''
        customer_id += ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase))
        customer_id += ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=id_length-1))
        return customer_id

    def _generate_name(self) -> str:
        customer_name = random.choice(self._initial_customer_list())
        return customer_name

    def _generate_customer_mobile(self) -> str:
        config = CustomerConfig()
        country_code = config.get_country_code()
        door_numbers = config.get_door_numbers()
        phone_length = config.get_phone_length()
        phone_number = random.choice(door_numbers)
        phone_number += ''.join(random.choices(string.digits, k=phone_length-len(phone_number)))
        phone_number = country_code + phone_number[1:]
        return phone_number

    def _generate_frequency(self) -> int:
        config = CustomerConfig()
        frequency_range = config.get_frequency_range()
        frequency = random.randint(frequency_range[0], frequency_range[1])
        return frequency
    
    def _initial_customer_list(self) -> list:
        config = CustomerConfig()
        name_number = config.get_name_number()
        name_list = config.get_name_list()
        customer_list = random.sample(name_list, k=name_number)
        return customer_list