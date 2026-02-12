from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"hello"}


@app.get("/items")
def read_items():
    return {"items":["items1","items2","items3"]}

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{"user_id":user_id,"name":"dasda das"}

@app.post("/items/")
def create_item(name:str,price:float):
    return{"item_name":name,"item_price":price}

@app.put("/items/{item_id}")
def create_item(item_id:int,name:str,price:float):
    return {"item_id": item_id,"item_name": name, "item_price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"dsdsa":f"das{item_id}dasa"}
