# scraping_utilities

Scraping utilities. Proxy and user-agent retrievers and rotators.

## What it does and for what is useful

Basically, it scrapes two web pages:

+ [developers.whatismybrowser](https://developers.whatismybrowser.com/) for user-agent retrieval.
+ [free-proxy-list](https://free-proxy-list.net/) for proxy retrieval.

And obtains two sets: one of proxies, ip:port, and another of user-agents.

This two sets are useful for scraping pages with "*safety*". Or better said to avoid getting blocked.

## How to use them

In `utils.py` two classes can be found `UserAgentRotator` and `ProxyRotator`

### Proxies

Only serves proxies from elite-proxy and those that support https.

First import and initialize the class:

```python
from utils import ProxyRotator

proxy\_rotator = ProxyRotator()

```

After this, if `proxy_server` is called it will return a ip:port of a random proxy.

```python
sample\_proxy = proxy\_rotator.proxy_server()
```

With an output such as `{'https': '103.216.82.153:6666'}`. The list of proxys can be seen with `roxy\_rotator.proxies`

### User Agents


