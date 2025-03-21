from dotenv import dotenv_values
from others import parse_to_string_list

env = dotenv_values(".env")
print(parse_to_string_list(env["MODELS"]))