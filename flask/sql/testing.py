import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()  # reads variables from a .env file and sets them in os.environ

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

# print(os.environ.keys())
print('-' * 50)
print(os.getenv('ROOT_URL'))
print(os.getenv('ADMIN_EMAIL'))
print(os.getenv('DOMAIN'))

print('-' * 50)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
print(path)
config = dotenv_values(path)
print(config)
