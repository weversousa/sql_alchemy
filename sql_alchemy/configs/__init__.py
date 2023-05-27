from os import getenv
from os.path import join
from pathlib import Path

from dotenv import load_dotenv


ROOT_PATH = Path().absolute()

load_dotenv(dotenv_path=join(ROOT_PATH, '.env'))

DATABASE_URL: str = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
    getenv('DATABASE_USER'),
    getenv('DATABASE_PASSWORD'),
    getenv('DATABSE_HOST'),
    getenv('DATABASE_PORT'),
    getenv('MYSQL_DATABASE')
)
