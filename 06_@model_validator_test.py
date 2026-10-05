from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated

#Define pydantic model which has schemas & validation constrain
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=20)]
    age: Annotated[int, Field(gt=0, strict=True)]
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(description='Married or not')] 
    allergies : Annotated[list[str], Field(max_length=5)]  #allergies should be list of string     
    email : Annotated[EmailStr, Field(default=None,description='Provide email address')]        
 
    @model_validator(mode='after')
    def validateModel(self):        
        if self.age >= 60 and self.email == None:
            raise ValueError('For age older than 60 email should present')            
        return self
        
#Create object of pydantic model
data = {'name':'Bhushan',
        'weight':70,
        'allergies':['Pollen', 'Dust', 'Grass'],
        'married': True, 
        'age':61,
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

