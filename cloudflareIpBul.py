import requests

for a in range(0,256):
    for b in range(0, 256):
        for c in range(0, 256):
            for d in range(0, 256):
                ipAddress = str(a)+"."+str(b)+"."+str(c)+"."+str(d)
                ip_headers = {"Host": "behindcloudflareexample.com"}
                w = requests.get(ipAddress, headers=ip_headers)
                if w.status_code == 200:
                    print("Founded "+ipAddress)