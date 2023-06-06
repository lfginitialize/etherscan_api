# etherscan_api
## 用途：
調用API獲取想要的信息，例如GasPrice, Gasfee

## 要求：
Python環境安裝庫Requests
```rudy
pip install requests
```

## 使用方法：
將etherscan_api.py文件拷貝到/Users/YOURNAME/opt/anaconda3/lib/python3.9/site-packages/mypackage目錄下。
```rudy
from mypackage.etherscan_api.etherscan_api import Ethereum
eth = Ethereum()
gasprice = eth.get_gas_price() # 這個函數會返回Proposal Gasprice

# Safe gas price: 66 Gwei
# Propose gas price: 66 Gwei
# Fast gas price: 70 Gwei
# 66.0
```

```rudy
from mypackage.etherscan_api.etherscan_api import BSC
bsc = BSC()
gasprice = bsc.get_gas_price() # 這個函數會返回Proposal Gasprice

# Safe gas price: 3 Gwei
# Propose gas price: 3 Gwei
# Fast gas price: 3 Gwei
# 3.0
```

```rudy
from mypackage.etherscan_api.etherscan_api import Polygon
polygon = Polygon()
gasprice = polygon.get_gas_price() # 這個函數會返回Proposal Gasprice

# Safe gas price: 163.7 Gwei
# Propose gas price: 211.2 Gwei
# Fast gas price: 223.9 Gwei
# 211.2
```


```rudy
from mypackage.etherscan_api.etherscan_api import Optimism
op = Optimism() OP Gas Price: 21000 wei
op.eth_estimateGas() # 這個函數會返回Proposal Gasprice

# OP eth_estimateGas: 21000 wei
```

```rudy
from mypackage.etherscan_api.etherscan_api import Arbitrum
arb = Arbitrum()
arb.eth_estimateGas()

# ARB eth_estimateGas: 342213 wei
```
