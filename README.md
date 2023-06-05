# etherscan_api
用途：
調用API獲取想要的信息，例如GasPrice, Gasfee

要求：
Python環境安裝庫Requests
```rudy
pip install requests
```

使用方法：
將etherscan_api.py文件拷貝到/Users/YOURNAME/opt/anaconda3/lib/python3.9/site-packages/mypackage目錄下。
```rudy
from mypackage.etherscan_api.etherscan_api import Ethereum
eth = Ethereum()
gasprice = eth.get_gas_price() # 這個函數會返回Proposal Gasprice
```

```rudy
from mypackage.etherscan_api.etherscan_api import BSC
bsc = BSC()
gasprice = bsc.get_gas_price() # 這個函數會返回Proposal Gasprice
```

```rudy
from mypackage.etherscan_api.etherscan_api import Polygon
polygon = Polygon()
gasprice = polygon.get_gas_price() # 這個函數會返回Proposal Gasprice
```
