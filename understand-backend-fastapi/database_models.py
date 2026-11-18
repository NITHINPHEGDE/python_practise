#we have to create this file as a reference model for all the queries of the api's

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,Float,String

'''''Think of Base as a parent class for all your database models.

Whenever you create a database model, you inherit from Base.
By inheriting from Base, SQLAlchemy understands that Products is a database model.

In simple words, you're telling SQLAlchemy:

"Hey, this class represents a table in my PostgreSQL database."'''

Base = declarative_base()
class Products(Base):

  __tablename__ = "product"
  id = Column(Integer,primary_key=True,index=True)
  name = Column(String)
  description = Column(String)
  price = Column(Float) 
  quantity = Column(Integer)
