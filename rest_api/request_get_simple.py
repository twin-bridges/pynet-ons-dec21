import requests
from rich import print
import pdbr  # noqa


if __name__ == "__main__":

    url = "https://netbox.lasthop.io/api/dcim/"
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    print()
    print(response)
    print()
