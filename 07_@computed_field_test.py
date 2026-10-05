from pydantic import BaseModel, Field, computed_field
from typing import Annotated

class Patient(BaseModel):
    name: str
    age: int
    weight: Annotated[float, Field(description='Weight in Kg')]
    married: bool 
    height: Annotated[float, Field(description='Height in Meter')]
    
    #To calculate bmi during Patient() object creation 
    @computed_field    
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2),2)      
        return bmi
        
data = {
    'name' :'Bhushan',
    'age' : 33,
    'weight' : 73,
    'height' : 1.524,
    'married' : True
}

pydObj = Patient(**data)

def insertIntoDb(data: Patient):
    print('Patient Data .....')
    print(data.model_dump()) #To convert a Pydantic model instance into a standard Python dictionary
    print('Data Inserted ...')
    
#Pass pydantic object across function i.e use in code
insertIntoDb(pydObj)