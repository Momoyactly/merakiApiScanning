import requests

url = "https://api.meraki.com/api/v0/networks/L_664280945037169055/portForwardingRules"

payload = {
    "rules": [
        {
            "lanIp": "192.168.30.16",
            "name": "SSH",
            "allowedIps": [
                "0.0.0.0/0"
            ],
            "publicPort": "22",
            "localPort": "22",
            "uplink": "internet1",
            "protocol": "tcp"
        }
    ]
}
headers = {
  'X-Cisco-Meraki-API-Key': '6f58931428519a7ffd9624ff522ea8ea2dde0e10',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, json = payload)

print(response.text.encode('utf8'))
