from urllib import request
import requests,threading,os,random

cit = 0
failed = 0
readproxy = open('proxies.txt','r')
readproxy2 = readproxy.readlines()
workproxy = []
for proxy3 in readproxy2:
    proxystrip = proxy3.strip('\n')
    workproxy.append(proxystrip)

os.system("cls")
print("discord.gg/catcha | dsc.gg/catcha")
print("dsc.gg Click baiter")

def click():
    global cit,failed,code
    try:
        proxyb = random.choice(workproxy)

        proxies = {'http': f'http://{proxyb}','https':f'http://{proxyb}'}
        r = requests.get(f"https://dsc.gg/{code}?ref=homepage", proxies=proxies)
        cit +=1
    except:
        failed +=1
    os.system(f"title Hits: {cit} ^| Failed {failed}")

th = int(input("Threads -->"))
code = input("Code to bot -->")

while True:
    if threading.active_count() < th:
        for x in range(th):
            threading.Thread(target=click).start()


