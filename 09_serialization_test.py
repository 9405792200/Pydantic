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
    allergies: list[str]

address = {'city':'Pune', 'state':'Maharashtra', 'pincode':411028} 
data = {'address': address, 'name':'Bhushan', 'age':33, 'gender': 'male', 'allergies':['Pollen', 'Dust', 'Grass']}

pydObj = Patient(**data)
pythonStdDict = pydObj.model_dump() #To convert a Pydantic model instance into a standard Python dictionary
jsonData = pydObj.model_dump_json() #To Convert a Pydantic model instance into a valid JSON string

print('Type of pydObj = {}'.format(type(pydObj)))
print('Type of pythonStdDict = {}'.format(type(pythonStdDict)))
print('Type of jsonData = {}'.format(type(jsonData)))
print('------------------------------------------------------------------')
print(pythonStdDict)
print('------------------------------------------------------------------')
print(jsonData)

