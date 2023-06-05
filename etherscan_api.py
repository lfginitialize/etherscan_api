import requests
import time

eth_api_key = 'YOUR ETHScan API KEY HERE'
bsc_api_key = 'YOUR BSCScan API KEY HERE'
polygon_api_key = 'YOUR PolygonScan API KEY HERE'

class Ethereum:
    def get_gas_price(self):
        url = "https://api.etherscan.io/api"

        payload = {
            "module": "gastracker",
            "action": "gasoracle",
            "apikey": eth_api_key
        }

        while True:
            try:
                response = requests.get(url, params=payload, timeout=5)  # 设置超时时间为5秒
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()

                if data["status"] == "1":
                    print("Safe gas price: {} Gwei".format(data["result"]["SafeGasPrice"]))
                    print("Propose gas price: {} Gwei".format(data["result"]["ProposeGasPrice"]))
                    print("Fast gas price: {} Gwei".format(data["result"]["FastGasPrice"]))
                    return float(data["result"]["ProposeGasPrice"])
                else:
                    print("Error occurred: {}".format(data["message"]))

            except (requests.RequestException, ValueError) as e:
                print("Error occurred during gas price retrieval:", str(e))

            print("Retrying after 5 seconds...")
            time.sleep(5)

        return None  # 返回 None 表示未能成功获取 gas price
    
class BSC:
    def get_gas_price(self):
        url = "https://api.bscscan.com/api"

        payload = {
            "module": "gastracker",
            "action": "gasoracle",
            "apikey": bsc_api_key
        }

        while True:
            try:
                response = requests.get(url, params=payload, timeout=5)  # 设置超时时间为5秒
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()

                if data["status"] == "1":
                    print("Safe gas price: {} Gwei".format(data["result"]["SafeGasPrice"]))
                    print("Propose gas price: {} Gwei".format(data["result"]["ProposeGasPrice"]))
                    print("Fast gas price: {} Gwei".format(data["result"]["FastGasPrice"]))
                    return float(data["result"]["ProposeGasPrice"])
                else:
                    print("Error occurred: {}".format(data["message"]))

            except (requests.RequestException, ValueError) as e:
                print("Error occurred during gas price retrieval:", str(e))

            print("Retrying after 5 seconds...")
            time.sleep(5)

        return None  # 返回 None 表示未能成功获取 gas price
    
class Polygon:
    def get_gas_price(self):
        url = "https://api.polygonscan.com/api"

        payload = {
            "module": "gastracker",
            "action": "gasoracle",
            "apikey": polygon_api_key
        }

        while True:
            try:
                response = requests.get(url, params=payload, timeout=5)  # 设置超时时间为5秒
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()

                if data["status"] == "1":
                    print("Safe gas price: {} Gwei".format(data["result"]["SafeGasPrice"]))
                    print("Propose gas price: {} Gwei".format(data["result"]["ProposeGasPrice"]))
                    print("Fast gas price: {} Gwei".format(data["result"]["FastGasPrice"]))
                    return float(data["result"]["ProposeGasPrice"])
                else:
                    print("Error occurred: {}".format(data["message"]))

            except (requests.RequestException, ValueError) as e:
                print("Error occurred during gas price retrieval:", str(e))

            print("Retrying after 5 seconds...")
            time.sleep(5)

        return None  # 返回 None 表示未能成功获取 gas price
