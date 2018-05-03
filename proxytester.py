import time
import requests
import os


def toMilSeconds(time):
    return int(time * 1000)

os.chdir("C:\\XXX\\XXXXX\\XXXXXX\\XXXXXX\\ProxyTester") #Change this to the directory of this program. Add additional \ between the directory
s = requests.Session()
s.headers.update({
    'User Agent': 'Mozilla/5.0'
})

site = "SITE"  #change site to the site you want to test.

with open('proxies.txt') as proxies_list:
    proxies = proxies_list.read().splitlines()

if (len(proxies) == 0):
    print ("No proxies loaded. Please put proxies into proxies.txt!!")
    quit()
else:
    print ("Number of proxies loaded: " + str(len(proxies)))

working_proxies = []


def proxyTester(proxy):
    try:
        proxy_parts = proxy.split(':')
        ip = proxy_parts[0]
        port = proxy_parts[1]
        user = proxy_parts[2]
        passw = proxy_parts[3]

        proxies = {
            'http': 'http://{}:{}@{}:{}'.format(user,passw,ip,port),
            'https': 'https://{}:{}@{}:{}'.format(user,passw,ip,port),
        }

        s.proxies = proxies
    except IndexError:
        proxies = {'http': 'http://' + proxy, 'https:': 'https://' + proxy}

    start = time.time()
    try:
        response = s.get(site)
        if (response.status_code != 200):
            print('{} doesnt work'.format(proxy))
        else:
            stop = time.time()
            ping = toMilSeconds(stop - start)
            print (proxy)
            print ('{} works on ' + site)
            print ('ping: ' + str(ping))
            working_proxies.append(proxy)
    except:
        print('Bad Proxy!')

            
#main
for p in proxies:

    proxyTester(p)

print(working_proxies)
