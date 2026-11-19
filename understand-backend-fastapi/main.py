from fastapi import FastAPI,Depends
from model import Products
from databaseconfig import session,engine
import database_models 
from sqlalchemy.orm import Session


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)
"""""database_models
This refers to the Python file where you defined your database models.
Base is the parent class of all your SQLAlchemy models.
This is where SQLAlchemy keeps information about your database tables.

For example, it knows:
- Table name: products
- Column: id
- Column: name
- Data types
- Primary keys
Think of metadata as a collection of information about your database structure.
create_all()
This tells SQLAlchemy:

"Create all the tables defined in my models if they don't already exist."

For example, if you have:
class Products(Base):    __tablename__ = "products"


SQLAlchemy creates a products table in PostgreSQL.

Important: It doesn't recreate existing tables or automatically update their structure.

bind=engine
Remember your database engine?
engine = create_engine(DATABASE_URL)


The engine knows how to connect to PostgreSQL.

bind=engine tells SQLAlchemy which database to create the tables in."""

@app.get("/")
def greet():
  return "hello and welcome to fast api"


products = [
  Products(id=1, name="Wireless Mouse", description="Ergonomic Bluetooth mouse", price=24.99, quantity=35),
  Products(id=2, name="Mechanical Keyboard", description="Compact RGB mechanical keyboard", price=79.50, quantity=18),
  Products(id=3, name="USB-C Hub", description="Seven-port USB-C hub", price=42.00, quantity=27),
  Products(id=4, name="Laptop Stand", description="Adjustable aluminum laptop stand", price=36.75, quantity=12),
  Products(id=5, name="Webcam", description="1080p webcam with built-in microphone", price=54.99, quantity=21),
  Products(id=6, name="Desk Lamp", description="LED desk lamp with brightness control", price=29.25, quantity=16),
]

def get_db():
  db=session()
  try:
    yield db   #everytime we have to make a database operation we will use this function and what yield does is it makes all the faciliteis for a query to get executed 
  finally:
    db.close()


def init_db():
  db=session()
  for product in products:
    db.add(database_models.Product(**product.model_dump()))
    """This line takes the product data received through the FastAPI request and converts it into a format that SQLAlchemy understands. First, product.model_dump() converts the Pydantic model into a Python dictionary containing the product details. Then, ** unpacks that dictionary into individual keyword arguments, which are passed to database_models.Product() to create a SQLAlchemy object representing a database row. Finally, db.add() adds that object to the current database session, marking it for insertion into PostgreSQL. The actual transaction is committed when you call db.commit().

In short: It converts API data into a database object and stages it for insertion into PostgreSQL."""
  db.commit()

init_db()

@app.get("/products")
def get_products(db:Session = Depends(get_db) ):#This line tells FastAPI to automatically create a database session by executing the get_db() function and provide that session to the API endpoint through the variable db. Here, db stores the database session, Session specifies its SQLAlchemy type, and Depends(get_db) tells FastAPI to handle the creation and injection of that session automatically. Typically, get_db() uses yield to provide the session to the endpoint and finally to close it once the request is completed. This avoids manually creating and closing database sessions in every API endpoint.
  db_products = db.query(database_models.Product).all
  return db_products


@app.get("/product/{id}")
def getproductbyid(id: int):
  for product in products:
    if product.id == id:
      return product
  return "product not found"

@app.post("/product")
def addproduct(product: Products):
  products.append(product)
  return product

# now put method is updating thedata in the and lets see how it works
@app.put("/product/{id}")
def updateproduct(id: int, product: Products):
  for i in range(len(products)):
    if products[i].id == id:
      product.id = id
      products[i]=product
      return "updated succefully"
  return "product not found"

@app.delete("/product")
def deleteproduct(id:int):
  for i in range(len(products)):
    if products[i].id==id:
      del products[i]
      return "rpoduct deleted"
  return " product not found"