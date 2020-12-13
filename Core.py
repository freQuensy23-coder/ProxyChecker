import threading


def get_proxies_from_file(file_name="proxy.txt"):
    proxy_list = []  # Proxies will be copied from that file to this list
    f = open(file_name, "r")

    for line in f:
        proxy = "http://" + line
        proxy = proxy.replace("\n", "")
        proxy_list.append({"http": proxy})
    return proxy_list


def save_goods(goods, filename="Goods.txt"):
    with open(filename, "w") as save_file:
        for good_proxy in goods:
            save_file.write(good_proxy[list(good_proxy.keys())[0]] + "\n")


def check(proxy, checker, goods):
    try:
        if checker.check_proxy(proxy) is True:
            goods.append(proxy)
    except:
        pass
    return goods


def generate_threads(proxies, checker, goods, func=check):
    """Return list of non started threads to check using checker"""
    t_list = []  # List of threads
    for i, proxy in enumerate(proxies):
        t = threading.Thread(target=func, name=f"thread {i}", args=(proxy, checker, goods))
        t_list.append(t)
    return t_list


def slice_list(list_: list, n: int):
    """Slice list list_ into n slices. Returns list of list."""
    if n > len(list_):
        raise IndexError
    else:
        result = []
        els_in_slice = int(len(list_) / n)  # Number of els in one
        prev_last = 0
        for i in range(n):
            result.append(list_[prev_last:prev_last + els_in_slice])
            prev_last += els_in_slice
    return result
