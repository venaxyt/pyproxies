> # PYPROXIES

``Please subscribe to my Github @venaxyt if you want more modules like this.``<br/>
**Pyproxies only returns proxy, it does not print them like on screenshot.**

## Send a request with http proxy
```
http_proxy = pyproxies.proxy("http")
proxy_ip = requests.get("https://api.ipify.org", proxies=http_proxy)
print(f" [IP] : {http_proxy}")
```
![http](https://user-images.githubusercontent.com/81310818/131668032-3ca5803c-f709-49bc-a243-b978f8293921.PNG)
## Send a request with socks4 proxy
```
socks4_proxy = pyproxies.proxy("socks4")
proxy_ip = requests.get("https://api.ipify.org", proxies=socks4_proxy)
print(f" [IP] : {socks4_proxy}")
```
![socks4](https://user-images.githubusercontent.com/81310818/131668049-e8eb6e97-1fc8-46df-9222-e38450d1469b.PNG)
## Send a request with socks5 proxy
```
socks5_proxy = pyproxies.proxy("socks5")
proxy_ip = requests.get("https://api.ipify.org", proxies=socks5_proxy)
print(f" [IP] : {socks5_proxy}")
```
![socks5](https://user-images.githubusercontent.com/81310818/131668046-1d9d3683-2a9f-41d0-a786-ac4428c24cdf.PNG)

## Informations:
Pyproxies check every proxy it returns, by sending a request to "api.ipify.org", a website which returns requester ip adress.
Pyproxies only returns valid proxies whose timeout is less than 10 seconds, you can edit the timeout in the module code.
All proxies comes from proxyscrape.com, you can edit the proxies source in the module code too.
Thanks for using my modules, @venaxyt.

> ### Download : pip install pyproxies
> ### Documentation : https://pypi.org/project/pyproxies
