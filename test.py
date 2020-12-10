from Checker import Checker
import asyncio

checker = Checker()
# print(checker.check_connection())



list_to_check = [{
    "h": "http://" + "185.156.172.122" + ":" + "3128",
    "hs": "https://"+ "96.18.70.146" + ":" + "3128"
}]

for proxy in list_to_check:
    print(checker.check_proxy(proxy_dict=proxy))


