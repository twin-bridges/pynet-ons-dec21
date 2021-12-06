import requests
import json
from rich import print
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning
import pdbr  # noqa

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    pdbr.set_trace()

    http_headers = {"Content-Type": "application/json-rpc;"}
    host = "arista1.lasthop.io"
    port = 443
    username = "pyclass"
    password = getpass()

    url = "https://{}:{}/command-api".format(host, port)

    json_payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {"version": 1, "cmds": ["show version"], "format": "json"},
        "id": "1",
    }
    json_data = json.dumps(json_payload)
    http_headers["Content-length"] = str(len(json_data))

    response = requests.post(
        url,
        headers=http_headers,
        auth=(username, password),
        data=json_data,
        verify=False,
    )
    response = response.json()

    print()
    print(response)
    print()
