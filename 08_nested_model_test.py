from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name : str
    age: int
    gender: str
    address : Address 

address = {'city':'Pune', 'state':'Maharashtra', 'pincode':411028} 
data = {'address': address, 'name':'Bhushan', 'age':33, 'gender': 'male'}

pydObj = Patient(**data)

print(pydObj.model_dump()) #To convert a Pydantic model instance into a standard Python dictionary