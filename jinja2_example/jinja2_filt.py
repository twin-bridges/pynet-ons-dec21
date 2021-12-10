from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from my_code import say_hello

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])
env.filters["say_hello"] = say_hello

my_vars = {"bgp_as": 22, "router_id": "1.1.1.1", "peer1": "10.20.30.1"}

template_file = "bgp_config.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
