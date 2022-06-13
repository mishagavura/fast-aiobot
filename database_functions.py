from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, Date,  Integer, String, Boolean ,DateTime, ForeignKey,Float
from sqlalchemy.orm import declarative_base, registry, sessionmaker, relationship
import os

Base = declarative_base()

########################################################################
class Cart(Base):
    """"""
    __tablename__ = 'ev_cart'
    id = Column(Integer, primary_key = True, autoincrement=True)
    title = Column(String, nullable = True)
    images = relationship("Images", secondary=association_table)
    sizes = relationship("Sizes", secondary=association_table)


    def __init__(self, title, images, sizes):
        self.title = title
        self.images = images
        self.sizes = sizes

class Images(Base):
    __tablename__ = 'ev_images'
    id = Column(Integer, primary_key = True, autoincrement=True)
    title = Column(String, nullable = True)
    description = Column(String, nullable = True)
    image_url = Column(URLType, nullable = True)

    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

class Sizes(Base):
    __tablename__ = 'ev_sizes'
    id = Column(Integer, primary_key = True, autoincrement=True)
    weight = Column(Float, nullable = True)
    metrics = Column(String, nullable = True)
    price = Column(Float, nullable = True)
    discount_percent = Column(Integer, nullable = True)

    def __init__(self, weight, metrics, price, discount_percent):
        self.weight = weight
        self.metrics = metrics
        self.image_url = image_url
        self.price = price
        self.discount_percent = discount_percent


Base.metadata.create_all(engine)

