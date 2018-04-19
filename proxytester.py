import requests
import time

work = 'working'
banned = 'banned'
proxy_file = open(r"LOCATION") #change location to the location of ur proxies.txt
proxy_list = proxy_file.readlines()
num_proxies = len(proxy_list)

for i in range(num_proxies):
    now = time.time()
    proxy = {
        "https": proxy_list[i]
    }

    req = requests.get("http://google.com",proxies = proxy) #change site to your desired
    print (proxy_list[i])
    print (req)
    after_req = time.time()        
    print ("ms:")
    print (round((after_req - now) *100)) #prints time it takes for it to make the request
