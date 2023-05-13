import os
from dotenv import load_dotenv


# load environment variable
load_dotenv()

TOKEN = os.environ.get("token")
