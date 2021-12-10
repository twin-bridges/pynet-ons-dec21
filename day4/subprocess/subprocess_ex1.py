import subprocess
import re
from pprint import pprint


def subprocess_wrapper(cmd_list, raise_error=True):
    """Wrapper to execute subprocess including byte to UTF-8 conversion."""
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = proc.communicate()
    (std_out, std_err) = [x.decode("utf-8") for x in (std_out, std_err)]
    if raise_error and std_err:
        print(f"An error occurred:\n{std_err}")

    return (std_out, std_err, proc.returncode)


if __name__ == "__main__":

    cmd_list = ["df", "-h"]
    std_out, _, _ = subprocess_wrapper(cmd_list)
    print(std_out)
