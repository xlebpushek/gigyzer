from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gigyzer.database import UserModel

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()
UserModel.metadata.create_all(engine)


__all__ = ["db_session"]
