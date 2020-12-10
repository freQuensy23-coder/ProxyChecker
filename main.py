from Checker import Checker
import threading
from requests import get, exceptions
import time


def check(proxy):
    """Функция для работы с многопоточностью"""
    try:
        if checker.check_proxy(proxy) is True:
            goods.append(proxy)
            print(proxy)
    except:
        pass


checker = Checker()
proxy_filename = "proxy.txt"  # File with proxy by default
proxy_list = []  # Proxies will be copied from that file to this list
goods = []  # Working proxies

try:
    f = open(proxy_filename, "r")
except FileNotFoundError:
    filename = input("Введите название файла со список файлов (ip:port) ")
    f = open(filename, "r")

for line in f:
    proxy = "http://" + line
    proxy = proxy.replace("\n", "")
    proxy_list.append({"http": proxy})

print(proxy_list)
t_list = []
for i, proxy_dict in enumerate(proxy_list):
    t = threading.Thread(target=check, name=f"thread {i}", args=(proxy_dict,))
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(len(goods))
