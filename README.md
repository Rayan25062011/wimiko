# wimiko
Encrypt data/sockets/packages coming in and out using wimiko

# How to use

```python
from wimiko import *

tunnel = sptp()

tunnel.connect(hosts='www.google.com')
```
