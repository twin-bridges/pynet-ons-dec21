import requests
import os

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices/34/"
    http_headers = {
        "Content-Type": "application/json; version=2.4;",
        "authorization": "Token {}".format(token),
    }
    response = requests.delete(url, headers=http_headers, verify=False)
    if response.ok:
        print("Device deleted successfully")
