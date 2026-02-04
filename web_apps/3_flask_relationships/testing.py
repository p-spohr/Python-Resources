from dotenv import load_dotenv
import sys, pathlib, os

base_dir = pathlib.Path(__file__).absolute().parent 

load_dotenv(base_dir.joinpath('.env'))

flask_config = os.environ.get('FLASK_APP')
print(flask_config)