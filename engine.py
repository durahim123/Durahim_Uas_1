import os
from sqlalchemy import create_engine

from sqlalchemy import MetaData

meta = MetaData()

USER = os.getenv("DB_USER", "postgres")
PASSWORD = os.getenv("DB_PASSWORD", "123ere123")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")
NAME = os.getenv("DB_NAME", "uas1")

base_engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}')
