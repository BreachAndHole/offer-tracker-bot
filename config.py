import os
import dotenv


dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

DB_FILE_NAME = 'offers.db'
