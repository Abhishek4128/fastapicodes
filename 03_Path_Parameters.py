from fastapi import FastAPI
app=FastAPI()

@app.get("/users/{user_id}")
def getting_users(user_id:int):
    return  {"user_id":user_id,
             "username":"rana"}

@app.get("/products/{product_id}")
def reading_product(product_id:str):
    return {"product_id":product_id}

@app.get("/users")
def getting_all_users():
    users=[{"user_id":1,"user_name":"john"},
           {"user_id":2,"user_name":"rohit"},
           {"user_id":3,"user_name":"shreyas"}
    ]
    return {"users":users}