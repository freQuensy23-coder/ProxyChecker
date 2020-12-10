import requests as req
import random

class Checker():
    def __init__(self, normal_status_code=200):
        self.normal_status_code = normal_status_code
        self.time_out = 30
        self.sites = ["http://google.com",
                      "http://github.com/",
                      "http://youtube.com/",
                      "http://yandex.ru/",
                      "http://ya.ru",
                      "http://yahoo.com",
                      "http://www.facebook.com/",
                      "http://twitter.com/"]


    def check_connection(self):

        for site in self.sites:
            r = req.get(site)

    def check_proxy(self, proxy_dict):
        try:
            r = req.get(random.choice(self.sites), proxies=proxy_dict, timeout=self.time_out)
        except req.exceptions.ProxyError:
            return False
        if r.status_code == self.normal_status_code:
            return True
        else:
            return False

