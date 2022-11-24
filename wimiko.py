import requests
import time 
import urllib3
import sys
import socket
import ssl

class sptp(object):
    def connect(*args, host):
        class WimikoError(Exception):
            pass

        try:
            while True:
                context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                context.verify_mode = ssl.CERT_REQUIRED
                context.check_hostname = True
                context.load_default_certs()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ssl_sock = context.wrap_socket(s, server_hostname=f'{host}')
                ssl_sock.connect((f'{host}', 443))

        except KeyboardInterrupt:
            print("Tunnel Disconnected from {}".format(host))
            sys.exit()

        except socket.error:
            raise WimikoError("An error accured, check your internet connection and try again.")
    
