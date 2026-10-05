from pydantic import BaseModel

#Define Pydantic model, inherit BaseModel 
class patient(BaseModel):
    name: str 
    age: int

#Create object of Pydantic model
data = {'name':'Bhushan', 'age': '33'}
pyObj = patient(**data) #** to unpack dictionary & create Pydantic object

#Use pyObj across code 
print(f'name = {pyObj.name} age = {pyObj.age}')
