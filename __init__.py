# Module made by @venaxyt on Github
import requests

def proxy(server):
    working_proxy = False
    while not working_proxy:
        if server == "http":
            server_proxy_list = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&co").text
        elif server == "socks4":
            server_proxy_list = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1000&co").text
        elif server == "socks5":
            server_proxy_list = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1000&co").text
        else:
            raise Exception("Error : You only can use http, socks4 and socks5 proxies.")
        server_proxy = random.choice(server_proxy_list.splitlines())
        proxy = {"https": f"{server}://{server_proxy}"}
        try:
            requests.get("https://api.ipify.org", proxies = proxy, timeout = 10)
            working_proxy = True
        except:
            pass
        if working_proxy == True:
            return proxy
