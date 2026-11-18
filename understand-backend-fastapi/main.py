from fastapi import FastAPI
from model import Products
from databaseconfig import Session,engine
import database_models 


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

def init_db():
  db=Session()
  for product in products:
    db.add(database_models.Product(**product.model_dump()))
  db.commit()

init_db()

@app.get("/products")
def get_products():
  db=Session()
  return products

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