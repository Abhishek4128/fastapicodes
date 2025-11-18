from fastapi import FastAPI

app=FastAPI()
items={}

@app.get("/")
def getting_items():
    return items

@app.post("/items")
def creating_item(item_id:int,item:dict):
    item_id = max(items.keys(),default=0)+1
    items[item_id] = item
    return {"created":{"item_id":item_id,"item": item}}

@app.put("/items/{item_id}")
def updating_items(item_id:int,item:dict):
    if item_id not in items:
        items[item_id]=item
        return {"added":{"item_id":item_id,"item": item}}
    items[item_id]=item
    return {"updated":{"item_id":item_id,"item": item}}

@app.delete("/items/{item_id}")
def deleting_item(item_id:int):
    if item_id not in items:
        return "item not found"
    del items[item_id]
    return {"deleted":item_id}