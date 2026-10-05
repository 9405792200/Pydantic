from pydantic import BaseModel, Field, field_validator
from typing import Annotated

#Define pydantic model which has schemas & validation constrain
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=20)]
    age: Annotated[int, Field(gt=0, strict=True)]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(description='Married or not')] 
    allergies : Annotated[list[str], Field(max_length=5)]  #allergies should be list of string     
    email : Annotated[str, Field(description='Provide email address')]
    
    #Custom field transformation for attribute name
    @field_validator('name')
    @classmethod    
    def convertCase(cls, value):
        value = value.upper()
        return value
    
    #Custom field transformation for attribute allergies
    @field_validator('allergies')
    @classmethod
    def convertUpperCase(cls, value):
        return [item.upper() for item in value]
    
    #Custom field validation for attribute email    
    @field_validator('email')
    @classmethod
    def validatedEmail(cls, value):
        validDomains = ['hdfc.com', 'icici.com', 'sbi.com']
        domainName = value.split('@')[1]       
        if domainName in validDomains:
            return value
        else: 
            raise ValueError(f"Please provide email with domain {validDomains}")     
    
#Create object of pydantic model
data = {'name':'Bhushan',
        'weight':70,
        'allergies':['Pollen', 'Dust', 'Grass'],
        'married': True, 
        'age':33,
        'email':'bhushanpal93@icici.com'    
       }
pydObj = Patient(**data) #To create Pydantic object from dictionary 

def insertIntoDb(data: Patient):
    print('Patient Data .....')
    print(f'Name = {data.name}')
    print(f'Age = {data.age}')
    print(f'Weight = {data.weight}')
    print(f'Married = {data.married}')
    print(f'Allergies = {data.allergies}')
    print(f'Contact Details = {data.email}')
    print('Data Inserted ...')
    
#Pass pydantic object across function i.e use in code
insertIntoDb(pydObj)

