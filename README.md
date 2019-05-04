# scraping_utilities

Scraping utilities. Proxy and user-agent retrievers and rotators.

## What it does and for what is useful

Basically, it scrapes two web pages:

+ [developers.whatismybrowser](https://developers.whatismybrowser.com/) for user-agent retrieval.
+ [free-proxy-list](https://free-proxy-list.net/) for proxy retrieval.

And obtains two sets: one of proxies, ip:port, and another of user-agents.

This two sets are useful for scraping pages with "*safety*". Or better said to avoid getting blocked.

The first time the program scrapes the webs it stores the results in two files just to avoid rescraping again and again. Nevertheless, if you want to scrape the pages again you can initialize the
objects `ProxyRotator` and `UserAgentRotator` with the argument `reload=True`.

## How to use them

In `utils.py` two classes can be found `UserAgentRotator` and `ProxyRotator`

### Proxies

Only serves proxies from elite-proxy and those that support https.

First import and initialize the class:

```python
from utils import ProxyRotator

proxy_rotator = ProxyRotator()

```

After this, if `proxy_server` is called it will return a ip:port of a random proxy.

```python
proxy_rotator.proxy_server()
```

With an output such as `{'https': '103.216.82.153:6666'}`. The list of proxys can be seen with `roxy_rotator.proxies`

### User Agents

Works in the same way as the proxy rotator. However, in the class initialization it incorporates two options: `max_pages` and `name_regex`.

```python
from utils import UserAgentRotator

user_rotator = UserAgentRotator(name_regex=r'(Linux|Computer|Chrome|Web Browser)', max_pages = 2)
```

`name_regex` chooses which kind of user-agents will be retrieved. The default is `r'(Linux|Computer|Chrome|Web Browser)'`. Take a look at the web page and change it appropiately with the name of the user-agents that you want to retrieve. `max_pages` controls how many pages are used to retrieve user-agents from each type. Beware that a high number here will imply a long scraping time.

You can retrieve a user-agent randomly with:

```python
user_rotator.user_agent_server()
```

Producing the following output: `'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'`

### Example with requests

```python

from requests import get

req = get("www.google.com", proxies=proxy_rotator.proxy_server(), headers = {'User-Agent': user_rotator.user_agent_server()}
```


