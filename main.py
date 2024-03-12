from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_app():
        return {"message" : "Hello World!"}

@app.post("/", description = "Post app")
async def post():
        return {"message" : "Hello from post route"}

@app.put("/")
async def put():
        return {"message" : "Hello from put route"}



#path-parameters

# @app.get("/items") #if i add "/items" after the localhost route, then the below content will be displayed
# def list_items():
#         return {"message": "list items route"}

# @app.get("/items/{item_id}") #add route for the existing route
# def get_item(item_id : int): #we can add type for parameter passed like def get_item(item_id : int)
#         return {"item_id": item_id}



@app.get("/users/me")
def get_user():
        return {"user_id": "I am the current user"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
        return {"user_id": user_id}
# specific paths like me, host should be put before the general one which takes id as input 
# because fastAPI scans the input from top to bottom and it print whichever path it matches with first



#Enum usage

from enum import Enum

class FoodEnum(str, Enum):
        fruits = "fruits"
        vegetables = "vegetables"
        dairy = "dairy"

@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
        if food_name == FoodEnum.vegetables:
                return {"food name": food_name, "message": "healthy vegetables"}
        if food_name == FoodEnum.fruits:
                return {"food name": food_name, "message": "sweet fruits"}
        return {"food name": food_name, "message": "dairy product"}


# query paramaters
# we do not include item name or id in route in this case, we just take the item as a parameter in function header!


items_db = [{"item_name": "abcd"}, {"item_name": "pqrs"}, {"item_name": "wxyz"}, {"item_name": "mnop"}]
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
        return items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_items(item_id, q : str | None = None):           #here, item_id is path parameter and q is a query parameter
        if q:
                return {"item_id": item_id, "q": q}
        return {"item_id": item_id}

@app.get("/items/{item_id}/users/{user_id}")
async def get_item_user(item_id : int, user_id : int, q : str | None = None, short:bool = False):
        item = {"item_id": item_id, "owner_id": user_id}
        if q:
                item.update({"q": q})
        if not short:
                item.update({
                        "description": "lorem ipsum dolor......."
                        })
        return item