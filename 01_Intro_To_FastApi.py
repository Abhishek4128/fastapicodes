from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return "welcome to api world!"

@app.get("/name")
def getting_name():
    return "john - python developer"