#this file is used to connect the project with the database
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#every time we have to execute any method of http we first have to create a session with the database at first so we create this session maker and then we will import the session object we have created here, wherever we need to make a connection with the databse


url="postgresql://postgres:NithinP%40123@localhost:5432/nithin"  #the last thing you wrote there is the databse name
engine =create_engine(url)
session = sessionmaker(autocommit = False, autoflush=False,bind=engine)
#autoflus:- when you write any query the query doesnt execute all of a sudden if you haeve autflush false, so everytime you write a query you have to flush manually
#auto commit:- when you have auto commit as false the changes doesnt get sasved in the databse so after executing each and every query you have to manually write yourslef the commit and then proceed