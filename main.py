from Checker import Checker
import threading
from requests import get, exceptions
import time
import datetime
from Core import get_proxies_from_file,  save_goods, check

goods = []  # Working proxies
checker = Checker()


proxy_list = get_proxies_from_file()

print(proxy_list)
t_list = []
for i, proxy_dict in enumerate(proxy_list):
    t = threading.Thread(target=check, name=f"thread {i}", args=(proxy_dict, checker))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(len(goods))
# Now save proxies
save_goods(goods)