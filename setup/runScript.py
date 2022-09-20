import os
from dotenv import load_dotenv

load_dotenv()
scrpt = os.getenv('SCRIPT')
os.system(scrpt)


