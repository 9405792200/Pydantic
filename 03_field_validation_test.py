from pydantic import BaseModel, PositiveInt, PositiveFloat, EmailStr, Field

class Patient(BaseModel):
    name: str = Field(default=..., description='Name of Patient', frozen=True)
    age: PositiveInt = Field(default=..., description='Age of Patient', le=100) #An integer that must be greater than zero due to positive int & less than equal to 100 due to le=100
    weight: PositiveFloat = Field(strict=True)   #A float that must be greater than zero.strict to avoid type conversion
    email : EmailStr        #The input string must be a valid email address.
    married: bool  
    allergies: list[str] = Field(max_length=5) #Only 5 allergies accepted      

#Create object of pydantic model
data = {'name':'Bhushan',
        'weight':70.9,
        'allergies':['Pollen', 'Dust', 'Grass'],
        'married': True, 
        'age':33,
        'email':'abc@gmail.com'        
       }
pydObj = Patient(**data) #To create Pydantic object from dictionary 

def insertIntoDb(data: Patient):
    print('Patient Data .....')
    print(f'Name = {data.name}')
    print(f'Age = {data.age}')
    print(f'Weight = {data.weight}')
    print(f'Email = {data.email}')
    print(f'Married = {data.married}')
    print(f'Allergies = {data.allergies}')    
    print('Data Inserted ...')
    
#Pass pydantic object across function i.e use in code
insertIntoDb(pydObj)
