from pydantic import BaseModel

#Define pydantic model which has schemas & validation constrain
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool 
    allergies : list[str]  #allergies should be list of string 
    contactDetails : dict[str, str] #contactDetails should be dict of key-value pair of string
    
#Create object of pydantic model
data = {'name':'Bhushan',
        'weight':70,
        'allergies':['Pollen', 'Dust', 'Grass'],
        'married': True, 
        'age':33,
        'contactDetails':{'MobNo':'9405792200', 'Email':'bhushanpal93@gmail.com'}
       }
pydObj = Patient(**data) #To create Pydantic object from dictionary 

def insertIntoDb(data: Patient):
    print('Patient Data .....')
    print(f'Name = {data.name}')
    print(f'Age = {data.age}')
    print(f'Weight = {data.weight}')
    print(f'Married = {data.married}')
    print(f'Allergies = {data.allergies}')
    print(f'Contact Details = {data.contactDetails}')
    print('Data Inserted ...')
    
#Pass pydantic object across function i.e use in code
insertIntoDb(pydObj)

