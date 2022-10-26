from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import Configuration

db = create_engine(Configuration.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=db)
session = Session()
session._model_changes = {}