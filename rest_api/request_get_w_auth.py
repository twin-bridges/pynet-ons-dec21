import requests
import os
from rich import print
import pdbr
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    # token = "bad"

    # url = "https://netbox.lasthop.io/api/dcim/devices"
    url = "https://netbox.lasthop.io/api/dcim/devices/1/"
    http_headers = {"accept": "application/json; version=2.4;"}
    if token:
        http_headers["authorization"] = "Token {}".format(token)

    response = requests.get(url, headers=http_headers, verify=False)

    pdbr.set_trace()
    response = response.json()

    print()
    print(response)
    print()
