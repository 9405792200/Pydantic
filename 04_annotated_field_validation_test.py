from pydantic import BaseModel,Field
from typing import Annotated

#Annotated is not introducing new functionality. Its main purpose is cleaner type hints, better static type checking, and a standardized way to attach metadata to a Python type
#Annotated[T, X] annotated Separates Type and Metadata. where T is python type & X is metadata

class Patient(BaseModel):
    name     :Annotated[str, Field(default=..., description='Name of Patient', frozen=True)]
    age      :Annotated[int, Field(default=..., description='Age of Patient', gt=0, le=100)] #An integer that must be greater than zero due gt=0 & less than equal to 100 due to le=100
    weight   :Annotated[float, Field(gt=0, strict=True)]   #A float that must be greater than zero. strict to avoid type conversion 
    married  :Annotated[bool, 'married or not']  
    allergies:Annotated[list[str], Field(max_length=5)] #Only 5 allergies accepted      

#Create object of pydantic model
data = {'name':'Bhushan',
        'weight':70,
        'allergies':['Pollen', 'Dust', 'Grass'],
        'married': True, 
        'age':33          
       }
pydObj = Patient(**data) #To create Pydantic object from dictionary 

def insertIntoDb(data: Patient):
    print('Patient Data .....')
    print(f'Name = {data.name}')
    print(f'Age = {data.age}')
    print(f'Weight = {data.weight}')    
    print(f'Married = {data.married}')
    print(f'Allergies = {data.allergies}')    
    print('Data Inserted ...')
    
#Pass pydantic object across function i.e use in code
insertIntoDb(pydObj)
