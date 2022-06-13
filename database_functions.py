

from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, Date,  Integer, String, Boolean ,DateTime
from sqlalchemy.orm import declarative_base, registry, sessionmaker
import os

Base = declarative_base()

########################################################################
class Cart(Base):
    """"""
    __tablename__ = 'ev_cart'
    id = Column(Integer, primary_key = True, autoincrement=True)
    title = Column(String, nullable = True)
    images = Column(, nullable = True)

    def __init__(self, user, time, time_after48, is_time, submitted):
        self.user = user
        self.time = time
        self.time_after48 = time_after48
        self.is_time = is_time
        self.submitted = submitted
        

Base.metadata.create_all(engine)
print("base connected")