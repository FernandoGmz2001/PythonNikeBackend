from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv('DATABASE_URL')

class Database:
    def __init__(self):
        engine = create_engine(database_url)
        self.Session = sessionmaker(bind=engine)

    def execute_query(self, query, params=None):
        with self.Session() as session:
            result = session.execute(query, params)
            if query.lower().startswith(("insert", "update", "delete")):
                session.commit()
            else:
                return result.fetchall()

    def close(self):
        self.Session.close_all()