from pydantic import BaseModel

class Products(BaseModel):
  id : int
  name : str
  description : str
  price : float 
  quantity : int



"""
with base model library you can write this code instead of writing traditional constructor methiod which is 
class Products:
  def __inti__(self,id,name,description,price,quantity):
  self.id=id
  self.decription=description
  self.name=name
  self.price=price
  self.quantity=quantity
"""