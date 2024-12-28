> [!CAUTION]
> WIP! Very much under development. Script is working but documentation hasn't been thoroughly tested. Planning on some automation for installing dependencies.
# Testing self hosted SearXNG metasearch engine

Created and tested with Ubuntu 24.04.1 LTS desktop and Ubuntu 22.04.5 LTS desktop as server in 2024/12. 

These Python scripts are for testing queries on self hosted SearXNG metasearch engine. 
https://github.com/searxng/searxng  
Scripts require SearXNG instance URL as **SEARCH_ENGINE_URL** variable in **.env** file **in same directory with script**.

```bash
# Your SearXNG URL here before "/search?q=$s" as in
# "https://your.searxng.url.here/search?q=$s"
SEARCH_ENGINE_URL = "https://your.searxng.url.here/search?q=$s" 
```
Setup
- 
### Ubuntu 22.04.5 LTS desktop as server
Operating system for Docker and SearXNG container. https://ubuntu.com/download
### Tailscale
For connectivity https://tailscale.com/
> ...software-defined mesh virtual private network (VPN)...

### Docker engine
Installation scripts for various operating systems can be found at https://github.com/sloul1/docker
### Self hosted SearXNG instance on Docker with SSL certificates

For hosting my own instance of SearXNG I used Alex Kretzchmar's instructions at https://blog.ktz.me/replacing-google-with-searxng-as-the-default-in-chrome/ and at Tailscale YouTube channel https://www.youtube.com/watch?v=cg9d87PuanE .

### Python, virtual environment and some pip dependencies
Query if Python is installed and what version:
```bash
whereis python3 && python3 -V
```
Query should give installation path as result.
```bash
python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz
Python 3.12.3
```
If for some reason Python is not present it can be installed:
```bash
sudo apt update && sudo apt install python3
```
https://docs.python.org/3/library/venv.html#  
  
Create Python virtual environment:
```bash
python -m venv /path/to/new/virtual/environment
```
Activate Python virtual environment:
```bash
source venv/bin/activate
```

Venv can be deactivated by just typing **deactivate**.
```bash
(venv) peppertp15ubu@peppertp15ubu-ThinkPad-E15-Gen-3:~/github/sloul1/searxng-testing$ deactivate
```
Resulting:
```bash
peppertp15ubu@peppertp15ubu-ThinkPad-E15-Gen-3:~/github/sloul1/searxng-testing$
```
When Python virtual environment is activated there is "(venv)" text in start of terminal:
```bash
(venv) peppertp15ubu@peppertp15ubu-ThinkPad-E15-Gen-3:~/github/sloul1/searxng-testing$
```
Pip dependencies should be installed when (venv) is active.
```bash
pip install python-dotenv requests
```
Single thread script can be run:
```bash
python3 searxng-testing.py
```
When **# Conditions for stopping** are met defined in script: 
```bash
Elapsed time: 10.510577917098999 seconds
Requests: 14
Pending requests: 6
```

This is an excellent example of learning about rate limiting harder way. Too many searches within too little time can result blocking your IP address on search engines.
![](images/ratelimiting-01.png)
I suggest not to use too high numbers in **searxng-parallel.py** script's **num_threads = 2** and **range(25)** values.
```python
    num_threads = 2
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _ in range(25):
            for query in search_queries:
                future = executor.submit(search, query)
                futures.append(future)
                #time.sleep(0.1)  # Uncomment toadd delay (in seconds) between searches
```
> [!WARNING] Running too many parallel requests at high rate results rate limiting suspension (=blocking) on search engines. 
![](images/ratelimiting-02.png)  
Suspension time may vary on different search engines.
