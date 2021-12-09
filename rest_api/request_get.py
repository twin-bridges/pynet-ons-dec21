import requests
from rich import print
import pdbr  # noqa
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    url = "https://netbox.lasthop.io/api/dcim/"
    # url = 'http://netbox.lasthop.io/api/dcim/devices/'
    # url = "https://api.github.com/"
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)

    # pdbr.set_trace()
    response = response.json()

    print()
    print(response)
    print()
