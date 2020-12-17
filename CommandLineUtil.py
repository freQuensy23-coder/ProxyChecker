import argparse
import os
from Core import get_proxies_from_file, generate_threads, save_goods, slice_list, generate_multi_task_threads
from Checker import Checker
import threading
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Proxy checker")
parser.add_argument("--file",
                    action="store",
                    dest="file_name",
                    default="proxy.txt",
                    type=str,
                    help="Select file with proxy data (ip:port)")
parser.add_argument("--threads",
                    action="store",
                    dest="threads",
                    type=int,
                    default=-1,
                    help="Select number of threads. -1 => Number of threads = Number of proxies, 0 - No threading.")
parser.add_argument("--timeout",
                    action="store",
                    dest="timeout",
                    default=30,
                    type=int,
                    help='Time, during that program will wait the answer from proxy.')
parser.add_argument("--dest",
                    action="store",
                    dest="dest",
                    default="Goods.txt",
                    type=str,
                    help='Select txt filename to save goods into it. Default Goods.txt'
                    )

args = parser.parse_args()
checker = Checker()
goods_dest = args.dest
checker.time_out = args.timeout
goods = []

# Проверяем соединение
if not checker.check_connection():
    print("Some troubles with your connection. Test could be wrong.")

proxies = get_proxies_from_file(file_name=args.file_name)
if args.threads == 0:  # If user don't want to use threading
    for proxy in proxies:
        if checker.check_proxy(proxy_dict=proxy):
            goods.append(proxy)
            print(proxy)
    save_goods(goods)

elif args.threads == -1:
        # Number of threads = Number of proxies
        t_list = generate_threads(proxies, checker=checker, goods=goods)
        for t in t_list:
            t.start()

        for t in tqdm(t_list):
            t.join()  # Waiting for process end checking
        save_goods(goods, filename=goods_dest)
else:
    threads = args.threads
    sorted_proxies = slice_list(proxies, threads)
    t_list = generate_multi_task_threads(checker=checker, goods=goods, proxies=sorted_proxies)
    for t in t_list:
        t.start()
    for t in tqdm(t_list):
        t.join()
    save_goods(goods, filename=goods_dest)
