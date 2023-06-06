import requests
import time

eth_api_key = 'YOUR API KEY'
bsc_api_key = 'YOUR API KEY'
polygon_api_key = 'YOUR API KEY'
op_api_key = 'YOUR API KEY'
arb_api_key = 'YOUR API KEY'

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


class Optimism:
    def eth_estimateGas(self):
        url = "https://api-optimistic.etherscan.io/api"

        payload = {
            "module": "proxy",
            "action": "eth_estimateGas",
            "data": "0x",
            "to": "0xf6c3c3621f42ec1f1cd1207bb1571d93646ab29a",
            "value": "0xff22",
            "gasPrice": "0x51da038cc",
            "gas": "0x2710",
            "apikey": op_api_key
        }

        while True:
            try:
                response = requests.get(url, params=payload, timeout=5)  # 设置超时时间为5秒
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()

                if "result" in data:
                    eth_estimateGas = int(data["result"], 16)
                    print("OP eth_estimateGas: {} wei".format(eth_estimateGas))
                    return eth_estimateGas
                else:
                    print("Error occurred: {}".format(data["error"]))

            except (requests.RequestException, ValueError) as e:
                print("Error occurred during gas price retrieval:", str(e))

            print("Retrying after 5 seconds...")
            time.sleep(5)

        return None  # 返回 None 表示未能成功获取 gas price


class Arbitrum:
    def eth_estimateGas(self):
        url = "https://api.arbiscan.io/api"

        payload = {
            "module" : "proxy",
            "action" : "eth_estimateGas",
            "data" : "0x",
            "to" : "0xf6c3c3621f42ec1f1cd1207bb1571d93646ab29a",
            "value" : "0xff22",
            "gasPrice" : "0x51da038cc",
            "gas" : "0x5f5e0ff",
            "apikey" : arb_api_key
        }
        # payload = {
        #     "module" : "proxy",
        #     "action" : "eth_gasPrice",
        #     "apikey" : arb_api_key
        # }

        while True:
            try:
                response = requests.get(url, params=payload, timeout=5)  # 设置超时时间为5秒
                response.raise_for_status()  # 检查请求是否成功
                data = response.json()

                if "result" in data:
                    eth_estimateGas = int(data["result"], 16)
                    print("ARB eth_estimateGas: {} wei".format(eth_estimateGas))
                    return eth_estimateGas
                else:
                    print("Error occurred: {}".format(data["error"]))

            except (requests.RequestException, ValueError) as e:
                print("Error occurred during gas price retrieval:", str(e))

            print("Retrying after 5 seconds...")
            time.sleep(5)

        return None  # 返回 None 表示未能成功获取 gas price
