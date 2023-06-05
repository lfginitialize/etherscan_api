import requests

api_key = 'YOUR API KEY HERE'

class Ethereum:
    def get_gas_price(self) :
        url = "https://api.etherscan.io/api"

        payload = {
            "module": "gastracker",
            "action": "gasoracle",
            "apikey": api_key
        }

        response = requests.get(url, params=payload)
        data = response.json()

        if data["status"] == "1":
            print("Safe gas price: {} Gwei".format(data["result"]["SafeGasPrice"]))
            print("Propose gas price: {} Gwei".format(data["result"]["ProposeGasPrice"]))
            print("Fast gas price: {} Gwei".format(data["result"]["FastGasPrice"]))
            global ProposeGasPrice
            ProposeGasPrice = float(data["result"]["ProposeGasPrice"])
        else:
            print("Error occurred: {}".format(data["message"]))

        return ProposeGasPrice
