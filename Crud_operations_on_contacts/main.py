from fastapi import FastAPI,Request
app=FastAPI()

contacts=[
    {
       'id': 1,
       'name': 'John',
       'phoneno': '7013908752'

    },
    {
        'id': 2,
       'name': 'rohit',
       'phoneno': '2767676254'
    }
]

@app.get("/")
def getting_all_contacts():
    return contacts

@app.get("/contact")
def getting_single_cont(contact_id:int):
    for con in contacts:
        if con['id']==contact_id:
            return con
    return "contact not found"

@app.post("/add/contact")
async def adding_contacts(request: Request):
    data=await request.json()
    contacts.append(data)
    return data

@app.put("/contact")
async def updating_contacts(request: Request):
    data= await request.json()
    for cont in contacts:
        if cont['id']==data['id']:
            cont.update(data)
            return contacts
    return "contact not found"
    
@app.delete("/contact/{contact_id}")
def deleting_contact(contact_id):
    for cont in contacts:
        if cont['id']==int(contact_id):
            contacts.remove(cont)
            return contacts
    return "contact not found"

#by using class(basemethod)
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Contact(BaseModel):
#     id: int
#     name: str
#     phoneno: str

# contacts = [
#     {
#         "id": 1,
#         "name": "John",
#         "phoneno": "7013908752"
#     },
#     {
#         "id": 2,
#         "name": "rohit",
#         "phoneno": "2767676254"
#     }
# ]

# @app.get("/")
# def getting_all_contacts():
#     return contacts

# @app.get("/contact")
# def getting_single_cont(contact_id: int):
#     for con in contacts:
#         if con["id"] == contact_id:
#             return con
#     return {"message": "contact not found"}

# @app.post("/add/contact")
# def adding_contacts(contact: Contact):
#     contacts.append(contact)
#     return contact

# @app.put("/contact")
# def updating_contacts(contact: Contact):
#     for cont in contacts:
#         if cont["id"] == contact.id:
#             cont.update(contact)
#             return contacts
#     return {"message": "contact not found"}

# @app.delete("/contact/{contact_id}")
# def deleting_contact(contact_id: int):
#     for cont in contacts:
#         if cont["id"] == contact_id:
#             contacts.remove(cont)
#             return contacts
#     return {"message": "contact not found"}
