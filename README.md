# ProxyChecker
MultiThreading Proxy cheker

# Installing
```
git clone https://github.com/freQuensy23-coder/ProxyChecker/
pip install requests
```
# Using command line util:
```
python CommandLineUtil.py --file proxy.txt --threads -1 --timeout 20
```
Result will be saved to Goods.txt

Proxy.txt example: 
```
40.113.206.14:80
52.221.196.143:80
61.91.61.110:80
69.75.143.12:80
82.165.252.82:80
18.183.65.22:80
144.76.99.207:1110
104.211.29.96:80
75.151.213.85:8080
104.248.26.39:8080
173.236.180.243:19646
```


# Using in your projects
```python
from Checker import checker
checker.time_out = 30
if checker.check_connection: # If user is on line
   list_to_check = [{
    "http": "http://" + "185.156.172.122" + ":" + "3128",
    "https": "https://"+ "96.18.70.146" + ":" + "3128"
  }]
  
  for proxy in list_to_check:
    print(checker.check_proxy(proxy_dict=proxy))


