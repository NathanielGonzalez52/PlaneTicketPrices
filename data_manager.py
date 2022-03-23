from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "LINK TO SHEETY"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_headers = {
            "Authorization": "YOUR AUTH CODE"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers = sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
data = DataManager()
print(data.get_destination_data())