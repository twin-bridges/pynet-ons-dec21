import yaml
from rich import print
from netmiko import ConnectHandler
import pdbr


def read_yaml_file(filename):
    with open(filename) as f:
        output = yaml.safe_load(f)
        return output


if __name__ == "__main__":

    filename = "/home/ktbyers/.netmiko.yml"

    pdbr.set_trace()
    netmiko_devices = read_yaml_file(filename)

    cisco = netmiko_devices["cisco"]
    arista = netmiko_devices["arista"]
    nxos = netmiko_devices["nxos"]
    juniper = netmiko_devices["juniper"]

    all_devices = cisco + arista + nxos + juniper
    pdbr.set_trace()

    for device_name in all_devices:
        device_dict = netmiko_devices[device_name]
        conn = ConnectHandler(**device_dict)
        print(conn.find_prompt())
        conn.disconnect()
