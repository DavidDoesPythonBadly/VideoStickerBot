from database import database
from sqlalchemy import Column, BigInteger, Integer, Boolean, String, create_engine
from sqlalchemy.engine import Connectable
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
# from sqlalchemy.orm import _DeclarativeBase
from pystark.config import ENV

class Users(database.base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    packs = Column(Integer)
    ask_emojis = Column(Boolean)
    get_webm = Column(Boolean)
    kang_mode = Column(Boolean)
    default_emojis = Column(String, nullable=True)
    bind = create_engine(ENV.DATABASE_URL)

    def __init__(self, user_id, packs=0, ask_emojis=False):
        self.user_id = user_id
        self.packs = packs
        self.ask_emojis = ask_emojis
        self.bind = create_engine(ENV.DATABASE_URL)
        
